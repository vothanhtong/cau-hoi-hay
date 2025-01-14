import re
import bcrypt
from getpass import getpass

# Hằng số
MAX_ATTEMPTS = 3
users_db = {}  # Cơ sở dữ liệu đơn giản lưu tài khoản và mật khẩu mã hóa

def validate(username, password):
    """Kiểm tra tính hợp lệ của tên tài khoản và mật khẩu."""
    return (
        len(username.split()) >= 2 and
        len(password) >= 8 and
        re.search(r'[A-Z]', password) and  # Ít nhất một chữ hoa
        re.search(r'[a-z]', password) and  # Ít nhất một chữ thường
        re.search(r'[0-9]', password) and  # Ít nhất một chữ số
        re.search(r'[^A-Za-z0-9]', password)  # Ít nhất một ký tự đặc biệt
    )

def create_account():
    """Tạo tài khoản mới."""
    while True:
        username = input("Nhập tên tài khoản (phải có họ và tên): ").strip()
        if username in users_db:
            print("Tên tài khoản đã tồn tại. Vui lòng thử tên khác.")
            continue
        
        password = getpass("Nhập mật khẩu (ít nhất 8 ký tự, chứa chữ hoa, chữ thường, số, ký tự đặc biệt): ").strip()
        if not validate(username, password):
            print("Tên tài khoản hoặc mật khẩu không hợp lệ. Vui lòng thử lại.")
            continue
        
        confirm_password = getpass("Nhập lại mật khẩu để xác nhận: ").strip()
        if password != confirm_password:
            print("Mật khẩu không khớp. Vui lòng thử lại.")
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            users_db[username] = hashed_password
            print("Tạo tài khoản thành công!")
            break

def login():
    """Đăng nhập vào hệ thống."""
    attempts = 0
    
    while attempts < MAX_ATTEMPTS:
        entered_username = input("Nhập tên tài khoản: ").strip()
        entered_password = getpass("Nhập mật khẩu: ").strip()
        
        if entered_username in users_db and bcrypt.checkpw(entered_password.encode('utf-8'), users_db[entered_username]):
            print("Đăng nhập thành công!")
            return True
        else:
            attempts += 1
            print(f"Sai tài khoản hoặc mật khẩu. Bạn còn {MAX_ATTEMPTS - attempts} lần thử.")
    
    print("Bạn đã vượt quá số lần thử đăng nhập.")
    return False

def show_users(admin_key):
    """Hiển thị danh sách tài khoản (chỉ quản trị viên mới có quyền)."""
    if admin_key == "admin123":  # Khóa quản trị đơn giản
        print("\n=== Danh sách tài khoản ===")
        for username in users_db.keys():
            print(f"- {username}")
        print("==========================\n")
    else:
        print("Bạn không có quyền truy cập chức năng này.")

def main():
    """Chương trình chính để quản lý nhiều tài khoản."""
    while True:
        print("\n=== Hệ thống quản lý tài khoản ===")
        print("1. Tạo tài khoản mới")
        print("2. Đăng nhập")
        print("3. Xem danh sách tài khoản (chỉ dành cho quản trị viên)")
        print("4. Thoát")
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == "1":
            create_account()
        elif choice == "2":
            if login():
                print("Chào mừng bạn đến với hệ thống!")
        elif choice == "3":
            admin_key = getpass("Nhập khóa quản trị viên: ").strip()
            show_users(admin_key)
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
