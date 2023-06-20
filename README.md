# Segmentação e Clusterização de Anomalias em Oleodutos Subaquáticos

Este repositório contém o código e os dados utilizados no estudo de segmentação e clusterização de anomalias em oleodutos subaquáticos. O objetivo deste projeto é contribuir para a detecção precisa e eficiente de áreas problemáticas nos oleodutos, permitindo a tomada de medidas preventivas e a manutenção adequada, evitando danos ambientais e prejuízos econômicos.

## Resumo do Projeto

A segmentação e clusterização das imagens de oleodutos subaquáticos foram realizadas utilizando técnicas de visão computacional e algoritmos de aprendizado de máquina. Uma base de dados composta por 34.323 imagens, obtidas por meio de inspeção ROV e anotadas com a posição do oleoduto, foi construída para treinamento e teste dos modelos.

A segmentação das imagens foi realizada utilizando a ferramenta Detectron 2, que possui recursos avançados de detecção e segmentação de objetos. Foram obtidos resultados satisfatórios, com uma precisão média de aproximadamente 93.8% para o conjunto de teste.

Além disso, a clusterização das anomalias nos oleodutos foi conduzida utilizando os algoritmos k-means e fuzzy k-means. Uma avaliação quantitativa do agrupamento de anomalias foi realizada, destacando a eficácia da abordagem proposta no processo de identificação e clusterização das anomalias.

## Estrutura do Repositório

- `docs/`: Documentação adicional, incluindo o trabalho de conclusão de curso relacionado ao projeto.
- `database/`: Pasta contendo as anotações utilizados no estudo, as imagens usadas nesse trabalho são confidenciais e não serão divulgadas.
- `libs`: Pasta contendo os arquivos de configuração da rede Detectron 2 e as funções utilizadas no carregamento da base de dados.
- `notebooks/`: Notebooks Jupyter com os passos de segmentação, extração de características, PCA e clusterização dos dados.

## Requisitos de Instalação

Para reproduzir os resultados deste projeto, é necessário instalar as seguintes dependências:

- Python 3.10 ou superior
- Bibliotecas Python: numpy, keras, tensorflow, scikit-image, pycocotools, pandas, scikit-learn, opencv-python, detectron2

## Como Usar

1. Clone este repositório em sua máquina local.

2. Instale as dependências necessárias executando o comando `pip install -r requirements.txt`.

3. Instale o pycocotools seguindo os passos abaixo
    1. > pip install cython
    2. > pip install numpy
    3. > git clone https://github.com/cocodataset/cocoapi.git
    4. > cd cocoapi/PythonAPI
    5. > python setup.py build_ext install

4. Instale o Detectron 2 (conforme feito nos notebooks "Detectron2_Training.ipynb" e/ou "Detectron2_Inference.ipynb" do projeto)

5. Execute os notebooks Jupyter em `notebooks/` para reproduzir os passos do projeto.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request com melhorias, correções de bugs ou novos recursos.

## Contato

Se você tiver alguma dúvida ou sugestão relacionada a este projeto, entre em contato conosco pelos e-mails: [caio_emiliano@hotmail.com](mailto:caio_emiliano@hotmail.com) [marcusrosa.14@hotmail.com](mailto:marcusrosa.14@hotmail.com)
