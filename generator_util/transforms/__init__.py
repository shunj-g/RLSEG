#!/usr/bin/env python
# encoding: utf-8
'''
@author: shunj-g
@license: (C) Copyright 2018-2035, Digital Imaging and Intelligent Computing Laboratory(DIIC LAB).SHMTU
@contact: shunjieg@gmail.com
@software: __init__
@file: __init__.py
@time: 2019/10/9 13:40
@desc:
'''

from .abstract_transforms import AbstractTransform, Compose, RndTransform
from .channel_selection_transforms import DataChannelSelectionTransform, SegChannelSelectionTransform, \
    SegChannelMergeTransform, SegChannelRandomSwapTransform, SegChannelRandomDuplicateTransform, SegLabelSelectionBinarizeTransform
from .color_transforms import BrightnessMultiplicativeTransform, BrightnessTransform, ContrastAugmentationTransform, \
    FancyColorTransform, GammaTransform, IlluminationTransform
from .crop_and_pad_transforms import CenterCropSegTransform, CenterCropTransform, PadTransform, RandomCropTransform
from .noise_transforms import GaussianBlurTransform, GaussianNoiseTransform
from .sample_normalization_transforms import CutOffOutliersTransform, RangeTransform, ZeroMeanUnitVarianceTransform

from .utility_transforms import ConvertSegToOnehotTransform, ListToTensor, NumpyToTensor, RenameTransform, \
    ConvertMultiSegToOnehotTransform, ConvertSegToArgmaxTransform, ConvertMultiSegToArgmaxTransform
from .spatial_transforms import ChannelTranslation, MirrorTransform, SpatialTransform, ZoomTransform, TransposeAxesTransform
from .resample_transforms import SimulateLowResolutionTransform

transform_list = [
    AbstractTransform, Compose, RndTransform, DataChannelSelectionTransform,
    SegChannelSelectionTransform, BrightnessMultiplicativeTransform, BrightnessTransform,
    ContrastAugmentationTransform, FancyColorTransform, GammaTransform, IlluminationTransform,
    CenterCropSegTransform, CenterCropTransform, PadTransform, RandomCropTransform,
    GaussianNoiseTransform, GaussianBlurTransform, CutOffOutliersTransform, RangeTransform,
    ZeroMeanUnitVarianceTransform, ChannelTranslation, MirrorTransform, SpatialTransform, ZoomTransform,
    ConvertSegToOnehotTransform, ListToTensor, NumpyToTensor
]
