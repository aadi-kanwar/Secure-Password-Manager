# import streamlit as st
# import pandas as pd
# from cryptography.fernet import Fernet
# import os

# CSV_FILE = "passwords.csv"
# KEY_FILE = "fernet_key.key"

# # Function to get or create an encryption key
# def get_encryption_key():
#     if os.path.exists(KEY_FILE):
#         with open(KEY_FILE, "rb") as key_file:
#             return key_file.read()
#     else:
#         key = Fernet.generate_key()
#         with open(KEY_FILE, "wb") as key_file:
#             key_file.write(key)
#         return key

# # Load the encryption key
# SECRET_KEY = get_encryption_key()
# fernet = Fernet(SECRET_KEY)

# # Function to encrypt a password
# def encrypt_password(password):
#     return fernet.encrypt(password.encode()).decode()

# # Function to decrypt a password
# def decrypt_password(encrypted_password):
#     try:
#         return fernet.decrypt(encrypted_password.encode()).decode()
#     except Exception as e:
#         return f"Decryption Error: {str(e)}"

# # Load passwords from CSV
# def load_passwords():
#     if os.path.exists(CSV_FILE):
#         return pd.read_csv(CSV_FILE)
#     return pd.DataFrame(columns=["Website", "Username", "Password"])

# # Save passwords to CSV
# def save_passwords(df):
#     df.to_csv(CSV_FILE, index=False)

# # Main UI
# def main_ui():
#     st.title("🔑 Secure Password Manager")
    
#     # Load existing passwords
#     df = load_passwords()
    
#     # Add new password
#     st.subheader("➕ Add New Password")
#     website = st.text_input("Website")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
    
#     if st.button("Save Password"):
#         if website and username and password:
#             encrypted_password = encrypt_password(password)
#             new_entry = pd.DataFrame([[website, username, encrypted_password]], columns=["Website", "Username", "Password"])
#             df = pd.concat([df, new_entry], ignore_index=True)
#             save_passwords(df)
#             st.success("Password saved successfully!")
#         else:
#             st.error("Please fill all fields")
    
#     # Show saved passwords
#     st.subheader("📋 Saved Passwords")
#     if not df.empty:
#         df_display = df.copy()
#         df_display["Password"] = "🔒 Encrypted"
#         st.dataframe(df_display)
        
#         # Delete password entry
#         st.subheader("🗑️ Delete Password")
#         selected_index = st.selectbox("Select an entry to delete", df.index)
        
#         if st.button("Delete Selected Entry"):
#             df = df.drop(index=selected_index).reset_index(drop=True)
#             save_passwords(df)
#             st.success("Password entry deleted successfully!")
        
#         # Decrypt and show passwords
#         if st.button("🔓 Show Decrypted Passwords"):
#             df["Password"] = df["Password"].apply(decrypt_password)
#             st.dataframe(df)
#     else:
#         st.write("No passwords saved yet.")

# # Login Page
# def login():
#     st.title("🔐 Secure Password Manager - Login")
    
#     # Predefined credentials
#     USERNAME = "admin"
#     PASSWORD = "password123"
    
#     # Session state to track login
#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
    
#     # Login form
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
    
#     if st.button("Login"):
#         if username == USERNAME and password == PASSWORD:
#             st.session_state.logged_in = True
#             st.success("Login successful! Redirecting...")
#             st.rerun()
#         else:
#             st.error("Invalid username or password")

# # Check login state and navigate
# if st.session_state.get("logged_in", False):
#     main_ui()
# else:
#     login()




import streamlit as st
import pandas as pd
from cryptography.fernet import Fernet
import os

CSV_FILE = "passwords.csv"
KEY_FILE = "fernet_key.key"

# Function to get or create an encryption key
def get_encryption_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return key

# Load the encryption key
SECRET_KEY = get_encryption_key()
fernet = Fernet(SECRET_KEY)

# Function to encrypt a password
def encrypt_password(password):
    return fernet.encrypt(password.encode()).decode()

# Function to decrypt a password
def decrypt_password(encrypted_password):
    try:
        return fernet.decrypt(encrypted_password.encode()).decode()
    except Exception as e:
        return f"Decryption Error: {str(e)}"

# Load passwords from CSV
def load_passwords():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    return pd.DataFrame(columns=["Website", "Username", "Password"])

# Save passwords to CSV
def save_passwords(df):
    df.to_csv(CSV_FILE, index=False)

# Main UI
def main_ui():
    st.title("🔑 Secure Password Manager")
    
    # Load existing passwords
    df = load_passwords()
    
    # Add new password
    st.subheader("➕ Add New Password")
    website = st.text_input("Website")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Save Password"):
        if website and username and password:
            encrypted_password = encrypt_password(password)
            new_entry = pd.DataFrame([[website, username, encrypted_password]], columns=["Website", "Username", "Password"])
            df = pd.concat([df, new_entry], ignore_index=True)
            save_passwords(df)
            st.success("Password saved successfully!")
        else:
            st.error("Please fill all fields")
    
    # Show saved passwords
    st.subheader("📋 Saved Passwords")
    if not df.empty:
        df_display = df.copy()
        df_display["Password"] = "🔒 Encrypted"
        
        for i, row in df.iterrows():
            col1, col2, col3, col4 = st.columns([3, 3, 3, 1])
            col1.write(row["Website"])
            col2.write(row["Username"])
            col3.write("🔒 Encrypted")
            if col4.button("🗑️", key=f"delete_{i}"):
                df = df.drop(index=i).reset_index(drop=True)
                save_passwords(df)
                st.rerun()
        
        # Decrypt and show passwords
        if st.button("🔓 Show Decrypted Passwords"):
            df_display["Password"] = df["Password"].apply(decrypt_password)
            st.write(df_display)
    else:
        st.write("No passwords saved yet.")

# Login Page
def login():
    st.title("🔐 Secure Password Manager - Login")
    
    # Predefined credentials
    USERNAME = "admin"
    PASSWORD = "password123"
    
    # Session state to track login
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    # Login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful! Redirecting...")
            st.rerun()
        else:
            st.error("Invalid username or password")

# Check login state and navigate
if st.session_state.get("logged_in", False):
    main_ui()
else:
    login()