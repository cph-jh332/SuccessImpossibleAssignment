import requests
import os.path
import json
import operator

if not os.path.exists('./coinapi.json'):
    headers = {'X-CoinAPI-Key' : '91562386-7363-47E2-837B-C1FFF6F8A95E'}
    url = 'https://rest.coinapi.io/v1/trades/BITSTAMP_SPOT_BTC_USD/history?time_start=2016-01-01T00:00:00&time_end=2017-01-01T00:00:00'
    response = requests.get(url, headers=headers)
    my_file = open('coinapi.json', 'w')
    my_file.write(response.text)
    my_file.close()
    my_file = json.loads(response.json)
else:
    my_file = open('coinapi.json')
    my_file = json.loads(my_file.read())

def question1():
    highest_volume_id = ''
    highest_volume = 0
    for item in my_file:
        if item['size'] > highest_volume:
            highest_volume = item['size']
            highest_volume_id = item['uuid']
    
    print('the highest volume is {} and the id is {}'.format(highest_volume, highest_volume_id))

def question2():
    price = [el['price'] for el in my_file]
    average_price = sum(price) / len(price)
    print('the average price pr transaction is {}'.format(average_price))

def question3():
    count = {}
    for el in my_file:
        if el['taker_side'] in count:
            count[el['taker_side']] += 1
        else:
            count[el['taker_side']] = 1
    print('the most favoured transaction type is {}'.format(max(count.items(), key=operator.itemgetter(1))[0]))

def question5():
    total_volume = sum([el['size'] for el in my_file])
    print('total volume per day is {}'.format(total_volume))

question1()
question2()
question3()
question5()