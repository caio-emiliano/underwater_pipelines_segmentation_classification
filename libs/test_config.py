from detectron2.config import get_cfg
from fvcore.common.config import CfgNode as CN
import os

#Test CONFIGS
cfg = get_cfg()

#Obtendo os pesos pré-treinados e usando transfer learning
cfg.merge_from_file("./detectron2/configs/COCO-InstanceSegmentation/mask_rcnn_R_101_C4_3x.yaml")
cfg.MODEL.WEIGHTS = "detectron2://ImageNetPretrained/MSRA/R-101.pkl"

cfg.DATASETS.TEST = ("pipeline_test_dataset",)

cfg.DATALOADER.NUM_WORKERS = 2
cfg.TEST.EVAL_PERIOD = 200

#Serão definidos no notebook de inference
cfg.MODEL.WEIGHTS = ""
cfg.OUTPUT_DIR = ""

# ---------------------------------------------------------------------------- #
# DATALOADER
# ---------------------------------------------------------------------------- #
#Essa config acima é usada para que o detectron retire as imagens sem
#anotações do treinamento (caso existam imagens com anotações vazias).
cfg.DATALOADER.FILTER_EMPTY_ANNOTATIONS = True

# ---------------------------------------------------------------------------- #
# MODEL
# ---------------------------------------------------------------------------- #
# Definir o modo de avaliação como "test"
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1
cfg.MODEL.ROI_HEADS.NMS_THRESH_TEST = 0.3
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7
cfg.MODEL.RPN.POST_NMS_TOPK_TEST = 500
cfg.MODEL.BACKBONE.FREEZE_AT = 2
cfg.MODEL.RPN.POST_NMS_TOPK_TRAIN = 2000
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 128
cfg.MODEL.MASK_ON = True
# ---------------------------------------------------------------------------- #
# INPUT
# ---------------------------------------------------------------------------- #
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