import re
import bcrypt
import json
import time
import logging
from getpass import getpass
from contextlib import contextmanager

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Hằng số
MAX_ATTEMPTS = 3
LOCK_DURATION = 30  # Thời gian khóa tài khoản (giây)
DATABASE_FILE = "users_db.json"
ADMIN_KEY = bcrypt.hashpw(b"admin123", bcrypt.gensalt()).decode('utf-8')  # Khóa quản trị viên đã mã hóa

# Quản lý mở/đóng tệp JSON
@contextmanager
def open_db():
    try:
        with open(DATABASE_FILE, "r") as file:
            yield json.load(file)
    except FileNotFoundError:
        yield {}

# Load dữ liệu từ tệp JSON
def load_users():
    with open_db() as db:
        return db

# Lưu dữ liệu vào tệp JSON
def save_users(users):
    with open(DATABASE_FILE, "w") as file:
        json.dump(users, file, indent=4)

# Kiểm tra tính hợp lệ của mật khẩu
def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Mật khẩu phải có ít nhất 8 ký tự.")
    if not re.search(r'[A-Z]', password):
        errors.append("Mật khẩu phải chứa ít nhất một chữ cái viết hoa.")
    if not re.search(r'[a-z]', password):
        errors.append("Mật khẩu phải chứa ít nhất một chữ cái viết thường.")
    if not re.search(r'[0-9]', password):
        errors.append("Mật khẩu phải chứa ít nhất một chữ số.")
    if not re.search(r'[^A-Za-z0-9]', password):
        errors.append("Mật khẩu phải chứa ít nhất một ký tự đặc biệt.")
    return errors

# Tạo tài khoản mới
def create_account():
    while True:
        username = input("Nhập tên tài khoản: ").strip()
        if username in users_db:
            logging.warning("Tên tài khoản đã tồn tại. Vui lòng thử tên khác.")
            continue
        
        password = getpass("Nhập mật khẩu: ").strip()
        errors = validate_password(password)
        if errors:
            logging.warning("Mật khẩu không hợp lệ:")
            for error in errors:
                logging.warning(f"- {error}")
            continue
        
        confirm_password = getpass("Nhập lại mật khẩu để xác nhận: ").strip()
        if password != confirm_password:
            logging.warning("Mật khẩu không khớp. Vui lòng thử lại.")
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            users_db[username] = {"password": hashed_password, "locked_until": 0}
            save_users(users_db)
            logging.info("Tạo tài khoản thành công!")
            break

# Đăng nhập
def login():
    username = input("Nhập tên tài khoản: ").strip()
    if username not in users_db:
        logging.warning("Tài khoản không tồn tại.")
        return False

    user_data = users_db[username]
    if time.time() < user_data["locked_until"]:
        remaining_time = int(user_data["locked_until"] - time.time())
        logging.warning(f"Tài khoản đang bị khóa. Vui lòng thử lại sau {remaining_time} giây.")
        return False

    attempts = 0
    while attempts < MAX_ATTEMPTS:
        password = getpass("Nhập mật khẩu: ").strip()
        if bcrypt.checkpw(password.encode('utf-8'), user_data["password"].encode('utf-8')):
            logging.info("Đăng nhập thành công!")
            return True
        else:
            attempts += 1
            logging.warning(f"Sai mật khẩu. Bạn còn {MAX_ATTEMPTS - attempts} lần thử.")
    
    users_db[username]["locked_until"] = time.time() + LOCK_DURATION
    save_users(users_db)
    logging.warning("Bạn đã vượt quá số lần thử. Tài khoản bị khóa tạm thời.")
    return False

# Đổi mật khẩu
def change_password():
    username = input("Nhập tên tài khoản của bạn: ").strip()
    if username not in users_db:
        logging.warning("Tài khoản không tồn tại.")
        return

    old_password = getpass("Nhập mật khẩu cũ: ").strip()
    if bcrypt.checkpw(old_password.encode('utf-8'), users_db[username]["password"].encode('utf-8')):
        new_password = getpass("Nhập mật khẩu mới: ").strip()
        errors = validate_password(new_password)
        if errors:
            logging.warning("Mật khẩu mới không hợp lệ:")
            for error in errors:
                logging.warning(f"- {error}")
            return
        
        confirm_password = getpass("Nhập lại mật khẩu mới để xác nhận: ").strip()
        if new_password == confirm_password:
            users_db[username]["password"] = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            save_users(users_db)
            logging.info("Đổi mật khẩu thành công!")
        else:
            logging.warning("Mật khẩu mới không khớp.")
    else:
        logging.warning("Sai mật khẩu cũ.")

# Hiển thị danh sách tài khoản (chỉ quản trị viên)
def show_users():
    admin_key = getpass("Nhập khóa quản trị viên: ").strip()
    if bcrypt.checkpw(admin_key.encode('utf-8'), ADMIN_KEY.encode('utf-8')):
        logging.info("\n=== Danh sách tài khoản ===")
        for username in users_db.keys():
            logging.info(f"- {username}")
        logging.info("==========================\n")
    else:
        logging.warning("Bạn không có quyền truy cập chức năng này.")

# Xóa tài khoản (chỉ quản trị viên)
def delete_account():
    admin_key = getpass("Nhập khóa quản trị viên: ").strip()
    if bcrypt.checkpw(admin_key.encode('utf-8'), ADMIN_KEY.encode('utf-8')):
        username = input("Nhập tên tài khoản cần xóa: ").strip()
        if username in users_db:
            del users_db[username]
            save_users(users_db)
            logging.info(f"Đã xóa tài khoản: {username}")
        else:
            logging.warning("Tài khoản không tồn tại.")
    else:
        logging.warning("Bạn không có quyền thực hiện chức năng này.")

# Chương trình chính
def main():
    global users_db
    users_db = load_users()

    while True:
        print("\n=== Hệ thống quản lý tài khoản ===")
        print("1. Tạo tài khoản mới")
        print("2. Đăng nhập")
        print("3. Đổi mật khẩu")
        print("4. Xem danh sách tài khoản (chỉ dành cho quản trị viên)")
        print("5. Xóa tài khoản (chỉ dành cho quản trị viên)")
        print("6. Thoát")
        choice = input("Chọn chức năng (1-6): ").strip()
        
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            change_password()
        elif choice == "4":
            show_users()
        elif choice == "5":
            delete_account()
        elif choice == "6":
            logging.info("Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            logging.warning("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()