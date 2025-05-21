<h1 align="center"> DES Encrypt / Decrypt Website</h1>
##  Mô tả

Website đơn giản dùng thuật toán **DES (Data Encryption Standard)** để mã hóa và giải mã file. Giao diện người dùng thân thiện, dễ sử dụng.

## Tính năng

- Chọn file để mã hóa hoặc giải mã.
- Nhập khóa chính xác 8 ký tự (DES yêu cầu 64-bit key).
- Tự động xử lý mã hóa hoặc giải mã khi nhấn nút tương ứng.

##  Công nghệ sử dụng

- Python (Flask)
- HTML / CSS (Bootstrap)
- PyCryptodome (để xử lý mã hóa DES)

##  Giao diện người dùng

<p align="center">
  <img src="Screenshot 2025-05-21 164117.png" alt="DES Encrypt Decrypt UI" width="500"/>
</p>

##  Cách chạy dự án

```bash
git clone https://github.com/your-username/your-repo.git
cd DES_Website
pip install -r requirements.txt
python app.py
