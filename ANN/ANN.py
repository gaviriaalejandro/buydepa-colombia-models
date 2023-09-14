import os
import pandas as pd
import math as mt
import numpy as np
import mysql.connector as sql
import unicodedata
import random
import copy
import scipy.optimize 
from datetime import datetime
from dateutil.relativedelta import relativedelta
from scipy.optimize import fmin_bfgs
from sqlalchemy import create_engine 
from tqdm import tqdm

# https://cloudxlab.com/blog/numpy-pandas-introduction/

def ANN(data):
    listavar = ['areaconstruida',
                'habitaciones',
                'banos',
                'garajes',
                'estrato',
                'scacodigo',
                'tiempodeconstruido',
                'valor']

                # Variables que ya no estan: barrio,localidad,cuartodeservicio,saloncomunal,conjuntocerrado
                
    # Keep variables
    data = data[listavar]
    
    # Eliminar donde sea un null 
    data       = data.dropna()
    data.index = range(len(data))
    
    # Crear variables dummies 
    list_dummies  = ['scacodigo','habitaciones','banos','garajes','estrato','tiempodeconstruido']
    for i in list_dummies:
        if i in list(data):
            newcol = pd.get_dummies(data[i])
            if newcol.empty is False:
                try:    newcol.columns = [elimina_tildes(i)+'#'+str(int(z)) for z in list(newcol)]
                except: newcol.columns = [elimina_tildes(i)+'#'+elimina_tildes(z) for z in list(newcol)]
                data = data.drop(columns=[i]) 
                data = pd.merge(data, newcol, left_index=True, right_index=True)

    # Transformar 
    vardep = 'valor'
    minmax = {} 
    for i in tqdm(list(data)):
        if i!=vardep:
            minvalue = data[i].min()
            maxvalue = data[i].max()
            minmax.update({i:{'min':minvalue,'max':maxvalue}})
            newval   = (data[i]-minvalue)/(maxvalue-minvalue)
            data[i]  = newval
            
    # Algoritmo
    datatotal = copy.deepcopy(data)
    mapeold   = np.inf
    lmd       = 1e-4
    nhdl      = 0.7
    
    # Numero de hidden layers
    data      = copy.deepcopy(datatotal)
    options   = {'hiddenlayers':[1],'lambdavalue':lmd,'tipofun':'cuadratica','biasunit':'on','xtrans':'minmax','ytrans':'log'}        
    terminado = 0
    while terminado==0:
        numcoef = NumCoef(data.drop(columns=[vardep]).shape[1],options)
        if (numcoef/len(data))>nhdl:
            terminado = 1
        else: options['hiddenlayers'][0] += 1
    
    numcoef = NumCoef(data.drop(columns=[vardep]).shape[1],options)    
    coef    = [random.uniform(-0.1, 0.1) for z in range(numcoef)]
    if options['ytrans']=='log': varyini = np.log(data[[vardep]])  # Variable dependiente
    else: varyini = data[[vardep]]
        
    # ANN
    varxini     = data.drop(columns=[vardep]) # Data matrix X 
    yini        = varyini.values
    xini        = varxini.values
    funresult   = scipy.optimize.minimize(FunOpt, coef, args=(yini.T,xini.T,options), method='L-BFGS-B', jac=GradOpt, bounds=None, tol=None, callback=None, options={'disp': None, 'maxcor': 10, 'ftol': 2.220446049250313e-09, 'gtol': 1e-05, 'eps': 1e-08, 'maxfun': 15000, 'maxiter': 15000, 'iprint': -1, 'maxls': 20})
    coef        = funresult['x'].tolist()
    varx        = data.drop(columns=[vardep]) # Data matrix X
    x           = varxini.values
    value       = ForecastFun(coef,x.T,options)
    if options['ytrans']=='log':
        value = np.exp(value)
    compare             = data[[vardep]]
    compare['forecast'] = pd.DataFrame(data = {'forecast':value[0]} )
    compare['error']    = (abs(compare['valor']-compare['forecast'])/compare['valor'])
    mape                = compare['error'].mean()
    # Compare
    if mape<mapeold:
        mapeold = mape
        result  = {'coef':coef,
                   'options':options,
                   'varlist':list(varx),
                   'minmax':minmax,
                   'MAPE': mape,
                   'cuantiles':compare['error'].quantile([0.25,0.5,0.75,0.975,0.99]).to_dict()}
    print({'lambda':lmd,'hdl':str(options['hiddenlayers']),'numcoef':str(numcoef),'ndata':str(len(data)),'MAPE':result['MAPE']})
    return result
    
def ForecastFun(coef,x,options):

    hiddenlayers = options['hiddenlayers']
    lambdavalue  = options['lambdavalue']
    biasunit     = options['biasunit']
    tipofun      = options['tipofun']
    numvar       = x.shape[0]
    nodos        = [numvar]
    for i in hiddenlayers: nodos.append(i)
    nodos.append(1)
        
    k          = len(nodos)
    suma       = 0
    theta      = [[] for i in range(k-1)]
    lambdac    = [[] for i in range(k-1)]
    lambdavect = np.nan
    for i in range(k-1):
        theta[i]   = np.reshape(coef[0:(nodos[i]+suma)*nodos[i+1]], (nodos[i]+suma, nodos[i+1]), order='F').T
        lambdac[i] = lambdavalue*np.ones(theta[i].shape)
        coef       = coef[(nodos[i]+suma)*nodos[i+1]:]
        if biasunit=='on':
            suma = 1
            lambdac[i][:,0] = 0
        [fil,col]  = lambdac[i].shape
        lambdavect = np.c_[lambdavect,np.reshape(lambdac[i],(fil*col,1)).T ]
    lambdac = lambdavect[:,1:].T
        
    # Forward Propagation
    a    = [[] for i in range(k)]
    z    = [[] for i in range(k)]
    g    = [[] for i in range(k)]
    a[0] = x
    numN = x.shape[1]
    for i in range(k-1):
        z[i+1]      = np.dot(theta[i],a[i])
        [ai,g[i+1]] = ANNFun(z[i+1],tipofun)
        if ((i+1)!=(k-1)) & (biasunit=='on'): a[i+1] = np.vstack((np.ones((1,numN)),ai))
        else:                                 a[i+1] = ai
    return a[-1]

def ObjFun(coef,y,x,options):

    hiddenlayers = options['hiddenlayers']
    lambdavalue  = options['lambdavalue']
    biasunit     = options['biasunit']
    tipofun      = options['tipofun']
    numvar       = x.shape[0]
    nodos        = [numvar]
    for i in hiddenlayers: nodos.append(i)
    nodos.append(1)
        
    k          = len(nodos)
    coefini    = coef
    suma       = 0
    theta      = [[] for i in range(k-1)]
    lambdac    = [[] for i in range(k-1)]
    lambdavect = np.nan
    for i in range(k-1):
        theta[i]   = np.reshape(coef[0:(nodos[i]+suma)*nodos[i+1]], (nodos[i]+suma, nodos[i+1]), order='F').T
        lambdac[i] = lambdavalue*np.ones(theta[i].shape)
        coef       = coef[(nodos[i]+suma)*nodos[i+1]:]
        if biasunit=='on':
            suma = 1
            lambdac[i][:,0] = 0
        [fil,col]  = lambdac[i].shape
        lambdavect = np.c_[lambdavect,np.reshape(lambdac[i],(fil*col,1)).T ]
    lambdac = lambdavect[:,1:].T
        
    # Forward Propagation
    a    = [[] for i in range(k)]
    z    = [[] for i in range(k)]
    g    = [[] for i in range(k)]
    a[0] = x
    numN = x.shape[1]
    for i in range(k-1):
        z[i+1]      = np.dot(theta[i],a[i])
        [ai,g[i+1]] = ANNFun(z[i+1],tipofun)
        if ((i+1)!=(k-1)) & (biasunit=='on'): a[i+1] = np.vstack((np.ones((1,numN)),ai))
        else:                                 a[i+1] = ai
        
    # Backpropagation
    delta     = [[] for i in range(k)]
    delta[-1] = (a[-1]-y)*g[-1]
    
    for i in range(k-2,0,-1):
        thetai = theta[i]
        if biasunit=='on':
            thetai = theta[i][:,1:] 
        #delta[i] = ((thetai.T)*delta[i+1])*g[i]
        delta[i] = np.matmul(thetai.T, delta[i+1])*g[i]
    
    # Gradiente
    diftheta = np.nan
    for i in range(k-1):
        gradmat   = np.dot(delta[i+1],a[i].T)
        [fil,col] = gradmat.shape
        diftheta  = np.c_[diftheta, np.reshape(gradmat,(fil*col,1)).T]
    diftheta   = diftheta[:,1:].T
    #lambdapart = ((lambdac.T)*coefini).T
    lambdapart = np.matmul(lambdac.T,coefini).T
    grad       = ((1/numN)*diftheta+ (1/numN)*lambdapart).T
    
    # Funcion Objetivo
    coefini    = np.array(coefini)
    firstpart  = ((y-a[-1])*(y-a[-1])).sum()
    secondpart = coefini*coefini
    secondpart = np.reshape(secondpart,(np.array(secondpart).shape[0],1))
    secondpart = lambdac*secondpart
    secondpart = secondpart.sum()
    fun        = (1/(2*numN))*firstpart + (1/(2*numN))*secondpart
    return [fun,grad[0]]

def FunOpt(coef,y,x,options):

    hiddenlayers = options['hiddenlayers']
    lambdavalue  = options['lambdavalue']
    biasunit     = options['biasunit']
    tipofun      = options['tipofun']
    numvar       = x.shape[0]
    nodos        = [numvar]
    for i in hiddenlayers: nodos.append(i)
    nodos.append(1)
        
    k          = len(nodos)
    coefini    = coef
    suma       = 0
    theta      = [[] for i in range(k-1)]
    lambdac    = [[] for i in range(k-1)]
    lambdavect = np.nan
    for i in range(k-1):
        theta[i]   = np.reshape(coef[0:(nodos[i]+suma)*nodos[i+1]], (nodos[i]+suma, nodos[i+1]), order='F').T
        lambdac[i] = lambdavalue*np.ones(theta[i].shape)
        coef       = coef[(nodos[i]+suma)*nodos[i+1]:]
        if biasunit=='on':
            suma = 1
            lambdac[i][:,0] = 0
        [fil,col]  = lambdac[i].shape
        lambdavect = np.c_[lambdavect,np.reshape(lambdac[i],(fil*col,1)).T ]  
    lambdac = lambdavect[:,1:].T
        
    # Forward Propagation
    a    = [[] for i in range(k)]
    z    = [[] for i in range(k)]
    g    = [[] for i in range(k)]
    a[0] = x
    numN = x.shape[1]
    for i in range(k-1):
        z[i+1]      = np.dot(theta[i],a[i])
        [ai,g[i+1]] = ANNFun(z[i+1],tipofun)
        if ((i+1)!=(k-1)) & (biasunit=='on'): a[i+1] = np.vstack((np.ones((1,numN)),ai))
        else:                                 a[i+1] = ai
        
    # Funcion Objetivo
    coefini    = np.array(coefini)
    firstpart  = ((y-a[-1])*(y-a[-1])).sum()
    secondpart = coefini*coefini
    secondpart = np.reshape(secondpart,(np.array(secondpart).shape[0],1))
    secondpart = lambdac*secondpart
    secondpart = secondpart.sum()
    fun        = (1/(2*numN))*firstpart + (1/(2*numN))*secondpart
    return fun


def GradOpt(coef,y,x,options):

    hiddenlayers = options['hiddenlayers']
    lambdavalue  = options['lambdavalue']
    biasunit     = options['biasunit']
    tipofun      = options['tipofun']
    numvar       = x.shape[0]
    nodos        = [numvar]
    for i in hiddenlayers: nodos.append(i)
    nodos.append(1)
        
    k          = len(nodos)
    coefini    = coef
    suma       = 0
    theta      = [[] for i in range(k-1)]
    lambdac    = [[] for i in range(k-1)]
    lambdavect = np.nan
    for i in range(k-1):
        theta[i]   = np.reshape(coef[0:(nodos[i]+suma)*nodos[i+1]], (nodos[i]+suma, nodos[i+1]), order='F').T
        lambdac[i] = lambdavalue*np.ones(theta[i].shape)
        coef       = coef[(nodos[i]+suma)*nodos[i+1]:]
        if biasunit=='on':
            suma = 1
            lambdac[i][:,0] = 0
        [fil,col]  = lambdac[i].shape
        lambdavect = np.c_[lambdavect,np.reshape(lambdac[i],(fil*col,1)).T ]
    lambdac = lambdavect[:,1:].T
        
    # Forward Propagation
    a    = [[] for i in range(k)]
    z    = [[] for i in range(k)]
    g    = [[] for i in range(k)]
    a[0] = x
    numN = x.shape[1]
    for i in range(k-1):
        z[i+1]      = np.dot(theta[i],a[i])
        [ai,g[i+1]] = ANNFun(z[i+1],tipofun)
        if ((i+1)!=(k-1)) & (biasunit=='on'): a[i+1] = np.vstack((np.ones((1,numN)),ai))
        else:                                 a[i+1] = ai
        
    # Backpropagation
    delta     = [[] for i in range(k)]
    delta[-1] = (a[-1]-y)*g[-1]
    
    for i in range(k-2,0,-1):
        thetai = theta[i]
        if biasunit=='on':
            thetai = theta[i][:,1:] 
        #delta[i] = ((thetai.T)*delta[i+1])*g[i]
        delta[i] = np.matmul(thetai.T, delta[i+1])*g[i]
    
    # Gradiente
    diftheta = np.nan
    for i in range(k-1):
        gradmat   = np.dot(delta[i+1],a[i].T)
        [fil,col] = gradmat.shape
        diftheta  = np.c_[diftheta, np.reshape(gradmat,(fil*col,1)).T]
    diftheta   = diftheta[:,1:].T
    #lambdapart = ((lambdac.T)*coefini).T
    lambdapart = np.matmul(lambdac.T,coefini).T
    grad       = ((1/numN)*diftheta+ (1/numN)*lambdapart).T
    return grad[0]

def NumCoef(k,options):
    hiddenlayers = options['hiddenlayers']
    biasunit     = options['biasunit']
    nodos        = [k]
    for i in hiddenlayers: nodos.append(i)
    nodos.append(1) 
    if biasunit!='on':
        biasunit = 'off'
    result = 0
    suma   = 0
    for i in range(len(nodos)-1):
        if biasunit=='on':
            result = result + (nodos[i]+suma)*nodos[i+1]
            suma   = 1
        else: result = result + nodos[i]*nodos[i+1]
    return result

def ANNFun(z, tipofun):
    z = np.asarray(z)
    if tipofun=='lineal':
        f = z
        g = 1
    if tipofun=='logistica':
        f = 1/(1+mt.exp(-z))
        g = f*(1-f)
    if tipofun=='exp':
        f = np.exp(z)
        g = np.exp(z)
    if tipofun=='cuadratica':
        f = z + 0.5*(z*z)
        g = 1 + z
    if tipofun=='cubica':
        f = z + 0.5*(z*z)+(1/3.0)*(z*z*z)
        g = 1 + z + z*z
        
    return [f,g]

def listdrop(lista,addrop):
    try:
        if addrop!='':
            for i in addrop: lista.remove(i)
    except: pass
    return lista
    
def elimina_tildes(s):
    s = s.replace(' ','').lower().strip()
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))