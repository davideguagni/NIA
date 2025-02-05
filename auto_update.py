import subprocess
import sys
import os
import time

def check_and_update_packages():
    """Controlla e aggiorna automaticamente le librerie necessarie"""
    print("🔹 Controllo aggiornamenti librerie...")
    required_packages = [
        "openai", "flask", "torch", "opencv-python", "numpy", 
        "speechrecognition", "vosk", "pyautogui", "pygetwindow",
        "python-docx", "openpyxl", "python-pptx", "pywin32", "pyttsx3"
    ]
    
    for package in required_packages:
        try:
            print(f"🔍 Verifica aggiornamenti per {package}...")
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package], check=True)
            print(f"✅ {package} aggiornato con successo!")
        except subprocess.CalledProcessError:
            print(f"⚠️ Errore nell'aggiornamento di {package}")

def restart_nia():
    """Riavvia automaticamente NIA dopo l'aggiornamento"""
    print("🔄 Riavvio di NIA in corso...")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def auto_update():
    """Controlla aggiornamenti, aggiorna e riavvia"""
    check_and_update_packages()
    print("🚀 Aggiornamento completato. Riavvio del sistema...")
    time.sleep(2)
    restart_nia()
