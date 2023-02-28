#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:25:17 2023

@author: alfiegatehouse
"""

import numpy as np
from datetime import datetime

def xlinktimes(df,time):
    xlink_time = datetime.strptime(str(time), "%H%M")
    end = df.shape[1]
    pipettes = []
    delta_t = []
    for i in range(1,end):
        pipettes.append(df.columns[i])
        try:
            delta_t.append(str(((datetime.strptime(pipettes[i-1][-4:],"%H%M")) - xlink_time)))
        except ValueError:
            delta_t.append(xlink_time)
    time_array = np.c_[pipettes,delta_t]
    return(print(time_array))