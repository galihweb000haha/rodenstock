from cryptography.fernet import Fernet

fernet_key = Fernet.generate_key()
fernet = Fernet(fernet_key)

class Security():
    def encrypt_data(data):
        return fernet.encrypt(data.encode()).decode()
    
    def decrypt_data(encrypted_data):
        return fernet.decrypt(encrypted_data.encode()).decode()