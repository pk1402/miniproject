#print ("test commit")
#sudo pip install requests
import requests
import urllib.parse 
main_api='https://opendata.arcgis.com/datasets/3df29a3d088a42d890f11d027ea1c0be_0.geojson'
json_data =requests.get(main_api).json()

#x=json_data.get("features")
#y =x[0]
#x for i in range(902):
#a  =" ".join(str(l) for l in x)
#po = a.get("properties")
#e = po.get("PARK_NAME")
#print(e)

#fid=[]
#cleanlist=[]
#for i in range(902):
 #my_result = json_data['features'][i]['properties']['PARK_NAME']
 #my_result2=json_data.get['feature']  
 #fid.append(my_result,my_result2)
#[cleanlist.append(x) for x in fid if x is not in cleanlist]
 #for i in fid:
  #print(i) 
  #print(type(a))
  #str1 = ''.join(a)
 #print(my_result)
fid=[] #empty list
cleanlist=[]
for i in range(902):
    my_result = json_data['features'][i]['properties']['PARK_NAME'] #display park names in halifax
    my_result2 = json_data['features'][i]['properties']['HECTARES'] #display the area of park
    fid.append(my_result)
    fid.append(my_result2)
    #removing duplicates in the list
    [cleanlist.append(x) for x in fid if x not in cleanlist]

#second_api='https://maps.google.com/maps/api/geocode/json?'
#for parks in cleanlist:

    #url2=second_api+urllib.parse.urlencode({'address':parks})

#json_data=requests.get(url2).json()
    #formatted_address=json_data['results'][0]['geometry']['location']
    #print(parks)
    #for k,v in formatted_address.items():
    #print(k,v)
second_api='https://maps.google.com/maps/api/geocode/json?'
for parks in cleanlist: #unique park names print in new list
    url2=second_api+urllib.parse.urlencode({'address':parks})
    json_data=requests.get(url2).json()
    try:
        formatted_address=json_data['results'][0]['geometry']['location'] #location of the park is displayed
        print(parks)
        for k,v in formatted_address.items():
            print(k,v)
    except:
        pass

