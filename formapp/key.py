### Run this program to get your key.
### Rename file to 'key.py'
### Replace key with the key generated by this file.

key = ''

if key == '':
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    print("Copy and paste this next line into the key variable in 'key.py':")
    print(key)
