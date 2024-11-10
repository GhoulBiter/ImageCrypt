from PIL import Image
from aes import useAES
from rsa import useRSA
from printing import (
    ListFilesInOriginalsDirectory,
    ListFilesInEncryptedDirectory,
    ListFilesInDecryptedDirectory,
    DisplayPublicPrivateKeys,
    PrintMOTD,
)


# Initialise options
options_home = {
    1: "List Files in the 'Original Images' Directory",
    2: "List Files in the 'Encrypted Images' Directory",
    3: "List Files in the 'Decrypted Images' Directory",
    4: "Show Generated RSA Public and Private Key Pairs",
    5: "Encrypt or Decrypt using AES",
    6: "Encrypt or Decrypt using RSA",
    7: "Exit",
}

options_directory = {}

options_encryption_aes = {
    1: "Select an Image to Encrypt",
    2: "Set Default Secret Key (this is for development only)",
    3: "Display Default Secret Key (this is for development only)",
}
options_decryption_aes = {
    1: "Select an Image to Decrypt",
    2: "Set Default Secret Key (this is for development only)",
    3: "Display Default Secret Key (this is for development only)",
}
options_selection_aes = {
    # Fill this with options of image names in the current directory
}

options_encryption_rsa = {}


def printSelectionScreen():
    print()
    print("Select an option to proceed:")

    for item in options_home:
        print(f"{item}: {options_home[item]}")

    print()
    selection = input("> ")

    while True:
        try:
            selection = int(selection)
            break
        except:
            continue

    selectionFunctions = {
        1: ListFilesInOriginalsDirectory,
        2: ListFilesInEncryptedDirectory,
        3: ListFilesInDecryptedDirectory,
        4: DisplayPublicPrivateKeys,
        5: useAES,
        6: useRSA,
        7: exit,
    }

    selectionFunctions[selection]()

    input("Press any key to continue...")
    printSelectionScreen()


if __name__ == "__main__":
    PrintMOTD()
    printSelectionScreen()
