from werkzeug.security import generate_password_hash,check_password_hash

pwd =input("Enter your password : ")
generated_pwd = generate_password_hash(pwd)
print(generated_pwd)

reenterpwd =input("Enter re-enter your password : ")
isValid = check_password_hash(generated_pwd,reenterpwd)
if isValid:
    print("Access Granted")
else:
    print("Access not granted")    
