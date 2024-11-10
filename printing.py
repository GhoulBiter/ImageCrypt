import os


def PrintTimeStats(start, end, msg="Stats"):
    # print(f"{msg} >>> Time Started: {start} ; Time Finished: {end} ; Time Taken Overall: {end - start}")
    print(f"{msg} >>>")
    print(f"Unix Time Started:  {start}")
    print(f"Unix Time Finished: {end}")
    print(f"Time Taken Overall: {end - start}")


def ListFilesInOriginalsDirectory():
    dirPath = os.path.join(os.getcwd(), "img\original")
    filesInDirectory = os.listdir(dirPath)
    filePaths = []

    counter = 1

    print(">>> Displaying files in the Originals Directory")
    for item in filesInDirectory:
        if os.path.isfile(os.path.join(dirPath, item)):
            print(f"{counter}: {item}")
            filePaths.append(os.path.join(dirPath, item))
            counter += 1

    return filePaths


def ListFilesInEncryptedDirectory():
    dirPath = os.path.join(os.getcwd(), "img\encrypted")
    filesInDirectory = os.listdir(dirPath)
    filePaths = []

    counter = 1

    print(">>> Displaying files in the Encrypted Files' Directory")
    if len(filesInDirectory) == 0:
        print("No files in the Encrypted Files' Directory")
        return []

    for item in filesInDirectory:
        if os.path.isfile(os.path.join(dirPath, item)):
            print(f"{counter}: {item}")
            filePaths.append(os.path.join(dirPath, item))
            counter += 1

    return filePaths


def ListFilesInDecryptedDirectory():
    dirPath = os.path.join(os.getcwd(), "img\decrypted")
    filesInDirectory = os.listdir(dirPath)
    filePaths = []

    counter = 1

    print(">>> Displaying files in the Decrypted Files' Directory")
    if len(filesInDirectory) == 0:
        print("No files in the Decrypted Files' Directory")
        return []

    for item in filesInDirectory:
        if os.path.isfile(os.path.join(dirPath, item)):
            print(f"{counter}: {item}")
            filePaths.append(os.path.join(dirPath, item))
            counter += 1

    return filePaths


def DisplayPublicPrivateKeys():
    print("Not currently implemented")


def PrintMOTD():
    motd = """
 █████ ██████   ██████   █████████       █████████                                  █████                      
░░███ ░░██████ ██████   ███░░░░░███     ███░░░░░███                                ░░███                       
 ░███  ░███░█████░███  ███     ░░░     ███     ░░░  ████████  █████ ████ ████████  ███████    ██████  ████████ 
 ░███  ░███░░███ ░███ ░███            ░███         ░░███░░███░░███ ░███ ░░███░░███░░░███░    ███░░███░░███░░███
 ░███  ░███ ░░░  ░███ ░███    █████   ░███          ░███ ░░░  ░███ ░███  ░███ ░███  ░███    ░███ ░███ ░███ ░░░ 
 ░███  ░███      ░███ ░░███  ░░███    ░░███     ███ ░███      ░███ ░███  ░███ ░███  ░███ ███░███ ░███ ░███     
 █████ █████     █████ ░░█████████     ░░█████████  █████     ░░███████  ░███████   ░░█████ ░░██████  █████    
░░░░░ ░░░░░     ░░░░░   ░░░░░░░░░       ░░░░░░░░░  ░░░░░       ░░░░░███  ░███░░░     ░░░░░   ░░░░░░  ░░░░░     
                                                               ███ ░███  ░███                                  
                                                              ░░██████   █████                                 
                                                               ░░░░░░   ░░░░░                                  
"""
    print()
    print(motd)
    # print()
