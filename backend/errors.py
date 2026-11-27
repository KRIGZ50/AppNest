
import json


class AppError(Exception):
    status_code = None
    error_msg = None
    
    
class EmailTaken(AppError):
    status_code = 409
    error_msg = "Email taken! Try another Email address"  

class NameTaken(AppError):
    status_code = 409
    error_msg = "Username exists"
    
class EmailUnverified(AppError):
    status_code = 403
    error_msg = "Email Not verified"

class ExpiredToken(AppError):
    error_msg = "Token Expired"
    
class InvalidCredentials(AppError):
    status_code = 401
    error_msg = "Invalid Username or Password"
    
class InvalidVerificationCode(AppError):
    status_code = 400
    error_msg = "Invalid or expired verification code"
        
        
def error_handler(error):
    
    error_data = {"status code": error.status_code, "error msg": error.error_msg}
    return json.dumps(error_data)

