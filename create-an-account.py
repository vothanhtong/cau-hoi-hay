import re

# Hàm kiểm tra tên tài khoản (phải có ít nhất hai từ, tức là họ và tên)
def validate_username(username):
    return len(username.split()) >= 2

# Hàm kiểm tra mật khẩu (phải có ít nhất một ký tự đặc biệt)
def validate_password(password):
    return bool(re.search(r'[^A-Za-z0-9]', password))

# Hàm tạo tài khoản
def create_account():
    while True:
        username = input("Nhập tên tài khoản (phải có họ và tên): ")
        if not validate_username(username):
            print("Tên tài khoản phải có họ và tên. Vui lòng nhập lại.")
            continue

        password = input("Nhập mật khẩu (phải có ký tự đặc biệt): ")
        if not validate_password(password):
            print("Mật khẩu phải chứa ít nhất một ký tự đặc biệt. Vui lòng nhập lại.")
            continue
        
        print("Tài khoản và mật khẩu đã được thiết lập thành công.")
        return username, password

# Hàm đăng nhập
def login(username, password):
    while True:
        input_username = input("Nhập tên tài khoản: ")
        input_password = input("Nhập mật khẩu: ")
        
        if input_username == username and input_password == password:
            print("Bạn đã nhập thành công.")
            break
        else:
            print("Tài khoản hoặc mật khẩu không đúng. Vui lòng thử lại.")

# Chạy chương trình
if __name__ == "__main__":
    print("Thiết lập tài khoản")
    username, password = create_account()
    
    input("Nhấn Enter để tiến hành đăng nhập...")
    
    print("Đăng nhập")
    login(username, password)
