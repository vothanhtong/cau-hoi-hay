import re

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
        re.search(r'[^A-Za-z0-9]', password)
    )

def create_account():
    """
    Tạo một tài khoản mới bằng cách nhập tên tài khoản và mật khẩu.
    
    Returns:
        tuple: Tên tài khoản và mật khẩu hợp lệ.
    """
    while True:
        username = input("Nhập tên tài khoản (phải có họ và tên): ").strip()
        password = input("Nhập mật khẩu (ít nhất 8 ký tự, chứa ký tự đặc biệt): ").strip()
        
        if not validate(username, password):
            print("Tên tài khoản hoặc mật khẩu không hợp lệ. Vui lòng thử lại.")
            continue
        
        confirm_password = input("Nhập lại mật khẩu để xác nhận: ").strip()
        if password != confirm_password:
            print("Mật khẩu không khớp. Vui lòng thử lại.")
        else:
            print("Tạo tài khoản thành công!")
            return username, password

def login(username, password):
    """
    Đăng nhập bằng cách kiểm tra tên tài khoản và mật khẩu.
    
    Args:
        username (str): Tên tài khoản đã đăng ký.
        password (str): Mật khẩu đã đăng ký.
    """
    while True:
        entered_username = input("Nhập tên tài khoản: ").strip()
        entered_password = input("Nhập mật khẩu: ").strip()
        
        if entered_username == username and entered_password == password:
            print("Đăng nhập thành công!")
            break
        else:
            print("Sai tài khoản hoặc mật khẩu. Vui lòng thử lại.")

def main():
    """
    Chương trình chính để quản lý tài khoản và đăng nhập.
    """
    print("=== Thiết lập tài khoản ===")
    user, pw = create_account()
    
    print("\n=== Đăng nhập ===")
    login(user, pw)

if __name__ == "__main__":
    main()
