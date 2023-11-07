import freecurrencyapi

JPY_amount = 1000
client = freecurrencyapi.Client('')

result = client.latest(base_currency='JPY', currencies=['GBP'])

GBP_amount = JPY_amount * result['data']['GBP']

print("GBP amount: ", GBP_amount)