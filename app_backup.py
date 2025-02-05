import os
import sys
import subprocess
import importlib.util
import json
import traceback
import openai
from flask import Flask, request, jsonify

# Configurazione della chiave API di OpenAI (GPT-4)
API_KEY = "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"
client = openai.OpenAI(api_key=API_KEY)

# Percorsi dei file
NIA_MAIN_FILE = "app.py"
BACKUP_FILE = "app_backup.py"

# Inizializzazione Flask
app = Flask(__name__)

# 🔹 Funzione per controllare se un modulo è installato
def is_module_installed(module_name):
    spec = importlib.util.find_spec(module_name)
    return spec is not None

# 🔹 Funzione per installare un modulo mancante
def install_module(module_name):
    print(f"🔹 Installazione del modulo richiesto: {module_name}...")
    subprocess.run([sys.executable, "-m", "pip", "install", module_name])

# 🔹 Funzione per eseguire NIA e catturare errori
def execute_nia():
    try:
        subprocess.run([sys.executable, NIA_MAIN_FILE], check=True)
        return {"status": "success", "message": "NIA eseguita correttamente"}
    except subprocess.CalledProcessError as e:
        error_msg = str(e)
        print(f"⚠️ Errore durante l'esecuzione di NIA:\n{error_msg}")
        return {"status": "error", "message": error_msg}

# 🔹 Funzione per identificare e installare moduli mancanti
def handle_missing_module(error_message):
    missing_module = None
    if "ModuleNotFoundError" in error_message:
        missing_module = error_message.split("'")[1]
    
    if missing_module:
        print(f"⚠️ Modulo mancante rilevato: {missing_module}")
        install_module(missing_module)
        return {"status": "updated", "message": f"Modulo {missing_module} installato con successo!"}
    
    return {"status": "no_update", "message": "Nessun modulo mancante rilevato."}

# 🔹 Funzione per generare codice con GPT-4
def generate_fix_with_gpt4(error_message):
    print("🧠 Richiesta a GPT-4 per correzione codice...")
    
    prompt = f"""
    Ecco il codice Python che ha generato un errore:

    Errore: {error_message}

    Puoi correggere il codice e fornirmi una versione aggiornata e funzionante?
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        fixed_code = response.choices[0].message.content
        return fixed_code
    except Exception as e:
        print(f"❌ Errore nella richiesta a GPT-4: {str(e)}")
        return None

# 🔹 Funzione per modificare automaticamente il codice di NIA
def modify_nia_code():
    print("🛠️ Tentativo di miglioramento automatico di NIA...")

    # 1️⃣ Esegui NIA e cattura l'errore
    execution_result = execute_nia()
    if execution_result["status"] == "success":
        return jsonify({"status": "success", "message": "NIA è già perfettamente funzionante!"})

    error_message = execution_result["message"]

    # 2️⃣ Verifica se l'errore è dovuto a un modulo mancante
    module_fix = handle_missing_module(error_message)
    if module_fix["status"] == "updated":
        return jsonify(module_fix)

    # 3️⃣ Se l'errore è più complesso, tenta di correggere il codice con GPT-4
    print("⚠️ Errore complesso rilevato. Richiedo aiuto a GPT-4...")
    fixed_code = generate_fix_with_gpt4(error_message)

    if fixed_code:
        # Backup del codice originale
        if not os.path.exists(BACKUP_FILE):
            with open(NIA_MAIN_FILE, "r", encoding="utf-8") as f:
                with open(BACKUP_FILE, "w", encoding="utf-8") as f_backup:
                    f_backup.write(f.read())

        # Scrivi il nuovo codice aggiornato
        with open(NIA_MAIN_FILE, "w", encoding="utf-8") as f:
            f.write(fixed_code)

        return jsonify({"status": "updated", "message": "Codice aggiornato con successo grazie a GPT-4!"})

    return jsonify({"status": "error", "message": "Errore critico non risolvibile automaticamente."})

# 🌟 Endpoint Flask per attivare l'auto-evoluzione
@app.route("/evolve", methods=["POST"])
def evolve():
    return modify_nia_code()

# Avvio di NIA
if __name__ == "__main__":
    print("🔹 Avvio NIA in modalità auto-evolutiva...")
    app.run(debug=True)























 









    





































