import numpy as np
from skimage.draw import polygon2mask
import pycocotools.mask as coco_mask
from detectron2.structures import BoxMode
import os
import dask.dataframe as dd
import itertools

HEIGHT = 295
WIDTH = 510

def load_mask(polygon_vertices):
    """Recebe os vértices de um polígono e retorna sua máscara binária.

    Args:
        polygon_vertices (list): Lista com os vértices de um polígono anotado.

    Returns:
        ndarray: Máscara binária que representa o polígono anotado.
    """

    mask = np.zeros([HEIGHT, WIDTH], dtype=np.uint8) #Dim: Height, Width, 3 (RGB - 3 canais de cores)

    calculatedMask = polygon2mask(mask.shape, polygon_vertices)

    #Atribui o valor 1 para os pontos onde o polígono existe. O restante permanece como 0.
    mask[calculatedMask] = 1

    return mask

def getPolygonPoints(line):
    """Calcula os pontos de um polígono com base em uma linha.

    Args:
        line (list): Uma lista representando 2 linhas com 8 pontos [x1, y1, x2, y2, ...].
                     Essa lista vem com as colunas adicionais da anotação, que são removidas aqui nesta função.

    Returns:
        dict: Um dicionário contendo uma máscara (mask) baseada nos pontos do polígono.
    """

    '''O primeiro elemento é removido pois como recebemos todas as colunas de anotação, o primeiro
    elemento é uma string contendo o frame_id'''
    line.pop(0)

    line = np.array(line)
    listOfPoints_y = []
    listOfPoints_x = []

    for i in range(2):

        m = (int(line[3]) - int(line[1])) / (int(line[2]) - int(line[0]) + 0.000001)
        b = int(line[1]) - m * int(line[0])

        if m == 0:
            return False

        y = np.array([0, 640])
        x = np.array([(y[0] - b) / m, (y[1] - b) / m])

        '''Subtraímos 65 pixels de cada dimensão pois as imagens originais foram cortadas
        para remoção dos dados sensíveis.'''
        x -= 65
        y -= 65

        if not i:
            listOfPoints_x.extend((int(x[0]) / 1.0, int(x[1]) / 1.0))
            listOfPoints_y.extend((int(y[0]) / 1.0, int(y[1]) / 1.0))
        else:
            listOfPoints_x.extend((int(x[1]) / 1.0, int(x[0]) / 1.0))
            listOfPoints_y.extend((int(y[1]) / 1.0, int(y[0]) / 1.0))

        line = line[4:]

    polygon_vertices = [
        [listOfPoints_y[0], listOfPoints_x[0]],
        [listOfPoints_y[1], listOfPoints_x[1]],
        [listOfPoints_y[2], listOfPoints_x[2]],
        [listOfPoints_y[3], listOfPoints_x[3]]
    ]

    return {'mask': load_mask(polygon_vertices)}

def load_pipeline_image(df_partitioned):
    """Carrega as imagens do pipeline a partir de um dataframe particionado.

    Args:
        df_partitioned (DataFrame): O dataframe particionado contendo as informações das imagens.

    Returns:
        list: Uma lista contendo as informações das imagens no formato adequado para o pipeline.
    """

    pipeline_dataset = []

    for df_index, df_row in df_partitioned.iterrows():
        row = list(df_row)

        polygon_info = getPolygonPoints(row)

        if polygon_info == False:
            continue
        
        mask = polygon_info['mask']
        y, x = np.where(mask == 1)
        bbox = [np.min(x), np.min(y), np.subtract(np.max(x), np.min(x)), np.subtract(np.max(y), np.min(y))]

        obj = {
            "bbox": bbox,
            "bbox_mode": BoxMode.XYXY_ABS,
            "segmentation": coco_mask.encode(np.asarray(mask, order="F")),
            "category_id": 0
        }

        objs = [obj]

        image_name = df_row.image_name
        image_path = f"/content/all-images/{image_name}.png"

        image_info = {
            'file_name': image_path,
            'image_id': image_name,
            'height': HEIGHT,
            'width': WIDTH,
            'annotations': objs
        }

        pipeline_dataset.append(image_info)

    return pipeline_dataset


def load_pipeline_dataset(dataframe_annotation):
    """Carrega o dataset do pipeline a partir de um dataframe de anotações.

    Args:
        dataframe_annotation (DataFrame): O dataframe contendo as anotações das imagens.

    Returns:
        list: Uma lista contendo as informações do dataset no formato adequado para o pipeline.
    """

    meta = {"frame_id": np.int64, "x1": np.int64, "y1": np.int64, "x2": np.int64,
            "y2": np.int64, "x3": np.int64, "y3": np.int64, "x4": np.int64, "y4": np.int64,
            "image_name": object}

    dask_dataframe = dd.from_pandas(dataframe_annotation, npartitions=8)
    result = dask_dataframe.map_partitions(load_pipeline_image, meta=meta).compute()

    final_result = list(itertools.chain.from_iterable(result))

    return final_result
