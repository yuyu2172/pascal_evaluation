# THIS NO LONGER WORKS


# Evaluation of PASCAL VOC Detection task

This repository contains scripts to evaluate results produced by FasterRCNN implementation found at https://github.com/rbgirshick/py-faster-rcnn

This repository is created to verify the implementation of the evaluation code that is added to ChainerCV.

https://github.com/pfnet/chainercv/pull/130

# Directory structure

```
Annotations:  Annotations for PASCAL VOC 2007 detection tasks.
ImageSets:  There is a text file that contains a list of file ids to look for.
Main: A text file that contains coordinates of predicted bounding boxes.
annotations_cache:  cached annotations
```



# Evaluation results 

Results obtained by an evaluation code found at https://github.com/rbgirshick/py-faster-rcnn

```

$ python call_original.py            

('aeroplane', 0.67864799899108375)
('bicycle', 0.78249248815967498)
('bird', 0.66738567468225019)
('boat', 0.57644292759350124)
('bottle', 0.53114680537511683)
('bus', 0.75064712123804667)
('car', 0.80075418356341355)
('cat', 0.79762902216703579)
('chair', 0.4862165954344429)
('cow', 0.75566041480592216)
('diningtable', 0.69407412826839654)
('dog', 0.77598916966042197)
('horse', 0.81021121169305221)
('motorbike', 0.76208130419903619)
('person', 0.77090192776181299)
('pottedplant', 0.42651221567191583)
('sheep', 0.67961571534614706)
('sofa', 0.65458208497403625)
('train', 0.75503256331244883)
('tvmonitor', 0.71334268761681385)
>>>>>>>>>>>>>>>>>>>>>>>>>
('map ', 0.69346831202572845)

```



Results obtained from the reimplemented code.


```

$ pyhton parse_results.py

('aeroplane', 0.67864799899108375)
('bicycle', 0.78249248815967498)
('bird', 0.66738567468225019)
('boat', 0.57644292759350124)
('bottle', 0.53114680537511683)
('bus', 0.75064712123804667)
('car', 0.80075418356341355)
('cat', 0.79762902216703579)
('chair', 0.4862165954344429)
('cow', 0.75566041480592216)
('diningtable', 0.69407412826839654)
('dog', 0.77598916966042197)
('horse', 0.81021121169305221)
('motorbike', 0.76208130419903619)
('person', 0.77090192776181299)
('pottedplant', 0.42651221567191583)
('sheep', 0.67961571534614706)
('sofa', 0.65458208497403625)
('train', 0.75503256331244883)
('tvmonitor', 0.71334268761681385)
>>>>>>>>>>>>>>>>>>>>>>>>>>>
0.693468312026

```
