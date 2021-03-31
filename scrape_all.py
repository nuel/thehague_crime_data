# Scrape all data from the website
import json, requests

url = 'http://www.hoeveiligismijnwijk.nl/getDelicten.php'
params = dict(
    geb='wijk'
)

# Found in the web form
delict_codes = [100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 111, 117]

# Found by scraping district codes
districts = [51814, 51815, 51816, 51817, 51818, 51832, 51833, 51834, 51835, 51836, 51840, 51813, 51819, 51820, 51821, 51802, 51803, 51806, 51807, 51808, 51809, 51810, 51811, 51822, 51823, 51827, 51828, 51829, 51830, 51837, 51839, 51824, 51825, 51826, 51842, 51843, 51844, 50312, 50313, 50314, 50316, 50322, 50323, 50324, 50325, 50326, 50327, 50328, 50329, 60302, 60303, 60304, 60305, 60306, 60307, 60308, 60309, 62901, 63701, 63702, 63703, 63704, 63705, 63706, 63708, 63709, 51302, 51303, 51304, 51305, 51306, 51307, 51308, 51309, 48402, 48403, 48404, 48405, 48406, 48407, 48408, 48409, 55302, 55303, 55304, 55305, 55306, 55307, 55308, 55309, 55310, 55311, 55312, 55313, 55314, 55315, 55316, 55317, 55318, 55319, 55320, 55321]

# Trying out query manually reveals no data before 2011
for y in range(2011, 2018):
    print 'SCRAPING ' + str(len(districts)) + ' DISTRICTS FOR ' + str(y)

    params['jaar'] = y

    for g in districts:
    	print 'Gathering all data for district ' + str(g) + '...'

    	# Main data storage
        district = dict()

        for d in delict_codes:
        	# Param names found by inspecting network activity on web form
            params['del'] = d
            params['gebid'] = g
            months = []

            for m in range(1, 13):
                params['maand'] = m
                resp = requests.get(url=url, params=params).text

                # Raw data from the server, split by neighbourhood
                neighbourhoods = resp.split(';')
                neighbourhoods.pop()

                neighbourhoods_processed = []

                for n in neighbourhoods:
                    neighbourhood = dict()
                    raw_data = n.split('|')

                    # Construct the final JSON object
                    neighbourhood['name'] = raw_data[0]
                    neighbourhood['code'] = raw_data[1]
                    neighbourhood['delicts'] = raw_data[2]
                    neighbourhood['latitude'] = raw_data[3]
                    neighbourhood['longitude'] = raw_data[4]

                    neighbourhoods_processed.append(neighbourhood)

                months.append(neighbourhoods_processed)
            district[str(d)] = months

        # Write the data for this district out into its own file
        with open('data/' + str(y) + '/' + str(g) + '.json', 'w') as outfile:
            json.dump(district, outfile)
