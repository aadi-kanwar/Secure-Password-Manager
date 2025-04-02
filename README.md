# Secure Password Manager

## 🔐 Overview
Secure Password Manager is a simple and secure password storage application built using **Streamlit**. It encrypts stored passwords using **AES (Advanced Encryption Standard) encryption** or **Fernet Encryption** and allows users to manage their credentials securely.

## 🚀 Features
- **User Authentication**: Basic login system with predefined credentials.
- **Password Encryption**: Uses AES-128 encryption with a random IV (Initialization Vector) or FERNET Encryption.
- **Store Passwords**: Save website credentials in an encrypted format.
- **View Saved Passwords**: Display encrypted credentials.
- **Decrypt Passwords**: Option to view decrypted passwords.
- **Delete Password Entries**: Remove saved credentials securely.
- **Persistent Storage**: Saves data in a CSV file.

## 📦 Dependencies
Ensure you have the following Python packages installed:

```basj
pip install streamlit pandas pycryptodome cryptography
```

## 🛠 Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required dependencies using the command above.

## ▶️ Usage
Run the application using Streamlit:

### AES Encryption
```bash
streamlit run app.py
```
### Fernet Encryption
```bash
streamlit run fer.py
```

## 🔑 Encryption Details

- Uses AES-128 encryption (CBC mode) for secure password storage.

- Uses Fernet encryption for an additional security option.

- Generates and stores an encryption key (aes_key.key or fernet_key.key) in the working directory.

- Encrypts passwords with a random IV (for AES) to ensure security.

## 📁 File Structure
```
secure-password-manager/
│── app.py              # AED Encryption
│── fer.py               # FERNET Encryption
│── passwords.csv       # Stores encrypted passwords (generated automatically)
│── aes_key.key         # AES encryption key (generated automatically)
│── fernet_key.key      # Fernet encryption key (generated automatically)
│── README.md           # Documentation
```

## 📝 License
This project is open-source and free to use for personal projects. Modify and improve as needed!

## ✨ Contributing
Feel free to contribute to the project by submitting pull requests or reporting issues.

## 📧 Contact
For any queries or suggestions, feel free to reach out!

---
Enjoy secure password management with this simple and powerful application! 🔒🚀

