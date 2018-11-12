#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 19:45:56 2018

@author: wwt
"""
import collections
import cv2
import numpy as np

def get_data(input_path):
    '''
    get all_images, classes_count, class_mapping
    all_images: dict in dict, 
                every dict obtain one image info
                how many object and how many classes  
    class_count: dict, key is class's name, value is class's num
    class_mapping: every class's lag
    if we find 'bg', we will set 'bg' in the last of class_mapping
    '''
    found_bg = False
    all_imgs = {}
    classes_count = collections.defaultdict(lambda:0)
    class_mapping = {}
    
    with open(input_path,'r') as f:
        print('open {0} get some info'.format(input_path))
        for line in f:
            line_split = line.strip().split(',')
            [filename, x1, y1, x2, y2, class_name] = line_split
            
            classes_count[class_name]+=1
            
            if class_name == 'bg' and not found_bg:
                print('find special class:bg')
                found_bg = True
            
            if class_name not in class_mapping and class_name != 'bg':
                class_mapping[class_name]=len(class_mapping)
            
            if filename not in all_imgs:
                all_imgs[filename] = {}
                img = cv2.imread(filename)
                (rows, cols) = img.shape[:2]
                
                all_imgs[filename]['filepath'] = filename
                all_imgs[filename]['width'] = cols
                all_imgs[filename]['height'] = rows
                all_imgs[filename]['bboxes'] = []
                
                if np.random.randint(0, 6) > 0:
                    all_imgs[filename]['imageset'] = 'trainval'
                else:
                    all_imgs[filename]['imageset'] = 'test'
                
            all_imgs[filename]['bboxes'].append(
                    {'class': class_name, 'x1': int(float(x1)), 'x2': int(float(x2)), 'y1': int(float(y1)),
                 'y2': int(float(y2))})
        all_data = []
        for key in all_imgs:
            all_data.append(all_imgs[key])
        if found_bg:
            class_mapping['bg']=len(class_mapping)
            
    return all_data, classes_count, class_mapping
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                