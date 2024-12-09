
### Câu hỏi 1: Giao điểm của hai danh sách
# Câu hỏi: Viết một hàm nhận vào hai danh sách và trả về danh sách các phần tử chung giữa chúng mà không có phần tử trùng lặp.

def intersection(list1, list2):
    return list(set(list1) & set(list2))

# Ví dụ sử dụng
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(intersection(list1, list2))  # Kết quả: [4, 5]


# Giải thích: Hàm sử dụng tập hợp (`set`) để loại bỏ các phần tử trùng lặp và tìm giao điểm của hai tập hợp này. Phép toán `&` giữa hai tập hợp sẽ trả về tập hợp chứa các phần tử chung.

### Câu hỏi 2: Kiểm tra số nguyên tố
# Câu hỏi: Viết một hàm kiểm tra xem một số có phải là số nguyên tố hay không.

def is_prime(n):
    if n <= 1:
        return False
    # for i in range(2, int(n0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ví dụ sử dụng
print(is_prime(29))  # Kết quả: True
print(is_prime(15))  # Kết quả: False


# Giải thích: Hàm kiểm tra nếu số `n` nhỏ hơn hoặc bằng 1 thì không phải là số nguyên tố. Sau đó, nó kiểm tra từ 2 đến căn bậc hai của `n` để xác định xem `n` có thể chia hết cho số nào hay không. Nếu có, số đó không phải là số nguyên tố.

### Câu hỏi 3: Xáo trộn danh sách
# Câu hỏi: Viết một hàm xáo trộn một danh sách mà không sử dụng bất kỳ thư viện có sẵn nào.

import random

def shuffle_list(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]
    return lst

# Ví dụ sử dụng
my_list = [1, 2, 3, 4, 5]
print(shuffle_list(my_list))  # Kết quả: danh sách đã xáo trộn
# Giải thích: Hàm sử dụng thuật toán xáo trộn Fisher-Yates. Nó lặp qua danh sách từ cuối lên đầu và hoán đổi từng phần tử với một phần tử ngẫu nhiên trước đó, đảm bảo rằng mọi thứ trong danh sách có cơ hội được xáo trộn đều.