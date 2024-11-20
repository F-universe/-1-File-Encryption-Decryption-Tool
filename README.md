This project is a simple and secure file encryption and decryption tool built using Python. 
It is composed of two scripts: set_key.py, which is used to generate and store a custom encryption key,
and file_encrypt_decrypt_gui.py, which provides a graphical interface to encrypt and decrypt text files 
using the saved key. The core functionality relies on the powerful cryptography library, specifically the
Fernet module, which provides high-level encryption and decryption functionality while maintaining data 
integrity.

The shorter script, set_key.py, is responsible for creating a custom key and saving it in a file named
secret.key. The user is prompted to input a 32-character key, which is then converted into the format
required by the Fernet module. If the input does not meet the required length, an error message is displayed, 
and the key is not saved. This script ensures that a unique key can be generated and securely stored for future
encryption and decryption processes.

The longer script, file_encrypt_decrypt_gui.py, provides a user-friendly graphical interface to select files 
for encryption or decryption. When encrypting, the script reads the file, encrypts its content using the key
stored in secret.key, and saves the result as a new file with the .encrypted extension. For decryption,
the script reads the encrypted file, decrypts its content using the same key, and displays the decrypted
content directly in the terminal. This ensures that both encryption and decryption processes are tied to
the secure key stored in secret.key.

The main library used in this project is the cryptography library, which is widely recognized for its ease of
use and robust security features. Specifically, the Fernet module provides symmetric encryption and decryption,
which means the same key is used for both processes.
This ensures data integrity and guarantees that the data cannot be tampered with or accessed without the correct key. 
Additionally, the project uses the tkinter library to create a simple and intuitive graphical user interface,
making it easy for non-technical users to interact with the tool. The os library is also utilized to manage files
and check for the existence of the key file.

Overall, this project is designed to securely handle text files by encrypting them with a custom key and
decrypting them only when the correct key is provided. By combining the functionality of set_key.py and
file_encrypt_decrypt_gui.py, users can manage their data securely and efficiently, with the assurance
that the cryptographic processes are robust and reliable.
