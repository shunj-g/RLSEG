#!/usr/bin/env python
# encoding: utf-8
'''
@author: shunj-g
@license: (C) Copyright 2018-2035, Digital Imaging and Intelligent Computing Laboratory(DIIC LAB).SHMTU
@contact: shunjieg@gmail.com
@software: single_threaded_augmenter
@file: single_threaded_augmenter.py
@time: 2019/10/9 13:40
@desc:
'''

from __future__ import print_function

from future import standard_library

standard_library.install_aliases()
from builtins import object


class SingleThreadedAugmenter(object):
    """
    Use this for debugging custom transforms. It does not use a background thread and you can therefore easily debug
    into your augmentations. This should not be used for training. If you want a generator that uses (a) background
    process(es), use MultiThreadedAugmenter.
    Args:
        data_loader (generator or DataLoaderBase instance): Your data loader. Must have a .next() function and return
        a dict that complies with our data structure

        transform (Transform instance): Any of our transformations. If you want to use multiple transformations then
        use our Compose transform! Can be None (in that case no transform will be applied)
    """
    def __init__(self, data_loader, transform):
        self.data_loader = data_loader
        self.transform = transform

    def __iter__(self):
        return self


    def __next__(self):
        item = next(self.data_loader)
        if self.transform is not None:
            item = self.transform(**item)
        return item
