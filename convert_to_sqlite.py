# Convert JSON objects into sqlite records
import os, json, sqlite3

connection = sqlite3.connect('data/delicts.db')
c = connection.cursor()

for subdir, dirs, files in os.walk('data'):
    for file in files:
        if (file.endswith('.json')):
            year = subdir.split('/')[-1]
            district = json.load(open(os.path.join(subdir, file)))

            for delict, months in district.items():
                for month, neighbourhoods in enumerate(months):
                    for neighbourhood in neighbourhoods:
                        print(neighbourhood['name'], month)

                        c.execute('''INSERT INTO delicts(delict, latitude, longitude, month, year, count, name, neighbourhood, district) VALUES(?,?,?,?,?,?,?,?,?)''', (delict, neighbourhood['latitude'], neighbourhood['longitude'], month + 1, year, neighbourhood['delicts'], neighbourhood['name'], neighbourhood['code'], file.split('.')[0]))

connection.commit()
c.close()
