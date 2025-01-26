# from getpass import getpass
# password = getpass("Nhập mật khẩu: ")
# def is_valid_username(username):
#     return re.match(r'^[a-zA-Z0-9_-]{3,20}$', username) is not None
# if not is_valid_username(username):
#     print("Tên đăng nhập không hợp lệ. Chỉ được chứa chữ cái, số, dấu gạch ngang (-) và gạch dưới (_).")
#     return
# # ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'user';
# failed_attempts = {}  # Lưu số lần thất bại
# def login(username, password):
#     if failed_attempts.get(username, 0) >= 3:
#         print("Tài khoản đã bị khóa tạm thời. Vui lòng thử lại sau.")
#         return False

#     # Tiếp tục logic đăng nhập...
#     if bcrypt.checkpw(password.encode('utf-8'), stored_password):
#         failed_attempts[username] = 0  # Reset đếm thất bại
#         return True
#     else:
#         failed_attempts[username] = failed_attempts.get(username, 0) + 1
#         return False
# with sqlite3.connect("users.db") as conn:
#     cursor = conn.cursor()
#     # Thực hiện các thao tác...
# === Hệ Thống Đăng Nhập ===
# 1. Đăng ký
# 2. Đăng nhập
# 3. Cập nhật mật khẩu
# 4. Xóa tài khoản
# 5. Hiển thị danh sách người dùng (Admin)
# 6. Thoát
# Chọn chức năng (1-6): 2

# Nhập tên đăng nhập: admin
# Nhập mật khẩu: ********
# Đăng nhập thành công!
