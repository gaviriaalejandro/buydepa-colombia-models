from datetime import date

def getmaxdatefile(x):
    varlist   = [w for w in x if '.xlsx' in w]
    datelist  = [date(int(w.split('_')[1].split('-')[0]), int(w.split('-')[1]),  int(w.split('-')[2].split('.')[0])) for w in varlist]
    pos       = datelist.index(max(datelist))
    filename  = varlist[pos]
    file_date = varlist[pos].split('_')[1].split('.')[0]
    return filename,file_date