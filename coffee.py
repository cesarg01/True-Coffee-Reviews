import googlemaps
import requests
import pprint
import json

# Get the latitude and longitude of a location.
def get_coordinates(geocode_result, coord):
    try:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]
        coord['lat'] = lat
        coord['lng'] = lng 
    except IndexError as err:
        print('There are no coordinates for the location specified.', err)
        return None

    return coord

# Get the id of the place we are looking for.
def get_place_id(geocode_result, place_id):
    try:
        place_id = geocode_result[0]['place_id'].strip('\'')
    except KeyError as err:
        print('No Place ID for the location you are looking for.', err)
        return None


    return place_id



####################################################### Main #######################################################
# Create a map with None values
coord = {'lat': None, 'lng': None}
key = 'key goes here'
gmaps = googlemaps.Client(key)
try:
    geocode_result = gmaps.geocode("Cat and Cloud Aptos, CA")
    coord = get_coordinates(geocode_result, coord)
    print('The coordinates are: ', coord)

    place_id = ''
    place_id = get_place_id(geocode_result, place_id)
    print(place_id)

    url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + place_id + '&fields=name,rating,formatted_phone_number,website,reviews&key=AIzaSyAvoK_HHweMStq2uEXSYIWlygfYXFP9q4g'
    res = requests.get(url)
    place_details = json.loads(res.content)
    #pprint.pprint(place_details)
    rating = place_details['result']['rating']
    print('Rating for {} is: '.format(place_details['result']['name']), rating)
except IndexError as err:
    print('There is no such location.', err)





#pprint.pprint(geocode_result[0]['place_id'])
#place_id = geocode_result[0]['place_id'].strip('\'')
#print(place_id)
#url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + place_id + '&fields=name,rating,formatted_phone_number,website,reviews&key=key'


#res = requests.get(url)
#place_details = json.loads(res.content)
#pprint.pprint(place_details)
#rating = place_details['result']['rating']
#print('Rating for Verve is: ', rating)