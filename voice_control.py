import unreal
import speech_recognition as sr

def recognize_speech():
    """
    Riconosce comandi vocali per controllare il MetaHuman in Unreal Engine.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Parla ora per controllare il MetaHuman...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="it-IT")
        print(f"🎙 Comando riconosciuto: {command}")

        if "cammina" in command:
            apply_animation("MH_Example", "WalkCycle")
        elif "saluta" in command:
            apply_animation("MH_Example", "Wave")
        elif "fermati" in command:
            apply_animation("MH_Example", "Idle")
        else:
            print("❌ Comando non riconosciuto.")
    except sr.UnknownValueError:
        print("❌ Non ho capito il comando.")
    except sr.RequestError:
        print("❌ Errore nel riconoscimento vocale.")

# Test manuale: recognize_speech()

