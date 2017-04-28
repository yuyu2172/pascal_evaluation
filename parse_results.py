import re
import numpy as np
import os
import pickle
from chainercv.datasets.pascal_voc.voc_utils import pascal_voc_labels  

from chainercv.evaluations import eval_detection


def read_pascal_predictions(base_dir):
    d = {}

    for fn in os.listdir(base_dir):
        for label in pascal_voc_labels:
            r = re.match('\S+_test_{}.txt'.format(label), fn)
            if r is not None:
                d[label] = os.path.join(base_dir, fn)

    img_ids_list = []
    bboxes_list = []

    bboxes = {}
    labels = {}
    confs = {}
    for label, fn in d.items():
        for l in open(fn):
            split = l.split()
            img_id = split[0]
            conf = float(split[1])
            bbox = np.array([
                float(split[2]), float(split[3]),
                float(split[4]), float(split[5])])
            if img_id not in bboxes:
                bboxes[img_id] = []
                labels[img_id] = []
                confs[img_id] = []
            bboxes[img_id].append(bbox)
            labels[img_id].append(pascal_voc_labels.index(label))
            confs[img_id].append(conf)

    
    ids = bboxes.keys()
    bboxes = [np.array(bboxes[id_]) for id_ in ids]
    labels = [np.array(labels[id_]) for id_ in ids]
    confs = [np.array(confs[id_]) for id_ in ids]
    return ids, bboxes, labels, confs


def read_gt_annos(fn, ids):
    with open(fn, 'rb') as f:
        annots = pickle.load(f)

    # print annots
    gt_bboxes = [[] for _ in range(len(ids))]
    gt_labels = [[] for _ in range(len(ids))]
    gt_difficults = [[] for _ in range(len(ids))]
    for i, id_ in enumerate(ids):
        anno = annots[id_]
        for anno_elem in anno:
            gt_bboxes[i].append(anno_elem['bbox'])
            gt_labels[i].append(pascal_voc_labels.index(anno_elem['name']))
            gt_difficults[i].append(anno_elem['difficult'])
        gt_bboxes[i] = np.array(gt_bboxes[i])
        gt_labels[i] = np.array(gt_labels[i])
        gt_difficults[i] = np.array(gt_difficults[i], dtype=np.bool)
    return gt_bboxes, gt_labels, gt_difficults


if __name__ == '__main__':
    base_dir = 'Main'
    ids, bboxes, labels, confs = read_pascal_predictions(base_dir)

    anno_fn = 'annots.pkl'
    gt_bboxes, gt_labels, gt_difficults = read_gt_annos(anno_fn, ids)

    metric = eval_detection(bboxes, labels, confs, gt_bboxes, gt_labels, len(pascal_voc_labels), gt_difficults,
                            use_07_metric=True)
    print metric['map']
