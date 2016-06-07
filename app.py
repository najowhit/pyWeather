import requests
import os
import config


def callAPI(url):
    response = requests.get(url)
    location_data = response.json()['name']
    stats_data = response.json()['main']
    forecast_data = response.json()['weather'][0]['main']
    #forecast_image = response.json()['weather'][0]['icon']

    curr_temp = stats_data['temp']
    temp_max = stats_data['temp_max']
    temp_min = stats_data['temp_min']

    dictionary = {'location': location_data, 'temperature': curr_temp,
    'forecast': forecast_data, 'high': temp_max, 'low': temp_min}

    return dictionary


def writeFile(txtFile, dictionary):
    file = open(txtFile, 'w')

    file.write('Location: ' + str(dictionary['location']) + '\n')
    file.write('Temperature: ' + str(dictionary['temperature']) + '\n')
    file.write('High: ' + str(dictionary['high']) + '\n')
    file.write('Low: ' + str(dictionary['low']) + '\n')
    file.write('Forecast: ' + str(dictionary['forecast']))

    file.close()


def readFile(txtFile):
    file = open(txtFile, 'r')

    contents = file.read()
    print(contents)

    file.close()


def printData(dictionary):
    print('Location: ' + dictionary['location'])
    print('Temperature: ' + str(dictionary['temperature']))
    print('High: ' + str(dictionary['high']))
    print('Low: ' + str(dictionary['low']))
    print('Forecast: ' + dictionary['forecast'])


def main():
    zipcode = input("Please enter your zipcode: ")
    country = input("Please enter your country code: ")

    url = "http://api.openweathermap.org/data/2.5/weather?zip={},{}&units=imperial&appid={}".format(zipcode, country, config.apikey)
    txtFile = "w_data.txt"

    dictionary = callAPI(url)
    printData(dictionary)

    """  writeFile(txtFile, dictionary)
    readFile(txtFile)
    scraped = os.path.isfile(txtFile)

    if not scraped:
        dictionary = callAPI(url)
        writeFile(txtFile, dictionary)
        readFile(txtFile)

    else:
        readFile(txtFile)"""

main()
