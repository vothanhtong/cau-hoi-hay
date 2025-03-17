import random

# Danh sách các tên ban đầu (sẽ được người dùng nhập)
names = set()

# Hàm để tạo tên ngẫu nhiên
def generate_random_names(num_names):
    return random.sample(names, min(num_names, len(names)))

# Hàm hiển thị danh sách các tên hiện có
def display_names():
    print("\nDanh sách các tên hiện có:")
    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")
    print()

# Hàm thêm tên mới vào danh sách
def add_names():
    while True:
        new_name = input("Nhập tên bạn muốn thêm (nhập 'stop' để dừng): ").strip()
        if new_name.lower() == "stop":
            break
        if new_name and new_name not in names:
            names.add(new_name)
            print(f"Đã thêm tên: {new_name}")
        else:
            print("Tên không hợp lệ hoặc đã tồn tại.")

# Lưu danh sách tên ngẫu nhiên vào tệp
def save_to_file(random_names):
    with open("random_names.txt", "w") as file:
        file.write("\n".join(random_names))
    print("Danh sách tên ngẫu nhiên đã được lưu vào tệp 'random_names.txt'.")

# Hàm xử lý việc tạo danh sách tên ngẫu nhiên
def handle_random_names():
    try:
        num = int(input("Nhập số lượng tên bạn muốn tạo: "))
        if num > 0:
            if not names:
                print("Danh sách tên đang trống. Vui lòng thêm tên trước khi tạo danh sách ngẫu nhiên.")
            else:
                random_names = generate_random_names(num)
                print("Các tên ngẫu nhiên:", random_names)
                save_option = input("Bạn có muốn lưu danh sách này vào tệp không? (y/n): ").lower()
                if save_option == "y":
                    save_to_file(random_names)
        else:
            print("Số lượng phải lớn hơn 0.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

# Menu chức năng
def menu():
    while True:
        print("\n=== Chương trình Tạo Tên Ngẫu Nhiên ===")
        print("1. Hiển thị danh sách các tên hiện có")
        print("2. Thêm tên mới vào danh sách")
        print("3. Tạo danh sách tên ngẫu nhiên")
        print("4. Thoát")
        choice = input("Nhập lựa chọn của bạn: ").strip()

        if choice == "1":
            display_names()
        elif choice == "2":
            add_names()
        elif choice == "3":
            handle_random_names()
        elif choice == "4":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

# Chạy chương trình
if __name__ == "__main__":
    menu()