import re
import unicodedata

#-----------------------------------------------------------------------------#
# elimina_tildes
#-----------------------------------------------------------------------------#
def elimina_tildes(s):
    s      = re.sub(r'[\W_]+', '_', s).lower().strip('_').strip()
    result = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    return result