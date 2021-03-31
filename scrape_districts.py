# Scrape all district codes
import requests

for g in range(10000):
    url = 'http://www.hoeveiligismijnwijk.nl/getGebied.php'
    params = dict(
        geb='stadsdeel',
        gebid=g
    )

    result = requests.get(url=url, params=params).text
    print(result or 'Nothing in ' + str(g) + '...')

    with open('data/areas.txt', 'a') as outfile:
        if (result):
            outfile.write(result + '\r\n')
