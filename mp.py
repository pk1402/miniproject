#print ("test commit")
#sudo pip install requests
import requests 
main_api='https://opendata.arcgis.com/datasets/3df29a3d088a42d890f11d027ea1c0be_0.geojson'

json_data =requests.get(main_api).json()

#x=json_data.get("features")
#y =x[0]
#x for i in range(902):
#a  =" ".join(str(l) for l in x)
#po = a.get("properties")
#e = po.get("PARK_NAME")
#print(e)
fid=[]
cleanlist=[]
for i in range(902):
 my_result = json_data['features'][i]['properties']['PARK_NAME']
 #my_result2=json_data.get['feature']  
 fid.append(my_result)
 [cleanlist.append(x) for x in fid if x is not in cleanlist]
 #for i in fid:
  #print(i) 
  #print(type(a))
  #str1 = ''.join(a)
 print(my_result)
