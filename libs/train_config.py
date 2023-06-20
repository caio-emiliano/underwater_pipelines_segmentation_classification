from detectron2.config import get_cfg
from fvcore.common.config import CfgNode as CN

#Training CONFIGS
cfg = get_cfg()

#Obtendo os pesos pré-treinados e usando transfer learning
cfg.merge_from_file("./detectron2/configs/COCO-InstanceSegmentation/mask_rcnn_R_101_C4_3x.yaml")
cfg.MODEL.WEIGHTS = "detectron2://ImageNetPretrained/MSRA/R-101.pkl"

cfg.DATASETS.TRAIN = ("pipeline_train_dataset",)
cfg.DATASETS.TEST = ("pipeline_val_dataset",)

cfg.DATALOADER.NUM_WORKERS = 2
cfg.TEST.EVAL_PERIOD = 200

local_output = ""

# ---------------------------------------------------------------------------- #
# BACKBONE
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
# DATALOADER
# ---------------------------------------------------------------------------- #
#Essa config acima é usada para que o detectron retire as imagens sem
#anotações do teste (caso existam imagens com anotações vazias).
cfg.DATALOADER.FILTER_EMPTY_ANNOTATIONS = True
# ---------------------------------------------------------------------------- #
# MODEL
# ---------------------------------------------------------------------------- #
cfg.MODEL.ROI_HEADS.NMS_THRESH_TEST = 0.3
cfg.MODEL.RPN.POSITIVE_FRACTION = 0.33
cfg.MODEL.BACKBONE.FREEZE_AT = 2
cfg.MODEL.RPN.POST_NMS_TOPK_TRAIN = 2000
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 128
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1
cfg.MODEL.MASK_ON = True
# ---------------------------------------------------------------------------- #
# INPUT
# ---------------------------------------------------------------------------- #
cfg.INPUT.MIN_SIZE_TRAIN = 295
cfg.INPUT.MAX_SIZE_TRAIN = 510

#Para usarmos a resolução correta na validação também. 
#O detectron interpreta a validação como "teste" também.
cfg.INPUT.MIN_SIZE_TEST = 295
cfg.INPUT.MAX_SIZE_TEST = 510

cfg.INPUT.MASK_FORMAT = 'bitmask'

# ---------------------------------------------------------------------------- #
# SOLVER
# ---------------------------------------------------------------------------- #
cfg.SOLVER.LR_SCHEDULER_NAME = "WarmupCosineLR"
cfg.SOLVER.WARMUP_ITERS = 500

cfg.SOLVER.GAMMA = 0.1
cfg.SOLVER.STEPS = [1000, 1500]

cfg.SOLVER.MOMENTUM = 0.9
cfg.SOLVER.IMS_PER_BATCH = 2
cfg.SOLVER.BASE_LR = 0.001
cfg.SOLVER.WEIGHT_DECAY = 0
cfg.SOLVER.MAX_ITER = 2000
cfg.SOLVER.CHECKPOINT_PERIOD = 500

cfg.SOLVER.CLIP_GRADIENTS = CN({"ENABLED": True})
cfg.SOLVER.CLIP_GRADIENTS.CLIP_TYPE = "norm"
cfg.SOLVER.CLIP_GRADIENTS.CLIP_VALUE = 5.0
cfg.SOLVER.CLIP_GRADIENTS.NORM_TYPE = 2.0