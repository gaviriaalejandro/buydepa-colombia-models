from datetime import datetime

def tiempoconstruido(x):
    result = None
    try:
        if isinstance(x, datetime):
            x = int(datetime.now().year-x)
        elif x>=1900 and x<=datetime.now().year:
            x = int(datetime.now().year-x)
            
        if isinstance(x, float) or isinstance(x, int): 
            x = int(x)
            
        if x<0 or x>100: x = None
        
        if isinstance(x, int):
            if x<=1:   result = 'Menos de 1 año'
            elif (x>1) and (x<=8):   result = '1 a 8 años'
            elif (x>8) and (x<=15):  result = '9 a 15 años'
            elif (x>15) and (x<=30): result = '16 a 30 años'
            elif x>30: result = 'más de 30 años'
    except: 
        pass
    return result

