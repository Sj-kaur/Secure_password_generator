SECURE = (('s', '$'), ('and', '&'), 
            ('a', '@'), ('o', '0'), ('i', '!'),
            ('I', '|') , ('H', '#')) 


def secure_password(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password

if __name__ == "__main__":
    pass_input = input("Enterthe password: \n")
    print("Your new secured password is: \n", secure_password(pass_input))
