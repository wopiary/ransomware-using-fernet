from cryptography.fernet import Fernet
import os 
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


secretKeyFileName = 'fernetKey.txt'
fileName = input('Enter file path: ')
filePath = fileName.replace('C', 'c').replace('\\', '/').replace('"', '')


def createKeyFile():
    os.system('cls' if os.name=='nt' else 'clear')

    if not os.path.exists:
        key = Fernet.generate_key()
        with open(secretKeyFileName, 'rb') as keyFile:
            keyFile.write(key)
            print('Key generated and saved.')
    else:
        key = Fernet.generate_key()
        with open(secretKeyFileName, 'wb') as keyFile:
            keyFile.write(key)
            print('Key rewritten, generated, and saved.')
    return key


def encryptKey():
    global encryptedData, originalData, key
    key = createKeyFile()
    fernet = Fernet(key)

    with open(filePath, 'rb') as file:
        originalData = file.read()
    encryptedData = fernet.encrypt(originalData)

    with open(filePath, 'wb') as file:
        file.write(encryptedData)
    print('File encrypted successfully.')    


def loadKey():
    return open(secretKeyFileName, 'rb').read()

def decryptKey():
    os.system('cls' if os.name=='nt' else 'clear')
    key = loadKey()
    if key is None:
        return
    fernet = Fernet(key)

    with open(filePath, 'rb') as file:
        encryptedData = file.read()
        decryptedData = fernet.decrypt(encryptedData)
    
    with open(filePath, 'wb') as file:
        file.write(decryptedData)
        print('File decrypted successfully.')

def displayMessage():
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror('Horse', "Don't worry there's no Greeks here")
    userInput = simpledialog.askstring('Input', 'Key: ')
    if userInput == key.decode():
        decryptKey()
    else:
        messagebox.showerror(':))', 'uh oh.')
        return displayMessage()

createKeyFile()
encryptKey()
displayMessage()



