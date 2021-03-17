from cryptography.fernet import Fernet

key = Fernet.generate_key()
# get key from file
file = open('key.key', 'rb')
key = file.read()
file.close()

# encode message
message = 'my little message!'
encoded = message.encode()

# encrypt message
f = Fernet(key)
encrypted = f.encrypt(encoded)