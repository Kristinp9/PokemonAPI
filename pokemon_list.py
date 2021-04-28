import requests
import csv

ids=[]
nombres=[]

for i in range(1,898):
    url='https://pokeapi.co/api/v2/pokemon/{}/'.format(i)
    response=requests.get(url)
    if response.status_code==200:
        respuesta=response.json()
        ids.append(respuesta['id'])
        nombres.append(respuesta['name'])
        print('Done with row #{}'.format(i))

for i in range(10001,10220):
    url='https://pokeapi.co/api/v2/pokemon/{}/'.format(i)
    response=requests.get(url)
    if response.status_code==200:
        respuesta=response.json()
        ids.append(respuesta['id'])
        nombres.append(respuesta['name'])
        print('Done with row #{}'.format(i))
        
zipeado=zip(ids,nombres)
to_insert=list(zipeado)

with open('pokemons_list.csv','w+', newline ='') as p:
    write=csv.writer(p)
    write.writerow(['id','name'])
    write.writerows(to_insert)
    p.close()