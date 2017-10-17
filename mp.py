#print ("test commit
#sudo pip install requests
import requests 
main_api='https://opendata.arcgis.com/datasets/3df29a3d088a42d890f11d027ea1c0be_0.geojson'
json_data =requests.get(main_api).json()
formatted_address=json_data['features'][0]['properties']['park_name']
print('formatted_address')

