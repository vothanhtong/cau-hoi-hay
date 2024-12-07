# Dưới đây là phiên bản rút gọn và tối ưu của mã nguồn:

import re

# Kiểm tra tài khoản (ít nhất 2 từ) và mật khẩu (ít nhất 8 ký tự, chứa ký tự đặc biệt)
def validate(username, password):
    return len(username.split()) >= 2 and len(password) >= 8 and re.search(r'[^A-Za-z0-9]', password)

# Tạo tài khoản
def create_account():
    while True:
        username = input("Nhập tên tài khoản (phải có họ và tên): ")
        password = input("Nhập mật khẩu (ít nhất 8 ký tự, chứa ký tự đặc biệt): ")
        if validate(username, password):
            if password == input("Nhập lại mật khẩu để xác nhận: "):
                print("Tạo tài khoản thành công.")
                return username, password
            else:
                print("Mật khẩu không khớp. Vui lòng thử lại.")
        else:
            print("Tên tài khoản hoặc mật khẩu không hợp lệ. Vui lòng thử lại.")

# Đăng nhập
def login(username, password):
    while input("Nhập tên tài khoản: ") != username or input("Nhập mật khẩu: ") != password:
        print("Sai tài khoản hoặc mật khẩu. Vui lòng thử lại.")
    print("Đăng nhập thành công.")

# Chương trình chính
if __name__ == "__main__":
    print("Thiết lập tài khoản")
    user, pw = create_account()
    print("\nĐăng nhập")
    login(user, pw)


### Điểm tối ưu:
# 1. **Gộp logic**: Hàm `validate` kiểm tra đồng thời cả tên tài khoản và mật khẩu để tránh lặp code.
# 2. **Rút gọn thông báo lỗi**: Sử dụng thông báo chung khi tên tài khoản hoặc mật khẩu không hợp lệ.
# 3. **Giảm nhập liệu không cần thiết**: Tránh lặp lại nhập và kiểm tra trong từng bước riêng lẻ.
# 4. **Cấu trúc ngắn gọn**: Giữ nguyên chức năng nhưng code được trình bày đơn giản hơn.