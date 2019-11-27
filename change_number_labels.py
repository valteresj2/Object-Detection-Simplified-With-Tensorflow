#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:43:06 2019

@author: valteresj
"""

import argparse
import os

CWD_PATH = os.getcwd()


parser = argparse.ArgumentParser(description='Applyied change number labels in config model.')
parser.add_argument('--file_label_name',dest='file_label', type=str,
help='directory of files train',default='/conf_model/labelmap.pbtxt')
parser.add_argument('--file_conf_model',dest='conf_model', type=str,
help='directory of files test',default='/conf_model/model_conf.config')
args = parser.parse_args()



def change_number_labels(conf,label):
    reader = open(conf)
    labels = open(label)
    cont=0
    
    for i in labels:
        if i.rfind('name:')>0:
            cont+=1

    get_train_index=-1
    L=[]   
    for index,i in enumerate(reader):
        if i.rfind('num_classes:')>0:
            j=i.replace(i[(i.rfind(':')+1):len(i)],' '+str(cont)+'\n')
            L.append(j)
        elif i.rfind('fine_tune_checkpoint:')>0:
            j=i.replace(i[(i.rfind(':')+1):len(i)]," 'fine_tune_checkpoint/model.ckpt'"+'\n')
            L.append(j)
        elif i.rfind('fine_tune_checkpoint:')>0:
            get_train_index=0
        elif get_train_index==0 and i.rfind('input_path:')>0:
            j=i.replace(i[(i.rfind(':')+1):len(i)]," 'datatfrecord/train.record'"+'\n')
            L.append(j)
            get_train_index=-1
        elif get_train_index==-1 and i.rfind('input_path:')>0:
            j=i.replace(i[(i.rfind(':')+1):len(i)]," 'datatfrecord/test.record'"+'\n')
            L.append(j)
        elif i.rfind('label_map_path:')>0:
            j=i.replace(i[(i.rfind(':')+1):len(i)]," 'conf_model/labelmap.pbtxt'"+'\n')
            L.append(j)
        else:
            L.append(i)
    file1 = open(conf,"w")
    file1.writelines(L) 
    file1.close()
    
change_number_labels(conf=CWD_PATH+args.conf_model,label=CWD_PATH+args.file_label)


