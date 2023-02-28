# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def IVall(df):
    m =[]
    b = []
    end = df.shape[1]
    pipettes=[]
    for i in range(1,end):
        pipettes.append(df.columns[i])
    if df.iloc[10,0]==0:
        for i in range(1,end):
            pipettes.append(df.columns[i])
            fit = np.polyfit(df.iloc[8:13,0],df.iloc[8:13,i],1,cov = True)
            plt.plot(df.iloc[:,0],df.iloc[:,i], label = df.columns[i], marker = 'o', linestyle = 'None')
            plt.legend()
            m.append(fit[0][0])
            b.append(fit[0][1])    
        for i in range(0,end-1):
            plt.plot(df.iloc[8:13,0], m[i]*df.iloc[8:13,0]+b[i], marker='None',  linestyle='--')
    elif df.iloc[5,0]==0:
        for i in range(1,end):
            fit = np.polyfit(df.iloc[4:7,0],df.iloc[4:7,i],1,cov = True)
            plt.plot(df.iloc[:,0],df.iloc[:,i], label = df.columns[i], marker = 'o', linestyle = 'None')
            plt.legend()
            m.append(fit[0][0])
            b.append(fit[0][1])    
        for i in range(0,end-1):
            plt.plot(df.iloc[4:7,0], m[i]*df.iloc[4:7,0]+b[i], marker='None',  linestyle='--')
    else:
        raise ValueError('Unrecognised format') 
    
    fit_data = np.column_stack((pipettes,m,b))
    G_avg = np.mean(m)
    G_std = np.std(m)
    plt.xlabel('Voltage') 
    plt.ylabel('Current')
    return(plt.show(),print(fit_data,G_avg,G_std))

def avgIVplot(df):
    end = df.shape[1]
    df_avg = df.copy()
    df_avg['mean']= np.mean(df.iloc[:,1:end],axis = 1)
    df_avg['std'] = np.std(df.iloc[:,1:end],axis = 1)
    plt.errorbar(df_avg.iloc[:,0],df_avg.iloc[:,-2],yerr = df_avg.iloc[:,-1], marker = 'o')
    plt.xlabel('Voltage')
    plt.ylabel('Current')
    return(plt.show(),print(df_avg))
