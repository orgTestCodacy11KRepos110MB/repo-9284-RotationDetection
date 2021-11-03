# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

import numpy as np

from alpharotate.utils.pretrain_zoo import PretrainModelZoo
from configs._base_.models.retinanet_r50_fpn import *
from configs._base_.datasets.dota_detection import *
from configs._base_.schedules.schedule_1x import *

# schedule
BATCH_SIZE = 1
GPU_GROUP = "0,1,2"
NUM_GPU = len(GPU_GROUP.strip().split(','))
LR = 1e-3
SAVE_WEIGHTS_INTE = 11725 * 2
DECAY_EPOCH = [8, 11, 20]
MAX_EPOCH = 12
WARM_EPOCH = 1 / 16.
DECAY_STEP = np.array(DECAY_EPOCH, np.int32) * SAVE_WEIGHTS_INTE
MAX_ITERATION = SAVE_WEIGHTS_INTE * MAX_EPOCH
WARM_SETP = int(WARM_EPOCH * SAVE_WEIGHTS_INTE)

# dataset
DATASET_NAME = 'DIOR-R'
CLASS_NUM = 20

# model
# backbone
pretrain_zoo = PretrainModelZoo()
PRETRAINED_CKPT = pretrain_zoo.pretrain_weight_path(NET_NAME, ROOT_PATH)
TRAINED_CKPT = os.path.join(ROOT_PATH, 'output/trained_weights')

# bbox head
NUM_SUBNET_CONV = 4
LEVEL = ['P3', 'P4', 'P5', 'P6', 'P7']
BASE_ANCHOR_SIZE_LIST = [32, 64, 128, 256, 512]
ANCHOR_STRIDE = [8, 16, 32, 64, 128]
ANCHOR_SCALES = [2 ** 0, 2 ** (1.0 / 3.0), 2 ** (2.0 / 3.0)]
ANCHOR_RATIOS = [1, 1 / 2, 2.]

# loss
CLS_WEIGHT = 1.0
REG_WEIGHT = 0.01

VERSION = 'RetinaNet_DIOR_R_RIDet_2x_20211028'

"""
RIDet-8p
FLOPs: 662228714;    Trainable params: 32615676

cls : airplane|| Recall: 0.5924257184607891 || Precison: 0.26707290294246816|| AP: 0.5002738571237081
F1:0.5894261737114739 P:0.7718848580441641 R:0.4767413541159279
cls : airport|| Recall: 0.6831831831831832 || Precison: 0.025765898408743416|| AP: 0.3492807491130282
F1:0.46066007689422467 P:0.5008818342151675 R:0.4264264264264264
cls : baseballfield|| Recall: 0.7766453115899825 || Precison: 0.22734634728497144|| AP: 0.6678614360031092
F1:0.7247241284745414 P:0.9071803852889667 R:0.6033779848573093
cls : basketballcourt|| Recall: 0.902143522833178 || Precison: 0.0876255997103286|| AP: 0.804445327630726
F1:0.8489443388210348 P:0.9041600842548709 R:0.8000931966449207
cls : bridge|| Recall: 0.4063344920818849 || Precison: 0.02271794761051245|| AP: 0.22734632639077845
F1:0.295567130745561 P:0.44324324324324327 R:0.22170722286597142
cls : chimney|| Recall: 0.7546071774975752 || Precison: 0.03247349528341264|| AP: 0.7218983417304267
F1:0.8093336282913465 P:0.9479166666666666 R:0.7061105722599418
cls : dam|| Recall: 0.6654275092936803 || Precison: 0.012178527690842291|| AP: 0.2504548421432902
F1:0.34229867746713555 P:0.40664961636828645 R:0.2955390334572491
cls : Expressway-Service-area|| Recall: 0.847926267281106 || Precison: 0.03169790518191841|| AP: 0.6134651261912427
F1:0.6493176484082969 P:0.7881578947368421 R:0.552073732718894
cls : Expressway-toll-station|| Recall: 0.6104651162790697 || Precison: 0.02270515731430425|| AP: 0.48830425159952007
F1:0.5800737158538265 P:0.8839285714285714 R:0.4316860465116279
cls : golffield|| Recall: 0.84 || Precison: 0.03812154696132597|| AP: 0.6865350087767846
F1:0.7364054175202907 P:0.8975 R:0.6243478260869565
cls : groundtrackfield|| Recall: 0.9320954907161804 || Precison: 0.06706106870229007|| AP: 0.7324568901049738
F1:0.737245844246831 P:0.7199191102123357 R:0.7554376657824934
cls : harbor|| Recall: 0.5694041867954911 || Precison: 0.02134260432887891|| AP: 0.2770247414655502
F1:0.35861581375638696 P:0.42566371681415927 R:0.3098228663446055
cls : overpass|| Recall: 0.6083052749719416 || Precison: 0.035234844791158786|| AP: 0.41150768444344066
F1:0.488956162479061 P:0.5801232665639445 R:0.4225589225589226
cls : ship|| Recall: 0.6804695049167282 || Precison: 0.2803433014073953|| AP: 0.5649216146654359
F1:0.643058559191818 P:0.7439420527946832 R:0.5662763599158757
cls : stadium|| Recall: 0.8779761904761905 || Precison: 0.0613879929247737|| AP: 0.6312378540458232
F1:0.6236342015012892 P:0.6530944625407166 R:0.5967261904761905
cls : storagetank|| Recall: 0.47485124780617266 || Precison: 0.3220963995354239|| AP: 0.42294217888603775
F1:0.5333326258028573 P:0.7868893528183716 R:0.40336458199563374
cls : tenniscourt|| Recall: 0.8756638975895411 || Precison: 0.24420812761109|| AP: 0.754055708988889
F1:0.7806128240476375 P:0.7835093977225956 R:0.777747514639793
cls : trainstation|| Recall: 0.6699410609037328 || Precison: 0.013442131819615264|| AP: 0.3392711322466596
F1:0.4079063349966398 P:0.55 R:0.3241650294695481
cls : vehicle|| Recall: 0.2936936936936937 || Precison: 0.08756183271034312|| AP: 0.2449312003984481
F1:0.3326621703781149 P:0.5951228952970776 R:0.23085585585585586
cls : windmill|| Recall: 0.6647765176784523 || Precison: 0.11707689596428361|| AP: 0.5147766586832698
F1:0.5987063352345617 P:0.7220913801224682 R:0.5113408939292862
mAP is : 0.510149546531557
"""