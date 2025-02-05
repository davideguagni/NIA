import os
import subprocess
import sys

SOFTWARE_URLS = {
    "Unreal Engine 5": "https://store.epicgames.com/en-US/download",
    "MetaHuman Creator": "https://www.unrealengine.com/metahuman-creator",
    "Blender": "https://www.blender.org/download/",
    "Photoshop": "https://www.adobe.com/products/photoshop/free-trial-download.html"
}

def is_software_installed(software_name):
    """Controlla se un software è già installato nel sistema"""
    try:
        subprocess.run(["where", software_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def download_and_install(software_name):
    """Scarica ed installa il software richiesto"""
    if software_name in SOFTWARE_URLS:
        print(f"🔹 {software_name} non è installato. Download in corso...")
        url = SOFTWARE_URLS[software_name]
        print(f"🌐 Scarica manualmente da: {url}")
        print(f"🛠 Dopo l'installazione, riavvia NIA per completare la configurazione.")
    else:
        print(f"❌ Software {software_name} non riconosciuto.")

def check_and_install_software():
    """Verifica la presenza dei software principali e li installa se mancanti"""
    required_software = ["Unreal Engine 5", "MetaHuman Creator", "Blender", "Photoshop"]

    for software in required_software:
        if not is_software_installed(software):
            download_and_install(software)
        else:
            print(f"✅ {software} è già installato.")

if __name__ == "__main__":
    check_and_install_software()
