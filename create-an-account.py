import re
import bcrypt
from getpass import getpass

def validate(username, password):
    """
    Kiểm tra tính hợp lệ của tên tài khoản và mật khẩu.
    
    Args:
        username (str): Tên tài khoản.
        password (str): Mật khẩu.

    Returns:
        bool: True nếu hợp lệ, False nếu không.
    """
    return (
        len(username.split()) >= 2 and
        len(password) >= 8 and
        re.search(r'[A-Z]', password) and  # Ít nhất một chữ hoa
        re.search(r'[a-z]', password) and  # Ít nhất một chữ thường
        re.search(r'[0-9]', password) and  # Ít nhất một chữ số
        re.search(r'[^A-Za-z0-9]', password)  # Ít nhất một ký tự đặc biệt
    )

def create_account():
    """
    Tạo một tài khoản mới bằng cách nhập tên tài khoản và mật khẩu.
    
    Returns:
        tuple: Tên tài khoản và mật khẩu đã được mã hóa.
    """
    while True:
        username = input("Nhập tên tài khoản (phải có họ và tên): ").strip()
        password = getpass("Nhập mật khẩu (ít nhất 8 ký tự, chứa chữ hoa, chữ thường, số, ký tự đặc biệt): ").strip()
        
        if not validate(username, password):
            print("Tên tài khoản hoặc mật khẩu không hợp lệ. Vui lòng thử lại.")
            continue
        
        confirm_password = getpass("Nhập lại mật khẩu để xác nhận: ").strip()
        if password != confirm_password:
            print("Mật khẩu không khớp. Vui lòng thử lại.")
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            print("Tạo tài khoản thành công!")
            return username, hashed_password

def login(username, hashed_password):
    """
    Đăng nhập bằng cách kiểm tra tên tài khoản và mật khẩu.
    
    Args:
        username (str): Tên tài khoản đã đăng ký.
        hashed_password (bytes): Mật khẩu đã được mã hóa.
    """
    attempts = 0
    max_attempts = 3  # Giới hạn số lần thử đăng nhập
    
    while attempts < max_attempts:
        entered_username = input("Nhập tên tài khoản: ").strip()
        entered_password = getpass("Nhập mật khẩu: ").strip()
        
        if entered_username == username and bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password):
            print("Đăng nhập thành công!")
            return True
        else:
            attempts += 1
            print(f"Sai tài khoản hoặc mật khẩu. Bạn còn {max_attempts - attempts} lần thử.")
    
    print("Bạn đã vượt quá số lần thử đăng nhập.")
    return False

def main():
    """
    Chương trình chính để quản lý tài khoản và đăng nhập.
    """
    print("=== Thiết lập tài khoản ===")
    user, hashed_pw = create_account()
    
    print("\n=== Đăng nhập ===")
    login(user, hashed_pw)

if __name__ == "__main__":
    main()
#                                                                                   bai 2 



    import re
import bcrypt
from getpass import getpass

users_db = {}  # Cơ sở dữ liệu đơn giản lưu tên tài khoản và mật khẩu mã hóa

def validate(username, password):
    """
    Kiểm tra tính hợp lệ của tên tài khoản và mật khẩu.
    
    Args:
        username (str): Tên tài khoản.
        password (str): Mật khẩu.

    Returns:
        bool: True nếu hợp lệ, False nếu không.
    """
    return (
        len(username.split()) >= 2 and
        len(password) >= 8 and
        re.search(r'[A-Z]', password) and  # Ít nhất một chữ hoa
        re.search(r'[a-z]', password) and  # Ít nhất một chữ thường
        re.search(r'[0-9]', password) and  # Ít nhất một chữ số
        re.search(r'[^A-Za-z0-9]', password)  # Ít nhất một ký tự đặc biệt
    )

def create_account():
    """
    Tạo một tài khoản mới.
    """
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
    """
    Đăng nhập vào hệ thống.
    """
    attempts = 0
    max_attempts = 3  # Giới hạn số lần thử đăng nhập
    
    while attempts < max_attempts:
        entered_username = input("Nhập tên tài khoản: ").strip()
        entered_password = getpass("Nhập mật khẩu: ").strip()
        
        if entered_username in users_db and bcrypt.checkpw(entered_password.encode('utf-8'), users_db[entered_username]):
            print("Đăng nhập thành công!")
            return True
        else:
            attempts += 1
            print(f"Sai tài khoản hoặc mật khẩu. Bạn còn {max_attempts - attempts} lần thử.")
    
    print("Bạn đã vượt quá số lần thử đăng nhập.")
    return False

def show_users():
    """
    Hiển thị danh sách tài khoản (chỉ minh họa, không hiển thị mật khẩu).
    """
    print("\n=== Danh sách tài khoản ===")
    for username in users_db.keys():
        print(f"- {username}")
    print("==========================\n")

def main():
    """
    Chương trình chính để quản lý nhiều tài khoản.
    """
    while True:
        print("\n=== Hệ thống quản lý tài khoản ===")
        print("1. Tạo tài khoản mới")
        print("2. Đăng nhập")
        print("3. Xem danh sách tài khoản")
        print("4. Thoát")
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == "1":
            create_account()
        elif choice == "2":
            if login():
                print("Chào mừng bạn đến với hệ thống!")
        elif choice == "3":
            show_users()
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
