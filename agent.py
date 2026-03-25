import requests
import json
from datetime import datetime

def get_live_data():
    # Dünya Bankası API'sinden Nijerya Enerji Projelerini çekiyoruz
    url = "https://search.worldbank.org/api/v2/projects?format=json&fl=id,project_name,totalamt,closingdate,status&countrycode_exact=NG&sectortype_exact=Energy"
    
    try:
        response = requests.get(url, timeout=15)
        data = response.json()
        projects = []
        
        # En güncel 3 projeyi listeye ekleyelim
        for p_id in list(data['projects'].keys())[:3]:
            proj = data['projects'][p_id]
            projects.append({
                "n": "YENİ: " + proj['project_name'],
                "t": "Kamu / WB",
                "c": "Abuja",
                "e": "contact@worldbank.org",
                "w": f"projects.worldbank.org/{p_id}",
                "p": 5
            })
        return projects
    except:
        return []

# Robotun bulduğu verileri 'data.json' dosyasına yazdırıyoruz
new_list = get_live_data()
update_info = {
    "last_update": datetime.now().strftime("%d.%m.%Y %H:%M"),
    "projects": new_list
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(update_info, f, ensure_ascii=False, indent=2)

print("Robot görevini tamamladı, verileri dosyaya yazdı.")