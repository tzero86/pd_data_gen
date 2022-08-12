import datetime
import json
import random
import os

addresses_list = [{ "address": " 146 Brandywine Ct", "city": "Charlottesville", "state": "Virginia(VA)", "zip": "22901" } ,
                  { "address": " 1185 Owensville Rd", "city": "Charlottesville", "state": "Virginia(VA)", "zip": "22901" } ,
                  { "address": " 134 Hessian Hills Way #APT 1", "city": "Charlottesville", "state": "Virginia(VA)", "zip": "22901" } ,
                  { "address": " 1160 Tennis Rd", "city": "Charlottesville", "state": "Virginia(VA)", "zip": "22901" } ,
                  { "address": " 1006 Park St", "city": "Charlottesville", "state": "Virginia(VA)", "zip": "22901" } ,
                  { "address": " 1025 Cottonwood Rd", "city": "Charlottesville", "state": "Virginia(VA)", "zip": "22901" } ,
                  { "address": " 1201 Lili Ln", "city": "Charlottesville", "state": "Virginia(VA)", "zip": "22901" } ,
                  { "address": " 3070 Morewood Ln", "city": "Charlottesville", "state": "Virginia(VA)", "zip": "22901" } ,
                  { "address": " 170 Georgetown Rd #A", "city": "Charlottesville", "state": "Virginia(VA)", "zip": "22901" },
                  { "address": " 296 Harriston Rd", "city": "Grottoes", "state": "Virginia(VA)", "zip": "24441" } ,
                  { "address": " 9889 Greenleaf St", "city": "Grottoes", "state": "Virginia(VA)", "zip": "24441" } ,
                  { "address": " 9321 Browns Gap Rd", "city": "Grottoes", "state": "Virginia(VA)", "zip": "24441" } ,
                  { "address": " 40 Horsehead Rd", "city": "Grottoes", "state": "Virginia(VA)", "zip": "24441" } ,
                  { "address": " Black Rock Mhpk", "city": "Grottoes", "state": "Virginia(VA)", "zip": "24441" } ,
                  { "address": " 13232 Port Republic Rd", "city": "Grottoes", "state": "Virginia(VA)", "zip": "24441" } ,
                  { "address": " 603 13th St", "city": "Grottoes", "state": "Virginia(VA)", "zip": "24441" } ,
                  { "address": " 1203 Randall Rd #B13", "city": "Grottoes", "state": "Virginia(VA)", "zip": "24441" } ,
                  { "address": " 12179 Port Rd", "city": "Grottoes", "state": "Virginia(VA)", "zip": "24441" }]


# It returns the date formatted as YYYYMMDD to be used in the output's file name
def get_date():
	d = str(datetime.date.today())
	s = d.replace('-', '')
	return s

def save_to_file(data):
	date = get_date()
	new_path = os.path.join(os.getcwd(), f'PD_Issuer1_{date}_VA.json')
	print(new_path)
	with open(new_path, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=4)
	print(f'Data generated into this file: PD_Issuer1_{date}_VA.json')

def generate_data(addresses):
    data = []
    for address in addresses:
        address_object =  {
            "address1": f'{address["address"].strip()}',
            "address2": "",
            "city": f"{address['city']}",
            "state": f"VA",
            "postalCode": f"{address['zip']}",
            "coordinates": {
                "lat": 0,
                "lng": 0
            }
        }    
        data.append(address_object)
    save_to_file(data)
    
# we call the function to process the addresses list
generate_data(addresses_list)
