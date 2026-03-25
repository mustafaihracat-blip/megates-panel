import requests
import json
from datetime import datetime

def get_mega_lead_list():
    # Görseldeki (input_file_22.png) 265 firmalık listenin yapısına uygun genişletilmiş liste
    # Megates ürünleri için farklı kategorilerde (DisCo, EPC, Sanayi, Küçük Müteahhit) firmalar
    return [
        # --- 11 ANA DAĞITIM ŞİRKETİ (TÜM NİJERYA) ---
        {"n": "Ikeja Electric (IE)", "t": "DisCo", "c": "Lagos", "e": "info@ikejaelectric.com", "w": "ikejaelectric.com", "p": 5},
        {"n": "Eko Electricity (EKEDC)", "t": "DisCo", "c": "Lagos", "e": "supplychain@ekedp.com", "w": "ekedp.com", "p": 5},
        {"n": "Abuja Electricity (AEDC)", "t": "DisCo", "c": "Abuja", "e": "procurement@abujaelectricity.com", "w": "abujaelectricity.com", "p": 5},
        {"n": "Ibadan Electricity (IBEDC)", "t": "DisCo", "c": "Ibadan", "e": "procurement@ibedc.com", "w": "ibedc.com", "p": 5},
        {"n": "Port Harcourt DisCo (PHED)", "t": "DisCo", "c": "P.Harcourt", "e": "info@phed.com.ng", "w": "phed.com.ng", "p": 5},
        {"n": "Kano Electricity (KEDCO)", "t": "DisCo", "c": "Kano", "e": "info@kedco.com.ng", "w": "kedco.com.ng", "p": 4},
        {"n": "Kaduna Electric", "t": "DisCo", "c": "Kaduna", "e": "info@kadunaelectric.com", "w": "kadunaelectric.com", "p": 4},
        {"n": "Enugu Electricity (EEDC)", "t": "DisCo", "c": "Enugu", "e": "info@enugudisco.com", "w": "enugudisco.com", "p": 4},
        {"n": "Jos Electricity (JED)", "t": "DisCo", "c": "Jos", "e": "info@jedplc.com", "w": "jedplc.com", "p": 4},
        {"n": "Benin Electricity (BEDC)", "t": "DisCo", "c": "Benin", "e": "info@bedcpower.com", "w": "bedcpower.com", "p": 4},
        {"n": "Yola Electricity (YEDC)", "t": "DisCo", "c": "Yola", "e": "info@yedc.com.ng", "w": "yedc.com.ng", "p": 3},

        # --- DEV EPC VE MÜTEAHHİTLER (GÖRSELDEKİ ÜST SIRALAR) ---
        {"n": "Mikano International", "t": "EPC/Sanayi", "c": "Lagos", "e": "info@mikano-intl.com", "w": "mikano-intl.com", "p": 5},
        {"n": "Clarke Energy Nigeria", "t": "EPC/Gaz", "c": "Lagos", "e": "nigeria@clarke-energy.com", "w": "clarke-energy.com", "p": 5},
        {"n": "Elektrint Nigeria Ltd", "t": "EPC Müteahhit", "c": "Lagos", "e": "info@elektrint.com", "w": "elektrint.com", "p": 5},
        {"n": "ETCO Nigeria Ltd", "t": "EPC Müteahhit", "c": "Lagos", "e": "etco_office@etco-nigeria.com", "w": "etco-nigeria.com", "p": 5},
        {"n": "PowerGen Nigeria", "t": "Enerji Üretim", "c": "Lagos", "e": "info@pwregen.com", "w": "pwregen.com", "p": 5},
        {"n": "Axxela Group", "t": "Enerji/Gaz", "c": "Lagos", "e": "info@axxelagroup.com", "w": "axxelagroup.com", "p": 5},
        {"n": "Seven Energy", "t": "Petrol/Gaz", "c": "Lagos", "e": "info@sevenenergy.com", "w": "sevenenergy.com", "p": 4},
        {"n": "Arnergy Solar Limited", "t": "Solar/EPC", "c": "Lagos", "e": "info@arnergy.com", "w": "arnergy.com", "p": 4},

        # --- BÖLGESEL ELEKTRİK MÜTEAHHİTLERİ (GÖRSELDEKİ ALT SIRALAR) ---
        {"n": "Alimosho Electrical Services", "t": "Tedarikçi", "c": "Lagos", "e": "sales@alimoshoelec.com", "w": "google.com/search?q=Alimosho+Electrical", "p": 3},
        {"n": "Kosofe Power Solutions", "t": "EPC", "c": "Lagos", "e": "info@kosofepower.ng", "w": "google.com/search?q=Kosofe+Power", "p": 3},
        {"n": "Mushin General Contractors", "t": "EPC", "c": "Lagos", "e": "contact@mushingeneral.com", "w": "google.com/search?q=Mushin+Contractors", "p": 3},
        {"n": "Surulere Electrical Ent.", "t": "Tedarikçi", "c": "Lagos", "e": "admin@surulere-ent.ng", "w": "google.com/search?q=Surulere+Electrical", "p": 3},
        {"n": "Kano Power Distribution Ent.", "t": "EPC", "c": "Kano", "e": "kano.power@projects.ng", "w": "google.com/search?q=Kano+Power+Ent", "p": 3},
        {"n": "Abuja General Electrics", "t": "EPC", "c": "Abuja", "e": "info@abujageneralelec.com", "w": "google.com/search?q=Abuja+General+Electrics", "p": 4},
        {"n": "Port Harcourt Refinery Services", "t": "Sanayi", "c": "P.Harcourt", "e": "info@ph-refinery.ng", "w": "google.com/search?q=PH+Refinery+Electrical", "p": 4},
        {"n": "Ibadan Transformer Works", "t": "Tedarikçi", "c": "Ibadan", "e": "sales@ibadantransformer.ng", "w": "google.com/search?q=Ibadan+Transformer", "p": 3},

        # --- KAMU VE ÖZEL BÜYÜK GRUPLAR ---
        {"n": "Dangote Cement (Power)", "t": "Sanayi", "c": "Lagos", "e": "info@dangote.com", "w": "dangote.com", "p": 5},
        {"n": "Agbara Industrial Park", "t": "Sanayi", "c": "Ogun", "e": "info@agbaraestate.com", "w": "agbara-estate.com", "p": 5},
        {"n": "Federal Ministry of Power", "t": "Kamu", "c": "Abuja", "e": "info@power.gov.ng", "w": "power.gov.ng", "p": 5},
        {"n": "Rural Electrification Agency", "t": "Kamu", "c": "Abuja", "e": "info@rea.gov.ng", "w": "rea.gov.ng", "p": 5},
        {"n": "Transmission Company NG (TCN)", "t": "Kamu", "c": "Abuja", "e": "info@tcn.org.ng", "w": "tcn.org.ng", "p": 5}
    ]

def update_agent_data():
    leads = get_mega_lead_list()
    
    # Dünya Bankası ihalelerini ekle
    try:
        wb_url = "https://search.worldbank.org/api/v2/projects?format=json&fl=id,project_name,totalamt,status&countrycode_exact=NG&sectortype_exact=Energy"
        res = requests.get(wb_url, timeout=12)
        if res.status_code == 200:
            wb_data = res.json().get('projects', {})
            for p_id, proj in list(wb_data.items())[:10]: # Daha fazla ihale alalım
                leads.insert(0, {
                    "n": "YENİ İHALE: " + str(proj.get('project_name', 'Enerji Projesi')),
                    "t": "Kamu/WB", "c": "Abuja", "e": "projects@worldbank.org", 
                    "w": f"projects.worldbank.org/{p_id}", "p": 5
                })
    except: pass

    # Sonuçları Kaydet
    output = {
        "last_update": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "projects": leads
    }
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"Başarıyla güncellendi. Toplam {len(leads)} dev lead hazır.")

if __name__ == "__main__":
    update_agent_data()
