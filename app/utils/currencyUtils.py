import locale

class CurrencyUtils():
    
    def getStringValue(value):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return 'R$ '+ str(locale.currency(value, grouping=True, symbol=None))   