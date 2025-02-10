from flask import Flask, render_template, request, send_file
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

app = Flask(__name__)

# Generate a random 16-byte key and IV (You can store and reuse it securely)
KEY = os.urandom(16)
IV = os.urandom(16)

def encrypt_image(image_data):
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(IV), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad data to be a multiple of block size (AES block size is 16 bytes)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(image_data) + padder.finalize()
    
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return IV + encrypted_data  # Prepend IV for decryption

def decrypt_image(encrypted_data):
    iv = encrypted_data[:16]  # Extract IV
    encrypted_content = encrypted_data[16:]
    
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(encrypted_content) + decryptor.finalize()
    
    # Remove padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()
    
    return decrypted_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.files['image']
    encrypted_data = encrypt_image(file.read())
    encrypted_path = 'encrypted_image.enc'
    with open(encrypted_path, 'wb') as enc_file:
        enc_file.write(encrypted_data)
    return send_file(encrypted_path, as_attachment=True)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    file = request.files['encrypted_image']
    decrypted_data = decrypt_image(file.read())
    decrypted_path = 'decrypted_image.png'
    with open(decrypted_path, 'wb') as dec_file:
        dec_file.write(decrypted_data)
    return send_file(decrypted_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
