# -*- coding:utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

sys.path.append("../../")

from alpharotate.libs.models.detectors.ridet import build_whole_network_arbitrary_shaped
from tools.test_total_text_base_arbitrary_shaped import TestTotalText
from configs import cfgs
from alpharotate.libs.val_libs.voc_eval_r import EVAL


class TestTotalTextRIDet(TestTotalText):

    def eval(self):
        ridet = build_whole_network_arbitrary_shaped.DetectionNetworkRIDet(cfgs=self.cfgs,
                                                                           is_training=False)

        all_boxes_r = self.eval_with_plac(img_dir=self.args.img_dir, det_net=ridet,
                                          image_ext=self.args.image_ext)

        # with open(cfgs.VERSION + '_detections_r.pkl', 'rb') as f2:
        #     all_boxes_r = pickle.load(f2)
        #
        #     print(len(all_boxes_r))

        imgs = os.listdir(self.args.img_dir)
        real_test_imgname_list = [i.split(self.args.image_ext)[0] for i in imgs]

        print(10 * "**")
        print('rotation eval:')
        evaler = EVAL(self.cfgs)
        evaler.voc_evaluate_detections(all_boxes=all_boxes_r,
                                       test_imgid_list=real_test_imgname_list,
                                       test_annotation_path=self.args.test_annotation_path)


if __name__ == '__main__':

    tester = TestTotalTextRIDet(cfgs)
    tester.eval()
