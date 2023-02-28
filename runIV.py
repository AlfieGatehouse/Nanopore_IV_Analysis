#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:30:18 2023

@author: alfiegatehouse
"""

import IV as IV
import pandas as pd
import matplotlib.pyplot as plt
import rectification as rect
import xlinktime as xlt

# Insert sample details
Filename = "20220120_PVAamine_4%meth_13wt%_7200RCF_30m_12ml_0.1MKCl_ph7.95.xlsx" # insert filename here

data = pd.read_excel(Filename)

# Plot individual IVs
plt.figure(1,figsize = (3.1,2.3)) # set figsize
IV.IVall(data)
plt.savefig((Filename) +'.pdf', format = 'pdf',bbox_inches = 'tight')      # save figure

# plot average IVs
plt.figure(2,figsize = (3.1,2.3)) # set figsize
IV.avgIVplot(data)
plt.savefig((Filename) +'2.pdf', format = 'pdf',bbox_inches = 'tight') # save figure

# rectification data
rect.rectification(data)

# time from xlinking data
xlt.xlinktimes(data,1243) #insert crosslinking time

