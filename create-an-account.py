import re
import bcrypt
import json
import time
from getpass import getpass

# Hằng số
MAX_ATTEMPTS = 3
LOCK_DURATION = 30  # Thời gian khóa tài khoản (giây)
DATABASE_FILE = "users_db.json"

# Load dữ liệu từ tệp JSON
def load_users():
    try:
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Lưu dữ liệu vào tệp JSON
def save_users(users):
    with open(DATABASE_FILE, "w") as file:
        json.dump(users, file)

# Dữ liệu người dùng
users_db = load_users()
login_attempts = {}

def validate_password(password):
    """Kiểm tra tính hợp lệ của mật khẩu và gợi ý các yêu cầu chưa đạt."""
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

def create_account():
    """Tạo tài khoản mới."""
    while True:
        username = input("Nhập tên tài khoản (phải có họ và tên): ").strip()
        if username in users_db:
            print("Tên tài khoản đã tồn tại. Vui lòng thử tên khác.")
            continue
        
        password = getpass("Nhập mật khẩu: ").strip()
        errors = validate_password(password)
        if errors:
            print("Mật khẩu không hợp lệ:")
            for error in errors:
                print(f"- {error}")
            continue
        
        confirm_password = getpass("Nhập lại mật khẩu để xác nhận: ").strip()
        if password != confirm_password:
            print("Mật khẩu không khớp. Vui lòng thử lại.")
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            users_db[username] = {"password": hashed_password, "locked_until": 0}
            save_users(users_db)
            print("Tạo tài khoản thành công!")
            break

def login():
    """Đăng nhập vào hệ thống."""
    username = input("Nhập tên tài khoản: ").strip()
    if username not in users_db:
        print("Tài khoản không tồn tại.")
        return False

    user_data = users_db[username]
    if time.time() < user_data["locked_until"]:
        remaining_time = int(user_data["locked_until"] - time.time())
        print(f"Tài khoản đang bị khóa. Vui lòng thử lại sau {remaining_time} giây.")
        return False

    attempts = login_attempts.get(username, 0)
    while attempts < MAX_ATTEMPTS:
        password = getpass("Nhập mật khẩu: ").strip()
        if bcrypt.checkpw(password.encode('utf-8'), user_data["password"].encode('utf-8')):
            print("Đăng nhập thành công!")
            login_attempts.pop(username, None)
            return True
        else:
            attempts += 1
            login_attempts[username] = attempts
            print(f"Sai mật khẩu. Bạn còn {MAX_ATTEMPTS - attempts} lần thử.")
    
    users_db[username]["locked_until"] = time.time() + LOCK_DURATION
    save_users(users_db)
    print("Bạn đã vượt quá số lần thử. Tài khoản bị khóa tạm thời.")
    return False

def change_password():
    """Đổi mật khẩu cho tài khoản đã đăng nhập."""
    username = input("Nhập tên tài khoản của bạn: ").strip()
    if username not in users_db:
        print("Tài khoản không tồn tại.")
        return

    old_password = getpass("Nhập mật khẩu cũ: ").strip()
    if bcrypt.checkpw(old_password.encode('utf-8'), users_db[username]["password"].encode('utf-8')):
        new_password = getpass("Nhập mật khẩu mới: ").strip()
        errors = validate_password(new_password)
        if errors:
            print("Mật khẩu mới không hợp lệ:")
            for error in errors:
                print(f"- {error}")
            return
        
        confirm_password = getpass("Nhập lại mật khẩu mới để xác nhận: ").strip()
        if new_password == confirm_password:
            users_db[username]["password"] = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            save_users(users_db)
            print("Đổi mật khẩu thành công!")
        else:
            print("Mật khẩu mới không khớp.")
    else:
        print("Sai mật khẩu cũ.")

def show_users(admin_key):
    """Hiển thị danh sách tài khoản (chỉ quản trị viên mới có quyền)."""
    if admin_key == "admin123":
        print("\n=== Danh sách tài khoản ===")
        for username in users_db.keys():
            print(f"- {username}")
        print("==========================\n")
    else:
        print("Bạn không có quyền truy cập chức năng này.")

def delete_account(admin_key):
    """Xóa tài khoản (chỉ quản trị viên mới có quyền)."""
    if admin_key == "admin123":
        username = input("Nhập tên tài khoản cần xóa: ").strip()
        if username in users_db:
            del users_db[username]
            save_users(users_db)
            print(f"Đã xóa tài khoản: {username}")
        else:
            print("Tài khoản không tồn tại.")
    else:
        print("Bạn không có quyền thực hiện chức năng này.")

def main():
    """Chương trình chính."""
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
            admin_key = getpass("Nhập khóa quản trị viên: ").strip()
            show_users(admin_key)
        elif choice == "5":
            admin_key = getpass("Nhập khóa quản trị viên: ").strip()
            delete_account(admin_key)
        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
