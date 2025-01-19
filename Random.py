import random

# Danh sách các tên
names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Isaac", "Jack"]

# Hàm để tạo tên ngẫu nhiên
def generate_random_names(num_names):
    return random.sample(names, min(num_names, len(names)))

# Nhập số lượng tên từ người dùng
num = int(input("Nhập số lượng tên bạn muốn tạo: "))

# Gọi hàm và in ra kết quả
random_names = generate_random_names(num)
print("Các tên ngẫu nhiên:", random_names)
