# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

import numpy as np

from alpharotate.utils.pretrain_zoo import PretrainModelZoo
from configs._base_.models.retinanet_r50_fpn import *
from configs._base_.datasets.dota_detection import *
from configs._base_.schedules.schedule_1x import *

# schedule
BATCH_SIZE = 1  # r3det only support 1
GPU_GROUP = '0,1,2'
NUM_GPU = len(GPU_GROUP.strip().split(','))
LR = 1e-3
SAVE_WEIGHTS_INTE = 10000 * 2
DECAY_STEP = np.array(DECAY_EPOCH, np.int32) * SAVE_WEIGHTS_INTE
MAX_ITERATION = SAVE_WEIGHTS_INTE * MAX_EPOCH
WARM_SETP = int(WARM_EPOCH * SAVE_WEIGHTS_INTE)

# dataset
DATASET_NAME = 'HRSC2016'
IMG_SHORT_SIDE_LEN = [800, 400, 600, 1000, 1200]
IMG_MAX_LENGTH = 1200
CLASS_NUM = 1

# data augmentation
IMG_ROTATE = True
RGB2GRAY = True
VERTICAL_FLIP = True
HORIZONTAL_FLIP = True
IMAGE_PYRAMID = True

# model
NET_NAME = 'resnet101_v1d'
pretrain_zoo = PretrainModelZoo()
PRETRAINED_CKPT = pretrain_zoo.pretrain_weight_path(NET_NAME, ROOT_PATH)
TRAINED_CKPT = os.path.join(ROOT_PATH, 'output/trained_weights')

# bbox head
NUM_REFINE_STAGE = 1

# sample
REFINE_IOU_POSITIVE_THRESHOLD = [0.6, 0.7]
REFINE_IOU_NEGATIVE_THRESHOLD = [0.5, 0.6]

# loss
CLS_WEIGHT = 1.0
REG_WEIGHT = 2.0

KL_TAU = 2.0
KL_FUNC = 0   # 0: sqrt  1: log

VERSION = 'RetinaNet_HRSC2016_R3Det_KL_2x_20211013'

"""
r3det + kl + sqrt tau=2
FLOPs: 1461050966;    Trainable params: 55999620

07 metric
cls : ship|| Recall: 0.988599348534202 || Precison: 0.1913016073116924|| AP: 0.8986931420249472
F1:0.9468035107852405 P:0.9514802631578947 R:0.9421824104234527
mAP is : 0.8986931420249472

12 metric
cls : ship|| Recall: 0.996742671009772 || Precison: 0.09938291653134135|| AP: 0.9762299419922914
F1:0.9545962271212568 P:0.9589153656532456 R:0.9503257328990228
mAP is : 0.9762299419922914
"""

