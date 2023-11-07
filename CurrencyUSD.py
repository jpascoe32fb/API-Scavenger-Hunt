import freecurrencyapi

USD_amount = 100
client = freecurrencyapi.Client('key')

result = client.latest(base_currency='USD', currencies=['EUR'])

EUR_amount = USD_amount * result['data']['EUR']

print("EUR amount: ", EUR_amount)