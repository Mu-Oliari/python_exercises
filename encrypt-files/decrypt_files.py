from cryptography.fernet import Fernet

# get key from file
file = open('key.key', 'rb')
key = file.read()
file.close()

# decrypt message
f2 = Fernet(key)
decrypted = decrypted = f2.decrypt(encrypted)

# decode message
original_message = decrypted.decode()
print(original_message)