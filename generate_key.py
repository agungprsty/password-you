import os
import base64
import bcrypt

flask_key = base64.urlsafe_b64encode(os.urandom(32)).decode("utf-8") 
fernet_key = base64.urlsafe_b64encode(os.urandom(32)).decode("utf-8") 
hash_salt = bcrypt.gensalt().decode("utf-8")

print(f'FLASK_KEY : {flask_key}')
print(f'FERNET_KEY : {fernet_key}')
print(f'HASH_SALT : {hash_salt}')
