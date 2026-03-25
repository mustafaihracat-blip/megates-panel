import requests
import json
from datetime import datetime

def regional_scout():
    # Megates ürünlerine (Beton Köşk, Hücre, Pano) en uygun bölgesel hedefler
    # Bu liste robotun Nijerya pazarında öncelikli taradığı kurumları temsil eder
    targets = [
        {"n": "Ikeja Electric (IE) HQ", "t": "DisCo", "c": "Lagos", "e": "procurement@ikejaelectric.com", "w": "ikejaelectric.com", "p": 5},
        {"n": "Agbara Industrial Park Power", "t": "Sanayi", "c": "Ogun", "e": "info@agbaraindustrial.com", "w": "agbara-estate.com", "p": 5},
        {"n": "Elektrint Nigeria (EPC Contractor)", "t": "EPC Müteahhit", "c": "Lagos", "e": "contact@elektrint.com", "w": "elektrint.com", "p": 5},
        {"n": "Dangote Refinery Power Div.", "t": "Petrol/Gaz", "c": "Lagos", "e": "info@dangote.com", "w": "dangote.com", "p": 5},
        {"n": "Federal Ministry of Power", "t": "Kamu", "c": "Abuja", "e": "info@power.gov.ng", "w": "power.gov.ng", "p": 4},
        {"n": "Eko Electricity Distribution (EKEDC)", "t": "DisCo", "c": "Lagos", "e": "supplychain@ekedp.com", "w": "ekedp.com", "p": 5}
    ]
    return targets

def update_agent_data():
    # Mevcut bölgesel hedefleri al
    leads = regional_scout()
    
    # Dünya Bankası ihalelerini (Nijerya Enerji Sektörü) çek
    wb_url = "https://search.worldbank.org/api/v2/projects?format=json&fl=id,project_name,totalamt,status&countrycode_exact=NG&sectortype_exact=Energy"
    try:
        wb_res = requests.get(wb_url, timeout=10).json()
        if 'projects' in wb_res:
            for p_id in list(wb_res['projects'].keys())[:5]:
                proj = wb_res['projects'][p_id]
                leads.append({
                    "n": "YENİ İHALE: " + proj['project_name'],
                    "t": "Kamu/WB", 
                    "c": "Abuja", 
                    "e": "projects@worldbank.org", 
                    "w": f"projects.worldbank.org/{p_id}", 
                    "p": 5
                })
    except Exception as e:
        print(f"Hata oluştu: {e}")

    # Verileri hazırla
    data = {
        "last_update": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "projects": leads
    }
    
    # data.json dosyasını güncelle
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Başarıyla güncellendi. Toplam {len(leads)} lead bulundu.")

if __name__ == "__main__":
    update_agent_data()
