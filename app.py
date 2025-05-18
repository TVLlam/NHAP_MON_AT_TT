import os
from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from Crypto.Cipher import DES
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "secretkey"
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def pad(data):
    return data + b' ' * (8 - len(data) % 8)

def unpad(data):
    return data.rstrip(b' ')

def des_encrypt(data, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.encrypt(pad(data))

def des_decrypt(data, key):
    des = DES.new(key, DES.MODE_ECB)
    return unpad(des.decrypt(data))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files['file']
        key = request.form['key']

        if not file or key == '':
            flash("Missing file or key")
            return redirect(request.url)

        if len(key) != 8:
            flash("Key phải đúng 8 ký tự.")
            return redirect(request.url)

        action = request.form['action']
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        with open(filepath, 'rb') as f:
            data = f.read()

        key_bytes = key.encode('utf-8')

        if action == 'encrypt':
            processed_data = des_encrypt(data, key_bytes)
            output_filename = 'encrypted_' + filename
        else:
            try:
                processed_data = des_decrypt(data, key_bytes)
            except:
                flash("Giải mã thất bại. Sai khóa hoặc dữ liệu.")
                return redirect(request.url)
            output_filename = 'decrypted_' + filename

        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        with open(output_path, 'wb') as f:
            f.write(processed_data)

        return send_file(output_path, as_attachment=True)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
