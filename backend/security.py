import bcrypt
import hashlib
import hmac
import secrets

####        HASHING       ####

def pass_hashing(password):
    
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

def token_hashing(token):
    
    hashed = hashlib.sha256(token.encode()).hexdigest()
    return hashed


####    COMPARING     ####

def verify(password, stored_hash):
    return bcrypt.checkpw(password.encode(), stored_hash.encode())   
        
        
def verify(token, stored_hash):
    
    return hmac.compare_digest(
        hashlib.sha256(token.encode()).hexdigest(),
        stored_hash
    )
    
    
#### TOKEN GENERATION  ####

def get_token():
    return secrets.token_urlsafe(32)
