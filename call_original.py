from original import voc_eval


detpath = 'Main/comp4_bd2bb618-4fbd-4605-a58e-e9144f021829_det_test_aeroplane.txt'
annopath = 'Annotations/{:s}.xml'
imagesetfile = 'Main/test.txt'
cachedir = 'annotations_cache'
rec, prec, ap = voc_eval(detpath, annopath, imagesetfile, 'aeroplane', cachedir, use_07_metric=True)
print ap
