import requests
import json
from datetime import datetime

def regional_scout():
    return [
        {"n": "Ikeja Electric (IE) HQ", "t": "DisCo", "c": "Lagos", "e": "procurement@ikejaelectric.com", "w": "ikejaelectric.com", "p": 5},
        {"n": "Agbara Industrial Park Power", "t": "Sanayi", "c": "Ogun", "e": "info@agbaraindustrial.com", "w": "agbara-estate.com", "p": 5},
        {"n": "Elektrint Nigeria (EPC Contractor)", "t": "EPC Müteahhit", "c": "Lagos", "e": "contact@elektrint.com", "w": "elektrint.com", "p": 5},
        {"n": "Dangote Refinery Power Div.", "t": "Petrol/Gaz", "c": "Lagos", "e": "info@dangote.com", "w": "dangote.com", "p": 5},
        {"n": "Federal Ministry of Power", "t": "Kamu", "c": "Abuja", "e": "info@power.gov.ng", "w": "power.gov.ng", "p": 4},
        {"n": "Eko Electricity Distribution (EKEDC)", "t": "DisCo", "c": "Lagos", "e": "supplychain@ekedp.com", "w": "ekedp.com", "p": 5}
    ]

def update_agent_data():
    leads = regional_scout()
    try:
        wb_url = "https://search.worldbank.org/api/v2/projects?format=json&fl=id,project_name,totalamt,status&countrycode_exact=NG&sectortype_exact=Energy"
        res = requests.get(wb_url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            for p_id in list(data.get('projects', {}).keys())[:5]:
                p = data['projects'][p_id]
                leads.append({
                    "n": "IHALE: " + p.get('project_name', 'Enerji Projesi'),
                    "t": "Kamu/WB", "c": "Abuja", "e": "projects@worldbank.org", "w": f"projects.worldbank.org/{p_id}", "p": 5
                })
    except: pass
    
    output = {"last_update": datetime.now().strftime("%d.%m.%Y %H:%M"), "projects": leads}
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    update_agent_data()
