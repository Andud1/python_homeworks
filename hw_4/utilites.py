import requests

def currency_rates(val_code):
    result = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    result = result.text.replace('<Valute>', '')
    result = result.replace('</Valute>', '')
    result = result.replace('</ValCurs>', '')
    result = result.replace('</Nominal>', '')
    result = result.replace('<Nominal>', '')
    result = result.replace('<?xml version="1.0" encoding="windows-1251"?>', '')
    result = result.replace('<Valute>', '')
    result = result.replace('<NumCode>', '')
    result = result.replace('</NumCode>', '')
    result = result.replace('<CharCode>', ' ')
    result = result.replace('</CharCode>', ' ')
    result = result.replace('<Value>', '')
    result = result.replace('</Value>',  '')
    result = result.replace('<Name>', ' ')
    result = result.replace('</Name>', ' ')
    result = result.replace(',', '.')
    result = result.split('<Valute ID=')
    result.remove(result[0])
    i = 0
    valutes = {}
    while i < len(result):
        temp_result = result[i].split(' ')
        temp_result.remove(temp_result[0])
        temp_value = float(temp_result[len(temp_result) -1])
        valutes[temp_result[0]] = temp_value
        result[i] = ' '.join(temp_result)
        i += 1

    # print(valutes)
    return valutes.get(val_code)