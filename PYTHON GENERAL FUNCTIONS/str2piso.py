import re

#-----------------------------------------------------------------------------#
# str2piso
#-----------------------------------------------------------------------------#
def str2piso(x):
    result = None
    try:
        x = re.sub('[^0-9]','',x.strip())
        if len(x)==3: result = int(x[0])
        elif len(x)==4: result = int(x[0:2])
    except: pass
    return result