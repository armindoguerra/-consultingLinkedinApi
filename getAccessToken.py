import requests
import json

url = "https://www.linkedin.com/oauth/v2/accessToken"

code = "AQSL4Nq8RcRS_26WRJ0EF-Y4rg-NQAPEKGB6FuBwYiwvDARXHXGcEG6LGzY-ngmJF08CpRooWyE2y11h-8BP1uZn0UloX-OsaF1vBUjcGYYQFsj9vNBDQojn9dHjVONR11BO4dBa8_OuQkXx_QK8_nnSP6yx1VwrkvcAiW43"

Headers = {	    
    "Content-Type":"application/x-www-form-urlencoded"
}

payload = {
	"grant_type":"authorization_code",
	"code":code,
	"redirect_uri":"https://localhost:8000/login/callback",
	"client_id":"78c1j670w2r3pb",
	"client_secret": "V3Q5g9LsRWEpZKTM"
} 

r = requests.post(url, data=json.dumps(payload), headers=Headers)
json_data = json.loads(r.text)
print(json_data)