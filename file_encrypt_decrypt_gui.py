import os
from tkinter import Tk, filedialog, Button, Label
from cryptography.fernet import Fernet

# Carica la chiave dal file secret.key
def load_key():
    if not os.path.exists("secret.key"):
        print("Errore: Il file 'secret.key' non esiste. Genera o imposta una chiave prima di procedere.")
        raise FileNotFoundError("secret.key non trovato")
    return open("secret.key", "rb").read()

# Crittografa un file
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(file_path + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File '{file_path}' crittografato con successo!")

# Decrittografa un file e stampa il contenuto nel terminale
def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    print(f"\nContenuto decrittografato di '{file_path}':\n")
    print(decrypted_data.decode("utf-8"))

# Funzione per selezionare e crittografare un file
def select_file_encrypt():
    file_path = filedialog.askopenfilename(title="Seleziona un file da crittografare")
    if file_path:
        encrypt_file(file_path)

# Funzione per selezionare e decrittografare un file
def select_file_decrypt():
    file_path = filedialog.askopenfilename(title="Seleziona un file da decrittografare")
    if file_path:
        decrypt_file(file_path)

# Interfaccia grafica con Tkinter
def create_gui():
    root = Tk()
    root.title("File Encryption & Decryption Tool")
    root.geometry("400x200")

    Label(root, text="Scegli un'opzione:", font=("Helvetica", 14)).pack(pady=10)
    
    Button(root, text="Crittografa un File", command=select_file_encrypt, width=30).pack(pady=10)
    Button(root, text="Decrittografa un File", command=select_file_decrypt, width=30).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()


