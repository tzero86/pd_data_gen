#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Elias Medina (@tzero86) & Matias Paglia
# Created Date: 10-21-2021
# Last_Updated: 08-10-2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" ProviderDirectory Batch JSON Data Generator (Doctors, Facilities & Groups)"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import datetime
import json
import random
import os

# globals
state_specific_addresses = []
total_records = 400
target_state = 'VA'


# This function reads from the addresses file
def get_state_data():
	new_path = os.path.join(os.getcwd(), 'addresses-us-all.json')
	addresses_source = open(new_path, )
	addresses = json.load(addresses_source)

	for address in addresses['addresses']:
		if address['state'] == target_state and 'city' in address:
			state_specific_addresses.append(address)


# print(json.dumps(state_specific_addresses))


# It returns the date formatted as YYYYMMDD to be used in the output's file name
def get_date():
	d = str(datetime.date.today())
	s = d.replace('-', '')
	return s


# This function takes care of actually saving the file, supporting specific OS paths.
def save_to_file(data):
	date = get_date()
	new_path = os.path.join(os.getcwd(), f'PD_Issuer1_{date}.json')
	print(new_path)
	with open(new_path, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=4)
	print(f'Data generated into this file: PD_Issuer1_{date}.json')


# this generates the objects for the JSON data file
def gen_providers_json():
	pd_types = ['INDIVIDUAL', 'FACILITY', 'GROUP']
	pd_facility_names = ['Renal Dialysis Unit', 'Northwest Endoscopy Center LLC', 'Main Street Hospital',
	                     'Central Hospital', 'City Care Center']
	pd_facility_types = ["Hospital", "Ambulatory"]
	pd_specialties = ['Licensed Behavioral Analyst', 'Ophthalmology', 'Endocrinology']
	pd_program_type = ['QHP', 'QDP']
	pd_board_certification = ['MD', 'PA', 'PAC']
	pd_education = ['MD']
	pd_accepting = ['accepting', 'not accepting']
	pd_plan_id_type = ['HIOS-PLAN-ID']
	# Plan values for QA Only.
	pd_hios_plan_id = ["25210CA0110016", "25210CA0070012", "25210CA0060011", "25210CA0050010",
	                   "25210CA0090014", "25210CA0080013", "25210CA0110016", "25210CA0120017",
	                   "25210CA0120017"]
	# Plan values for UAT only.
	pd_hios_plan_id_UAT = ["11241VA0010001","11241VA0020001","11241VA0030001","11241VA0040001","11241VA0050001",
                        "23190VA0060001","10544VA0090001","10544VA0100001","10544VA0120001","10544VA0110001",
                        "10544VA0320004","10544VA0080001","11241VA0090001","11241VA0090002","11241VA0090003",
                        "11241VA0090004","11241VA0090005","11241VA0090006","71095VA0340012","71095VA0340013",
                        "71095VA0340014","10544VA0430004","10544VA0430005","10544VA0430006"]
	pd_network_tier = ['PREFERRED', 'NON-PREFERRED']
	pd_prov_languages = ['English', 'Spanish', 'Danish', 'Italian', 'German', 'French']
	pd_prov_gender = ['Female', 'Male']

	# We need to generate N number of objects
	json_data = []
	get_state_data()
 	# If the Sate is CA we use the QA plans, for any other we use UAT (This needs a proper function to support multiple environments)) 
	target_plans = pd_hios_plan_id if (target_state == 'CA') else pd_hios_plan_id_UAT 
	for x in range(0, total_records):
		gen_type = random.choice(pd_types)
		# print(gen_type)
		try:
			address = random.choice(state_specific_addresses)
		except:
			print(f'ERROR: It seems there is no data available for the state you selected: {target_state}')
			quit()
		json_body = {
			"npi": str(random.randint(1000000000, 9999999999)),
			"type": gen_type,
			**({"name": {
				"first": "Juan",
				"middle": "Carlos",
				"last": "Provider_" + str(x),
				"suffix": "Jr."
			}} if gen_type == "INDIVIDUAL" else {}),
			**({
				   "group_name": random.choice(pd_facility_names)
			   } if gen_type == "GROUP" else {}),
			**({"facility_name": random.choice(pd_facility_names), } if gen_type == 'FACILITY' else {}),
			**({"facility_type": [random.choice(pd_facility_types)], } if gen_type == 'FACILITY' else {}),
			"addresses": [
				{
					"address": address['address1'],
					"address_2": address['address2'],
					"city": address['city'],
					"state": address['state'],
					"zip": address['postalCode'],
					"phone": str(random.randint(1000000000, 9999999999))
				}
			],
			**({"specialty": [random.choice(pd_specialties)]} if gen_type != "GROUP" else {}
			   ),
			"program_type": [random.choice(pd_program_type)],
			"board_certification": [random.choice(pd_board_certification)],
			"education": [random.choice(pd_education)],

			**({"accepting": random.choice(pd_accepting),
			    } if gen_type == "INDIVIDUAL" else {}),
			"plans": [
				{
					"plan_id_type": random.choice(pd_plan_id_type),
					"plan_id": random.choice(target_plans),
					"network_tier": random.choice(pd_network_tier),
					"years": [2021, 2022, 2023]
				},
				{
					"plan_id_type": random.choice(pd_plan_id_type),
					"plan_id": random.choice(target_plans),
					"network_tier": random.choice(pd_network_tier),
					"years": [2021, 2022, 2023]
				}
			],
			**({"languages": [random.choice(pd_prov_languages)]} if gen_type != 'GROUP' else {}),
			**({"gender": random.choice(pd_prov_gender)} if gen_type == 'INDIVIDUAL' else {}),
			"last_updated_on": "2022-08-08"
		}
		json_data.append(json_body)
	##print(json.dumps(json_data, indent=4, sort_keys=False))
	save_to_file(json_data)


if __name__ == '__main__':
	gen_providers_json()
