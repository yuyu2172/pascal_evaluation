from original import voc_eval
from chainercv.datasets.pascal_voc.voc_utils import voc_detection_label_names
import numpy as np

labels = voc_detection_label_names[1:]

aps = []
for label in labels:
    detpath = 'Main/comp4_bd2bb618-4fbd-4605-a58e-e9144f021829_det_test_{}.txt'.format(label)
    annopath = 'Annotations/{:s}.xml'
    imagesetfile = 'Main/test.txt'
    cachedir = 'annotations_cache'
    rec, prec, ap = voc_eval(detpath, annopath, imagesetfile, label, cachedir, use_07_metric=True)
    print(label, ap)
    aps.append(ap)
print('>>>>>>>>>>>>>>>>>>>>>>>>>')
print('map ', np.mean(aps))

