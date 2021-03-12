from cryptography.fernet import Fernet
encryption='br-CL2E7iL6Fqfebzx20K7krE0hak9DIBUM_SDlWHmE='
f = Fernet(encryption)
filename='hashing.py'
with open(filename, "rb") as file:
	file_data = file.read()
	encrypted_data = f.encrypt(file_data)
with open(filename+'crypt', "wb") as file:
	file.write(encrypted_data)