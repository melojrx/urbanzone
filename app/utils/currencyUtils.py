import locale
import os

class CurrencyUtils():
    
    def getStringValue(value):
        os.environ['LC_ALL'] = 'pt_BR.UTF-8'
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return 'R$ '+ str(locale.currency(value, grouping=True, symbol=None))   