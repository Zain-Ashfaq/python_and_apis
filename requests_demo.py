import requests
import json

# get request

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(type(post_codes_req)) # <Response [200]>
print(type(post_codes_req.status_code)) # 200
print(post_codes_req.content) # returns content from uri as bytes
print(post_codes_req.json())
print(type(post_codes_req.json()))





test = post_codes_req.json()
print(test.get("result").get("postcode"))

# POST request - sending data to the API

json_body = json.dumps({'postcodes': ["PR3 OSG", "M45 6GN", "EX165BL"]})
print(json_body)
headers = {'Content-Type': 'application/json'}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())

# Pokemon api

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
print(pokemon_req.json()['forms'][0]['name'])

bbc_request = requests.get("https://www.bbc.co.uk/")
#print(bbc_request.content)