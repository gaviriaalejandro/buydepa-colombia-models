import numpy as np
import math as mt

#-----------------------------------------------------------------------------#
# precio_compra
#-----------------------------------------------------------------------------#
def precio_compra(inputvar):
    #inputvar = {'precio_venta':400000000,'areaconstruida':85,'admon':320000,'ganancia':0.06,'comision_compra':0.003,'comision_venta':0.003,'nmonths':6,'provisionmt2':100000,'pinturamt2':13000}
    
    ganancia        = 0.06 # (6%)
    comision_compra = 0.003 # (0.3%)
    comision_venta  = 0.003 # (0.3%)
    nmonths         = 6
    provisionmt2    = 100000  # Para reparaciones / colchon financiero
    pinturamt2      = 13000
    IVA             = 0.19
    p1              = None
    admon           = None
    areaconstruida  = None
    
    if 'precio_venta' in inputvar:
        p1 = inputvar['precio_venta']
    if 'ganancia' in inputvar and inputvar['ganancia']>0 and inputvar['ganancia']<100: 
        ganancia = inputvar['ganancia']
    if 'areaconstruida' in inputvar:
        areaconstruida = inputvar['areaconstruida']
    if 'nmonths' in inputvar: 
        nmonths = inputvar['nmonths']
    if 'admon' in inputvar and inputvar['admon']>0: 
        admon = inputvar['admon']*1.1 # Es usual que reporten un menor valor de la administracion
    else: 
        admon = 5500*areaconstruida
    if 'pinturamt2' in inputvar: 
        pinturamt2 = inputvar['pinturamt2']
    if 'provisionmt2' in inputvar: 
        provisionmt2 = inputvar['provisionmt2']
    
    PRECIO_GANANCIA  = p1/(1+ganancia)
    GN_VENTA         = 164000+0.0033*p1  # (regresion)
    COMISION_VENTA   = comision_venta*p1
    PINTURA          = pinturamt2*(1+IVA)*areaconstruida
    ADMON            = admon*nmonths
    PROVISION        = provisionmt2*areaconstruida
    X                = PRECIO_GANANCIA-GN_VENTA-COMISION_VENTA-PINTURA-ADMON-PROVISION
    preciocompra     = (X-57000)/(1+(0.0262+comision_compra))
    preciocompra     = np.round(preciocompra, int(-(mt.floor(mt.log10(preciocompra))-2)))
    gn_compra        = 57000+0.0262*preciocompra
    gn_compra        = np.round(gn_compra, int(-(mt.floor(mt.log10(gn_compra))-2)))
    gn_venta         = np.round(GN_VENTA, int(-(mt.floor(mt.log10(GN_VENTA))-2)))
    COMISION_COMPRA  = (preciocompra*comision_compra)
    retorno_bruto_esperado = p1/preciocompra-1
    retorno_neto_esperado  = (p1-COMISION_COMPRA-COMISION_VENTA-PINTURA-ADMON-PROVISION)/preciocompra-1
    return {'precio_venta':p1,'preciocompra':preciocompra,'retorno_bruto_esperado':retorno_bruto_esperado,'retorno_neto_esperado':retorno_neto_esperado,'gn_compra':gn_compra,'gn_venta':gn_venta,'comisiones':COMISION_VENTA+COMISION_COMPRA,'otros_gastos':PINTURA+ADMON+PROVISION}
