from datetime import datetime

def fix_antiguedad(x):
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
            result = x
    except: 
        pass
    return result

