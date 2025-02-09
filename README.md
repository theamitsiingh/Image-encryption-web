# 🔐 Image Encryption Web App

Protect your images with **AES encryption** using this simple yet powerful web-based app! Easily encrypt and decrypt images right from your browser.

## 🚀 Features
- 🔒 **Secure AES Encryption** for images
- 📥 Upload and encrypt images
- 📤 Download encrypted files
- 🔓 Decrypt encrypted images with ease
- 🎨 User-friendly web interface

## 🛠️ Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL
- **Encryption:** AES (Advanced Encryption Standard)

## 🔧 Installation Guide

### Prerequisites
- Python 3
- pip (Python package manager)
- MySQL database

### Setup Instructions
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/theamitsiingh/Image-encryption-web
   cd image-encryption-app
   ```

2. **Install Dependencies:**
   ```sh
   pip install flask cryptography
   ```

3. **Set Up the Database:**
   - Import the `database.sql` file into MySQL:
     ```sh
     mysql -u your_user -p your_password < database.sql
     ```
   - Update the Flask app to connect to your database if needed.

4. **Run the Application:**
   ```sh
   python app.py
   ```

5. **Access the Web Interface:**
   - Open `http://127.0.0.1:5000/` in your browser.

## 📂 File Structure
```
image-encryption-app/
│── app.py             # Flask backend
│── templates/
│   └── index.html     # Frontend UI
│── static/
│   └── styles.css     # (Optional) CSS file for styling
│── database.sql       # SQL file for database setup
│── README.md          # Project documentation
```

## 🎯 How to Use
1. **Encrypt an Image:**
   - Click **Choose File** to select an image.
   - Click **Encrypt** to process the image.
   - Download the encrypted file.

2. **Decrypt an Image:**
   - Click **Choose File** to upload an encrypted image.
   - Click **Decrypt** to restore the original image.
   - Download the decrypted file.

## 🤝 Contribute
Want to make this project even better? Fork it, improve it, and send a pull request!

## 📜 License
This project is licensed under the **MIT License**. Feel free to use and modify it as you like.

🚀 **Protect your images today with AES encryption!** 🔐


