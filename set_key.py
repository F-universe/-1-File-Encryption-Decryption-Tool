from cryptography.fernet import Fernet
import base64

def set_custom_key():
    user_key = input("Inserisci una chiave personalizzata (32 caratteri): ").strip()
    
    if len(user_key) != 32:
        print("Errore: La chiave deve essere lunga esattamente 32 caratteri.")
        return
    
    # Converti la chiave personalizzata in formato base64 richiesto da Fernet
    key = base64.urlsafe_b64encode(user_key.encode())
    
    # Salva la chiave in secret.key
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Chiave personalizzata salvata con successo in 'secret.key'.")

if __name__ == "__main__":
    set_custom_key()
