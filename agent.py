import requests
import json
from datetime import datetime

def scout_market():
    discovery_leads = [
        {"n": "Ikeja Electric (IE) HQ", "t": "DisCo", "c": "Lagos", "e": "procurement@ikejaelectric.com", "w": "ikejaelectric.com", "p": 5},
        {"n": "Elektrint Nigeria (EPC)", "t": "EPC Müteahhit", "c": "Lagos", "e": "contact@elektrint.com", "w": "elektrint.com", "p": 5},
        {"n": "Dangote Refinery Power Div.", "t": "Petrol/Gaz", "c": "Lagos", "e": "info@dangote.com", "w": "dangote.com", "p": 5},
        {"n": "Agbara Estate Power Unit", "t": "Sanayi", "c": "Ogun", "e": "info@agbaraindustrial.com", "w": "agbara-estate.com", "p": 4}
    ]
    try:
        url = "https://search.worldbank.org/api/v2/projects?format=json&fl=id,project_name,totalamt,status&countrycode_exact=NG&sectortype_exact=Energy"
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            projects = res.json().get('projects', {})
            for p_id in list(projects.keys())[:3]:
                p = projects[p_id]
                discovery_leads.append({
                    "n": "YENI IHALE: " + str(p.get('project_name', 'Enerji Projesi')),
                    "t": "Kamu/WB", "c": "Abuja", "e": "wb@projects.org", "w": f"projects.worldbank.org/{p_id}", "p": 5
                })
    except: pass
    return discovery_leads

if __name__ == "__main__":
    found_leads = scout_market()
    data = {"last_update": datetime.now().strftime("%d.%m.%Y %H:%M"), "projects": found_leads}
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Robot isi bitirdi.")