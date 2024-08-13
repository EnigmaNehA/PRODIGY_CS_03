import re

def strength_of_password(password):

    is_strong = True
    feedback = []

    if len(password) < 10:
        feedback.append("Password muxt contain atleast 10 characters. \n")
        is_strong = False

    if not re.search(r'[a-z]',password):
        feedback.append("Password must contain atleast 1 lowercase. \n")
        is_strong = False

    if not re.search(r'[A-Z]',password):
        feedback.append("Password must contain atleast 1 UPPERCASE. \n")
        is_strong = False

    if not re.search(r'[0-9]',password):
        feedback.append("Password must contain atleast 1 numerical character. \n")
        is_strong = False

    if not re.search(r'[!@#$%^&*()_+:"|<>?~`]' , password):
        feedback.append("Password must contain atleast 1 special character. \n")
        is_strong = False

    if re.search(r'(.)\1{2,}', password):
        feedback.append("Password must not contain three or more consecutive identical characters.")
        is_strong = False

    common_patterns = [r'123456', r'password', r'123456789', r'12345678', r'12345', r'qwerty', 
        r'abc123', r'password1', r'123123', r'admin', r'welcome', r'1234', 
        r'password123', r'qwertyuiop', r'letmein', r'monkey', r'sunshine', 
        r'123321', r'qwerty123', r'1q2w3e4r5t', r'123', r'password1', 
        r'football', r'iloveyou', r'123123123', r'admin123', r'dragon', 
        r'winner', r'password1', r'qwerty1']
    if any(re.search(pattern, password, re.IGNORECASE) for pattern in common_patterns):
        feedback.append("Password contains common patterns or words. Choose a more secure password.\n")
        is_strong = False

    if is_strong:
        print("The password meets all the Requirements.")
    else:
        print("Please follow the instructions carefully and choose a more secure password." +'\n'.join(feedback))

password = input("Enter the password to check its strength : ")
strength_of_password(password)
