# 3102_AI_Proj
ICT3102 Docker project

### Mongo-Express
- To GET data from the db for image / question / answer / caption use the following: (use the mongo-express line through other docker containers, or if locally, use 0.0.0.0) 
```
http://0.0.0.0:8081/db/data3102/expArr/datatable?key=&value=&type=&query=&projection=
http://mongo-express:8081/db/data3102/expArr/datatable?key=&value=&type=&query=&projection=
```


- To POST data to insert a new record for image / question / answer / caption
```
http://0.0.0.0:8081/db/data3102/datatable
http://mongo-express:8081/db/data3102/datatable
```
- With POST data like:
```
document={"_id": ObjectID(),"image":"t","question":"qns","answer":"ans","caption":"capt"}
```

- or consider a cURL request similar to (change 0.0.0.0 to mongo-express if running in docker containers)
```
curl 'http://0.0.0.0:8081/db/data3102/datatable' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: http://0.0.0.0:8081' -H 'Connection: keep-alive' -H 'Referer: http://0.0.0.0:8081/db/data3102/datatable' -H 'Cookie: mongo-express=s%3AQFxPTxS0j-yWe94Oq4ZvfTqj2FI7W3WZ.LZ%2Buw3%2FBNU1skD%2FaW1WTAUBEDbVOQEOkAvNl0OpWWVs' -H 'Upgrade-Insecure-Requests: 1' --data-raw 'document=%7B%22_id%22%3A+ObjectID%28%29%2C%22image%22%3A%22t%22%2C%22question%22%3A%22qns%22%2C%22answer%22%3A%22ans%22%2C%22caption%22%3A%22capt%22%7D'
```

- Admin panel is available at http://0.0.0.0:8081 
