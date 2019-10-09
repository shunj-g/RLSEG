#!/usr/bin/env python
# encoding: utf-8
'''
@author: shunj-g
@license: (C) Copyright 2018-2035, Digital Imaging and Intelligent Computing Laboratory(DIIC LAB).SHMTU
@contact: shunjieg@gmail.com
@software: extract_file_index
@file: extract_file_index.py
@time: 2019/9/29 15:54
@desc:  

'''
import os
#from config import *


file_name = "ade20k"
file_root = "E:\\shunj-g\\Reinforce_segmentation\\dataset\\data\\ADEChallengeData2016\\"+file_name


def data_list_store(data_path,label_path):
    """
    :param root_path:
    :return: data_file_paths
    """
    # TODO this can walk all file director and save all directors
    data_file_train_paths = []
    for roots, dirs, files in os.walk(data_path):
        for file in files:
            if ".jpg" in file:
                data_file_path = os.path.join(roots, file)
                data_file_train_paths.append(data_file_path)
    data_file_label_paths = []
    for roots, dirs, files in os.walk(label_path):
        for file in files:
            if ".png" in file:
                data_file_path = os.path.join(roots, file)
                data_file_label_paths.append(data_file_path)
    return data_file_train_paths, data_file_label_paths

train_path = os.path.join(file_root, 'images\\training')
train_label_path = os.path.join(file_root, 'annotations_instance\\training')
validation_path = os.path.join(file_root, 'images\\validation')
validation_label_path = os.path.join(file_root, 'annotations_instance\\validation')
file_train = open(file_name+"_train_list.txt","w")
file_valid = open(file_name+"_validation_list.txt", "w")
data_file_train_paths,data_file_label_paths = data_list_store(train_path,train_label_path)#D:/data/yizhou/ade20k/ADE20K_2016_07_26
for train_path,label_path in zip(data_file_train_paths,data_file_label_paths):
    file_train.write(train_path+" "+label_path+'\n')

data_file_valid_paths, data_file_label_paths = data_list_store(validation_path,validation_label_path)  # D:/data/yizhou/ade20k/ADE20K_2016_07_26
for valid_path, label_path in zip(data_file_valid_paths, data_file_label_paths):
    file_valid.write(valid_path + " " + label_path + '\n')
file_train.close()
file_valid.close()