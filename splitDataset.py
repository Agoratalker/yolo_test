import os
import random
#按比例划分数据集
#涉及路径的一定要改成自己的
trainval_percent = 0.9
train_percent = 0.9
xmlfilepath = 'D:/yolov8/ultralytics-main/ultralytics/data/datasets/Annotations'
txtsavepath = 'D:/yolov8/ultralytics-main/ultralytics/data/datasets/ImageSets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('D:/yolov8/ultralytics-main/ultralytics/data/datasets/ImageSets/trainval.txt', 'w')
ftest = open('D:/yolov8/ultralytics-main/ultralytics/data/datasets/ImageSets/test.txt', 'w')
ftrain = open('D:/yolov8/ultralytics-main/ultralytics/data/datasets/ImageSets/train.txt', 'w')
fval = open('D:/yolov8/ultralytics-main/ultralytics/data/datasets/ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()