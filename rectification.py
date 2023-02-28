#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:22:38 2023

@author: alfiegatehouse
"""
import numpy as np

def rectification(df):
    pipettes = []
    values = []
    end = df.shape[1]
    for i in range (1,end):
        pipettes.append(df.columns[i])
        if df.iloc[10,0]==0:
            values.append(df.iat[2,i]/(df.iat[18,i]*-1))
        elif df.iloc[5,0]==0:
            values.append(df.iat[1,i]/(df.iat[9,i]*-1))
        else:
            raise ValueError('Unrecognised format')
    rectification_mean = np.mean(values)
    rectification_std = np.std(values)
    rectification_all = np.column_stack((pipettes, values))
    return(print(rectification_all, rectification_mean,rectification_std))