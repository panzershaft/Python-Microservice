from cryptography.fernet import Fernet

"""
Second service from here, will take the key and 
the encrypted file from Service1 and decrypt xml to a new file. 
NOTE: this key and encrypted files are passed using docker volumes
"""


def script_runner2():
    key = open("secret_key.key", "rb").read()
    f = Fernet(key)

    # decrypt the encrypted file
    with open("encrypted_xml.xml", "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open("decrypted.xml", "wb") as file:
        file.write(decrypted_data)
    print('Yess, I guess one can say that it worked')

if __name__ == '__main__':
    script_runner2()
