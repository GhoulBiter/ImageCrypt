from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Hash import SHA256
from PIL import Image
import os
from printing import ListFilesInOriginalsDirectory, ListFilesInEncryptedDirectory, PrintTimeStats
import ntpath
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


def derive_key(key, salt):
    # Use SHA256 to derive a 32-byte key from the input key
    h = SHA256.new(key)
    h.update(salt)
    return h.digest()


def encrypt_image(input_file, output_file, key):
    # Generate a salt randomly
    salt = os.urandom(16)

    # Derive a key from the input key using SHA256
    derived_key = derive_key(key, salt)

    # Read the input image data
    with open(input_file, 'rb') as f:
        input_data = f.read()

    # Generate an initialization vector (IV) randomly
    iv = os.urandom(16)

    # Create an AES cipher object with the derived key and IV
    cipher = AES.new(derived_key, AES.MODE_CBC, iv)

    # Pad the input data so that it's a multiple of 16 bytes
    padded_data = input_data + b"\0" * (16 - len(input_data) % 16)

    # Encrypt the padded data using AES-CBC mode
    encrypted_data = iv + cipher.encrypt(padded_data)

    # Write the salt and encrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(salt)
        f.write(encrypted_data)


def decrypt_image(input_file, output_file, key):
    # Read the salt and encrypted data from the input file
    with open(input_file, 'rb') as f:
        salt = f.read(16)
        encrypted_data = f.read()

    # Derive a key from the input key and salt using SHA256
    derived_key = derive_key(key, salt)

    # Extract the IV from the encrypted data
    iv = encrypted_data[:16]

    # Create an AES cipher object with the derived key and IV
    cipher = AES.new(derived_key, AES.MODE_CBC, iv)

    # Decrypt the encrypted data using AES-CBC mode
    decrypted_data = cipher.decrypt(encrypted_data[16:])

    # Remove the padding from the decrypted data
    unpadded_data = decrypted_data.rstrip(b"\0")

    # Write the decrypted data to the output file
    with open(output_file, 'wb') as f:
        f.write(unpadded_data)



def useAES(path: str = None, secret: str = None, display: bool = False):
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

    # Getting the secret key to be used from the user
    print()
    print(">>> Choose the password / secret / key to be used:")

    secret = input("> ")

    # Read the image file
    image_file = listOfFiles[selection - 1]

    # Read the secret key
    secret_key = secret.encode()

    # Adjusting prefix of name for output path
    if option == True:
        outputFile = os.path.join(os.getcwd(), "img\decrypted", "decrypted_" + ntpath.basename(image_file))
    else:
        outputFile = os.path.join(os.getcwd(), "img\encrypted", "encrypted_" + ntpath.basename(image_file))


    # Carrying out the operation accordingly
    if option == True:
        startTime = time.time()
        decrypt_image(image_file, outputFile, secret_key)
        endTime = time.time()

        print()
        print("Operation Completed")
        PrintTimeStats(startTime, endTime)

        print()
        print(">>> Show Image? Y/N")
        selection = input("> ").lower()

        if selection == 'y':
            try:
                with Image.open(outputFile) as img:
                    img.show()
            except Exception:
                print("Image could not be opened because it was decrypted incorrectly. Check the key you used, most likely the fault is there!")
    else:
        startTime = time.time()
        encrypt_image(image_file, outputFile, secret_key)
        endTime = time.time()

        print()
        print("Operation Completed")
        PrintTimeStats(startTime, endTime)

