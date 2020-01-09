#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 16:13:19 2018

@author: duocao
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import scipy.io as sio
import math
import h5py
from sklearn import preprocessing

file_name = "build_frequency.xlsx"
import pandas as pd
df = pd.read_excel(file_name)

feature_columns = df.columns[1:-1]
X = df[feature_columns]
y = df['TF']
from sklearn.cross_validation import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)