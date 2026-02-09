import json 
#JSON String ↔ Python Object

json_str = '{"name":"saleem","age":36}'
data =json.loads(json_str)
print(data["name"])

#Python → JSON (dumps)

data = json.dumps(json_str)
print(data)


#Write JSON to file

with open("data1.json","w") as f:
    data =json.dump(data,f)

#Read JSON from file

with open("data.json","r") as f:
    response =json.load(f)

#JSON in APIs responses
print(response["data"]["name"])
if response.get("status") == "success":
    print("API call success")
    #Handle missing keys safely
    print(response.get("error", "No error"))

#Handling List of JSON Objects

with open("list.json","r") as f:
    response =json.load(f)

for r in response:
    print(r["name"])
  
    
    