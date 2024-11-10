# ImageCrypt (Image Encryption and Decryption Tool)

This project is a command-line tool designed for secure encryption and decryption of image files using AES and RSA algorithms. It provides a menu-driven interface that enables users to list images, encrypt and decrypt images, and view RSA key pairs. The project is built in Python and uses the Python Imaging Library (PIL) for handling image files.

## Features

- **List Images**: Displays available images in the original, encrypted, and decrypted directories.
- **RSA Encryption and Decryption**: Encrypt and decrypt images using RSA with automatic key generation and storage.
- **AES Encryption and Decryption**: Encrypt and decrypt images using AES with password-based encryption.
- **Display RSA Key Pairs**: View generated RSA public and private keys.
- **Time Statistics**: Provides time statistics for each operation, including file handling and encryption/decryption.

## Dependencies

- **Python 3.11.9**: This is the Python version used for developing and testing this tool. While other versions may work, it is not guaranteed to be the case.
- **PIL (Python Imaging Library)**: For loading and processing image files.
- **PyCryptodome**: For AES and RSA encryption.

A `requirements.txt` file is provided to enable easy installation using `pip install -r requirements.txt`.

## Usage

1. **Run the main script**:

    ``` bash
    python main.py
    ```

2. **Menu Options**:
   - **Option 1-3**: List files in the Original, Encrypted, or Decrypted directories.
   - **Option 4**: Show generated RSA public and private keys.
   - **Option 5**: Encrypt or decrypt images with AES.
   - **Option 6**: Encrypt or decrypt images with RSA.
   - **Option 7**: Exit the tool.

3. **AES and RSA Encryption/Decryption**:
   - Follow on-screen prompts to select files and enter encryption keys.
   - The tool will ask if you’d like to view the decrypted image upon successful decryption.

## Important Notes

- **File Paths**: Ensure the `img` and `secrets` directories are set up as required by the program.
- **Key Management**: RSA key pairs are saved in the `secrets` folder for future decryption; AES uses a password-based key derived from SHA-256 and a random salt.
- **Error Handling**: Basic input validation and error messages are included; further validation may be necessary in production.

## Future Enhancements

- **Improved Error Handling**: To validate inputs and handle incorrect keys.
- **Logging**: Record encryption and decryption operations in a log file.
- **User Interface**: Optionally, a GUI could replace the command-line interface for ease of use.
- **Additional Encryption Algorithms**: Support for other encryption modes or algorithms, like GCM for AES.

## License

This project is open-source and licensed under the MIT License.
