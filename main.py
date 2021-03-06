#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Elias Medina (@tzero86)
# Created Date: 10-21-2021
# version ='0.1'
# ---------------------------------------------------------------------------
""" ProviderDirectory Batch JSON Data Generator"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import json
import random

# globals
state_specific_addresses = []
total_records = 1000
target_state = 'CA'


def get_state_data():
    addresses_source = open('addresses-us-all.json', )
    addresses = json.load(addresses_source)

    for address in addresses['addresses']:
        if address['state'] == target_state and 'city' in address:
            state_specific_addresses.append(address)
# print(json.dumps(state_specific_addresses))


# Save end file to disk
def save_to_file(data):
    with open('PD_Issuer1_20201212.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# this generates the objects for the JSON data file
def gen_providers_json():
    pd_types = ['INDIVIDUAL', 'FACILITY']
    pd_facility_names = ['Renal Dialysis Unit', 'Northwest Endoscopy Center LLC', 'Main Street Hospital',
                         'Central Hospital', 'City Care Center']
    pd_facility_types = ["Hospital", "Ambulatory"]
    pd_specialties = ['Licensed Behavioral Analyst', 'Ophthalmology', 'Endocrinology']
    pd_program_type = ['QHP', 'QDP']
    pd_board_certification = ['NP']
    pd_education = ['Orthopedic']
    pd_accepting = ['accepting', 'not accepting']
    pd_plan_id_type = ['HIOS-PLAN-ID']
    pd_hios_plan_id = ["25210CA0110016", "25210CA0070012", "25210CA0060011", "25210CA0050010",
                       "25210CA0090014", "25210CA0080013", "25210CA0110016", "25210CA0120017",
                       "25210CA0120017", ]
    pd_network_tier = ['PREFERRED', 'NON-PREFERRED']
    pd_years = [2021, 2022]
    pd_prov_languages = ['English', 'Spanish', 'Danish', 'Italian', 'German', 'French']
    pd_prov_gender = ['female', 'male']

    # We need to generate N number of objects
    json_data = []
    get_state_data()
    for x in range(1, total_records):
        gen_type = random.choice(pd_types)
      #  print(gen_type)
        address = random.choice(state_specific_addresses)
        address2 = random.choice(state_specific_addresses)
        json_body = {
            "npi": str(random.randint(1000000000, 9999999999)),
            "type": gen_type,
            **({"name": {
                "first": "Juan",
                "middle": "Carlos",
                "last": "Provider_" + str(x),
                "suffix": "Jr."
            }} if gen_type == "INDIVIDUAL" else {}),
            **({"facility_name": random.choice(pd_facility_names) + "_" + str(x), } if gen_type == 'FACILITY' else {}),
            **({"facility_type": [random.choice(pd_facility_types)], } if gen_type == 'FACILITY' else {}),
             
            "addresses": [
                {
                    "address": address['address1'],
                    "address_2": address['address2'],
                    "city": address['city'],
                    "state": address['state'],
                    "zip": address['postalCode'],
                    "phone": str(random.randint(1000000000, 9999999999))
                },
                {
                    "address": address2['address1'],
                    "address_2": address2['address2'],
                    "city": address2['city'],
                    "state": address2['state'],
                    "zip": address2['postalCode'],
                    "phone": str(random.randint(1000000000, 9999999999))
                }
            ],
            **({"specialty": [random.choice(pd_specialties)], } if gen_type == 'INDIVIDUAL' else {}),
            "program_type": [random.choice(pd_program_type)],
            "board_certification": [random.choice(pd_board_certification)],
            "education": [random.choice(pd_education)],
            "accepting": random.choice(pd_accepting),
            "plans": [
                {
                    "plan_id_type": random.choice(pd_plan_id_type),
                    "plan_id": random.choice(pd_hios_plan_id),
                    "network_tier": random.choice(pd_network_tier),
                    "years": [2021, 2022]
                }
            ],
            **({"languages": [random.choice(pd_prov_languages)], } if gen_type == 'INDIVIDUAL' else {}),
            
            **({"gender": random.choice(pd_prov_gender)} if gen_type == 'INDIVIDUAL' else {}),
            "last_updated_on": "2021-07-12"
        }
        json_data.append(json_body)
   # print(json.dumps(json_data, indent=4, sort_keys=False))
    save_to_file(json_data)


if __name__ == '__main__':
    gen_providers_json()
