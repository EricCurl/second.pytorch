# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 10:38:18 2022

@author: eric1
"""

import os
import sys
import h5py
import numpy as np

def check_if_exists(__path):
    if os.path.isdir(__path+'training/'):
        sys.exit('ERROR: dataset already exists in this directory\nchange dataset location')
    if os.path.isdir(__path+'testing/'):
        sys.exit('ERROR: dataset already exists in this directory\nchange dataset location')

def create_dir(__path):
    os.mkdir(__path+"training")
    os.mkdir(__path+"training/velodyne")
    os.mkdir(__path+"training/velodyne_reduced")
    os.mkdir(__path+"training/label_2")
    os.mkdir(__path+"training/calib")
    os.mkdir(__path+"training/image_2")
    os.mkdir(__path+"testing")
    os.mkdir(__path+"testing/velodyne")
    os.mkdir(__path+"testing/velodyne_reduced")
    os.mkdir(__path+"testing/calib")
    os.mkdir(__path+"testing/image_2")
    
def transfer_data_from_hpf5(file_name,__path):
    dataset=h5py.File('16-lineTrain.hdf5','r+')
    raw_data =dataset['/training_data']
    num_scans=raw_data.shape[0]
    num_lines_per_scan=raw_data.shape[1]
    num_points_per_line=raw_data.shape[2]
    num_dimensions=raw_data.shape[3]
    for i in range(num_scans):
        v_points=np.zeros((1,4),dtype=np.float32)
        for j in range(num_lines_per_scan):
            for k in range(num_points_per_line):
                point=np.array(raw_data[i,j,k,...])
                v_points=np.vstack((v_points, point))
        scan_id=str(i).zfill(6)+'.bin'
        scan_id_dir=os.path.join(__path+'training/velodyne/',scan_id)
        f=open(scan_id_dir,"w")
        v_points=np.delete(v_points, (0),axis=0)
        v_points.tofile(f)
        f.close()
    dataset.close()
