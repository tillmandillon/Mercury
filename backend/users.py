from passlib.context import CryptContext
pwd_context=CryptContext(schemes=["pbkdf2_sha256"],default="pbkdf2_sha256",pbkdf2_sha256__default_rounds=30000)

def get_hash(password):
    return pwd_context.encrypt(password)
    
def verify_password(password,_hash):
    return pwd_context.verify(password,_hash)