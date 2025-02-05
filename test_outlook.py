import win32com.client

try:
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)  # 0 indica un'email normale
    mail.To = "esempio@email.com"
    mail.Subject = "Test invio email"
    mail.Body = "Questo è un test di invio email da Python."
    
    # Usa .Display() per mostrare la mail prima di inviarla
    mail.Display()
    
    # Usa .Send() per inviare direttamente
    # mail.Send()
    
    print("Email creata con successo!")
except Exception as e:
    print(f"Errore: {e}")
