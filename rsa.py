from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from printing import ListFilesInOriginalsDirectory, ListFilesInEncryptedDirectory, PrintTimeStats
import ntpath
import os
from PIL import Image
import time

def setToDecryptionMode():
    """Handles user input for choosing the operation mode

    Returns:
        bool: False if encrypt, True if decrypt
    """

    choice = False

    print()
    print("Do you want to decrypt a file (By default this is set to encrypt)? Y/N")
    selection = input("> ")

    if selection.lower() == 'y':
        choice = True

    return choice


def generate_keys(key_size):
    # Generate RSA key pair of given key size
    key = RSA.generate(key_size)

    # Print the public and private keys to the terminal
    # print(f"Public key:  (n={hex(key.n)}, e={hex(key.e)})")
    # print(f"Private key: (n={hex(key.n)}, d={hex(key.d)})")

    return key

def encrypt_chunk(chunk, key):
    # Encrypt the chunk with RSA
    cipher_rsa = PKCS1_OAEP.new(key)
    encrypted_chunk = cipher_rsa.encrypt(chunk)
    return encrypted_chunk

def decrypt_chunk(encrypted_chunk, key):
    # Decrypt the chunk with RSA
    cipher_rsa = PKCS1_OAEP.new(key)
    chunk = cipher_rsa.decrypt(encrypted_chunk)
    return chunk


def DecryptImageRSA(input_path, output_path, key):
    # Decrypt each chunk with RSA
    with open(input_path, 'rb') as input_file:
        with open(output_path, 'wb') as output_file:
            chunk_size = key.size_in_bytes() - 42
            while True:
                encrypted_chunk = input_file.read(key.size_in_bytes())
                if not encrypted_chunk:
                    break
                decrypted_chunk = decrypt_chunk(encrypted_chunk, key)
                output_file.write(decrypted_chunk)


def EncryptImageRSA(input_path, output_path, key):
    # Split the image file into smaller chunks and encrypt each chunk with RSA
    chunk_size = key.size_in_bytes() - 42
    with open(input_path, 'rb') as input_file:
        with open(output_path, 'wb') as output_file:
            while True:
                chunk = input_file.read(chunk_size)
                if not chunk:
                    break
                encrypted_chunk = encrypt_chunk(chunk, key.publickey())
                output_file.write(encrypted_chunk)



def useRSA():
        # Checking whether to proceed with encryption or whether the user wants to decrypt instead
    option = setToDecryptionMode()

    # Getting the file path for the file intended to be encrypted / decrypted
    print()
    print(">>> Select an item below to proceed")
    if option == True:
        listOfFiles = ListFilesInEncryptedDirectory()
    else:
        listOfFiles = ListFilesInOriginalsDirectory()

    print()
    selection = input("> ")

    while True:
        try:
            selection = int(selection)
            break
        except:
            continue
    
    # Selecting the file and generating the key object
    image_file = listOfFiles[selection - 1]
    keyPairObject = generate_keys(2048)

    # Adjusting prefix of name for output path
    if option == True:
        outputFile = os.path.join(os.getcwd(), "img\decrypted", "decrypted_" + ntpath.basename(image_file))
    else:
        outputFile = os.path.join(os.getcwd(), "img\encrypted", "encrypted_" + ntpath.basename(image_file))


    # Carrying out the operation accordingly
    if option == True:
        startTimeFile = time.time()
        # Decryption can't be done straightforwardly, data about the private key needs to be loaded from a file that may or may not exist first :)

        publicKeyFileName = ""
        # If this is true then this file has corresponding private and public key PEM files in the secrets folder, so decryption is possible
        for filename in os.listdir(os.path.join(os.getcwd(), "secrets")):
            if ntpath.basename(image_file) in filename:
                publicKeyFileName = filename
                break
        

        if publicKeyFileName != "":
            with open(os.path.join(os.getcwd(), "secrets", filename), 'rb') as privateKeyFile:
                privateKey = RSA.import_key(privateKeyFile.read())
            endTimeFile = time.time()

            startTimeDec = time.time()
            DecryptImageRSA(image_file, outputFile, privateKey)
            endTimeDec = time.time()

            print()
            print("Operation Completed")
            PrintTimeStats(startTimeDec, endTimeDec, "Stats for Encryption")
            PrintTimeStats(startTimeFile, endTimeFile, "Stats for File IO OP")

            print()
            print(">>> Show Image? Y/N")
            selection = input("> ").lower()

            if selection == 'y':
                with Image.open(outputFile) as img:
                    img.show()
        else:
            print("Chosen file has no associated private key generated, please encrypt it properly using RSA first, then proceed with decryption.")
    else:
        # The image is encrypted using the public key component stored in the keyPairObject variable
        startTimeEnc = time.time()
        EncryptImageRSA(image_file, outputFile, keyPairObject)
        endTimeEnc = time.time()

        #! DEBUG
        # print(os.path.join(os.getcwd(), "secrets", "encrypted_" + ntpath.basename(image_file)))
        
        startTimeFile = time.time()
        basePath = os.path.join(os.getcwd(), "secrets", "encrypted_" + ntpath.basename(image_file))

        # The information on the public and private keys is written to separate files in the 'secrets' folder, this allows the program to know if a file can be decrypted or not when decrypting later on
        with open(basePath + '_private.pem', 'wb') as secretsFile:
            secretsFile.write(keyPairObject.exportKey())
        
        with open(basePath + '_public.pem', 'wb') as secretsFile:
            secretsFile.write(keyPairObject.publickey().exportKey())
        endTimeFile = time.time()
        
        print()
        print("Operation Completed")
        PrintTimeStats(startTimeEnc, endTimeEnc, "Stats for Encryption")
        PrintTimeStats(startTimeFile, endTimeFile, "Stats for File IO OP")


