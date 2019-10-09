#!/usr/bin/env python
# encoding: utf-8
'''
@author: shunj-g
@license: (C) Copyright 2018-2035, Digital Imaging and Intelligent Computing Laboratory(DIIC LAB).SHMTU
@contact: shunjieg@gmail.com
@software: dataset
@file: dataset.py
@time: 2019/10/9 13:40
@desc:
'''

from abc import ABCMeta, abstractmethod


class Dataset(object):
    def __init__(self):
        __metaclass__ = ABCMeta

    @abstractmethod
    def __getitem__(self, item):
        '''
        needs to return a data_dict for the sample at the position item
        :param item:
        :return:
        '''
        pass

    @abstractmethod
    def __len__(self):
        '''
        returns how many items the dataset has
        :return:
        '''
        pass



