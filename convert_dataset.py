# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 10:45:22 2022

@author: eric1
"""
import numpy as np
from build_directories import check_if_exists
from build_directories import create_dir
from build_directories import transfer_data_from_hpf5
# CAMGIAN_DATASET_ROOT
data_path='C:/Users/eric1/testing_dataset_pull/data/camgian/'

# check for confliciting directories
##### check_if_exists(data_path)
# create new directories on local machine
##### create_dir(data_path)
# pull data from hpf5 dataset
transfer_data_from_hpf5('16-lineTrain.hdf5', data_path)

