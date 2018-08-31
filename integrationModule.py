#!/usr/bin/env python

import pandas as pd
import json
import requests
import getAccessToken

auth = AuthenticationApi()
access_token = auth.oath2()

class App(object):

	def __init__(self):
        print("init")

	def linkedin_companies_parser(self, url):

		# Montando a requisição para a API do Linkedin

		r = request.get_json(url, headers={'Authorization': access_token})

		
		# Fazendo parcing das do arquivo json recebido 

		entityStatus = r["entityStatus"]
		vanityName = r["vanityName"]	
		id1 = r["id"]
		industries = r["industries"]
		foundedOn = r["foundedOn"]
		website = r["website"]
		specialties = r["specialties"]
		staffCountRange = r["staffCountRange"]

		# Montando arquivo json para resposta

		data = {
		    "entityStatus":entityStatus,
		    "vanityName":vanityName,
		    "id":id1,
		    "industries":industries,
		    "foundedOn":foundedOn,
		    "website":website,
		    "specialties":specialties,
		    "staffCountRange":staffCountRange

		}

		return data

	 
	def consult_api(self, *lista):
	    
		# Recebendo os dados das empresas e consultando a API

	    company_list = lista
	    
	    extracted_data = []
	    for i in company_list:
	    	url = 'https://api.linkedin.com/v2/organizations?q=vanityName&vanityName='+i
	    	extracted_data.append(linkedin_companies_parser(url))
	    	f = open('data.json', 'w')
	    	json.dump(extracted_data, f, indent=4)

if __name__ == '__main__':
	consult_api()

