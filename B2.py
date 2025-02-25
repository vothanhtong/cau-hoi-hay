from functools import cmp_to_key
from typing import List, Callable, Any
import time

def bubble_sort(
    arr: List[Any],
    reverse: bool = False,
    key: Callable[[Any], Any] | None = None,
    inplace: bool = False,
    verbose: bool = False,
    stability: bool = False,
    stats: bool = False
) -> List[Any]:
    """
    Sắp xếp danh sách bằng thuật toán Bubble Sort.

    Tham số:
        arr (list): Danh sách cần sắp xếp.
        reverse (bool): True để sắp xếp giảm dần, False để tăng dần (mặc định).
        key (callable, optional): Hàm trả về giá trị so sánh từ phần tử.
        inplace (bool): True để sửa đổi danh sách gốc, False để trả về bản sao.
        verbose (bool): True để in chi tiết quá trình sắp xếp.
        stability (bool): True để đảm bảo tính ổn định (giữ thứ tự ban đầu khi giá trị bằng nhau).
        stats (bool): True để hiển thị thống kê hiệu suất (số phép so sánh, thời gian).

    Trả về:
        list: Danh sách đã được sắp xếp.

    Ngoại lệ:
        TypeError: Nếu `arr` không phải list hoặc `key` không phải callable.
        ValueError: Nếu phần tử không thể so sánh với `key`.
    """
    # Kiểm tra kiểu dữ liệu đầu vào
    if not isinstance(arr, list):
        raise TypeError("Tham số 'arr' phải là một danh sách (list).")
    if key is not None and not callable(key):
        raise TypeError("Tham số 'key' phải là một callable (hàm).")

    # Tạo bản sao nếu không sắp xếp tại chỗ
    result = arr if inplace else arr.copy()
    if len(result) <= 1:  # Trả về ngay nếu danh sách rỗng hoặc 1 phần tử
        if verbose and result:
            print(f"Danh sách đã được sắp xếp: {result}")
        return result

    # Xử lý hàm key
    key_func = key if key else (lambda x: x)

    # Kiểm tra khả năng so sánh
    try:
        sample = [key_func(x) for x in result]
    except Exception as e:
        raise ValueError("Phần tử trong danh sách không thể so sánh hoặc key không hợp lệ.") from e

    # Khởi tạo biến
    n = len(result)
    comparisons = 0  # Đếm số phép so sánh
    swaps_count = 0  # Đếm số lần hoán đổi
    start_time = time.perf_counter() if stats else None

    # Vòng lặp Bubble Sort
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            comparisons += 1
            left_val, right_val = key_func(result[j]), key_func(result[j + 1])

            # Kiểm tra điều kiện hoán đổi
            should_swap = (left_val > right_val) ^ reverse
            if stability and left_val == right_val:
                should_swap = False  # Giữ ổn định nếu giá trị bằng nhau

            if should_swap:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
                swaps_count += 1
                if verbose:
                    print(f"Hoán đổi [{j} ↔ {j+1}]: {result[j]} ↔ {result[j+1]} -> {result}")

        # Thoát sớm nếu không còn hoán đổi
        if not swapped:
            if verbose:
                print(f"Không còn hoán đổi ở vòng lặp {i + 1}. Kết thúc sớm!")
            break

    # Hiển thị kết quả và thống kê
    if verbose:
        print(f"Kết quả sắp xếp: {result}")
    if stats:
        elapsed_time = time.perf_counter() - start_time
        print(f"Thống kê: {comparisons} phép so sánh, {swaps_count} lần hoán đổi, {elapsed_time:.6f} giây")

    return result

# Minh họa sử dụng
if __name__ == "__main__":
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], False, None, False, True, False, False, "Sắp xếp tăng dần"),
        ([64, 34, 25, 12, 22, 11, 90], True, None, False, True, False, False, "Sắp xếp giảm dần"),
        ([("a", 3), ("b", 1), ("c", 2)], False, lambda x: x[1], False, True, False, False, "Sắp xếp theo giá trị tuple"),
        ([("x", 2), ("y", 2), ("z", 1)], False, lambda x: x[1], True, True, True, True, "Sắp xếp với tính ổn định"),
        ([], False, None, False, True, False, False, "Danh sách rỗng"),
        ([42], False, None, False, True, False, False, "Danh sách một phần tử"),
        ([5, 5, 5, 5], False, None, False, True, True, True, "Danh sách giá trị giống nhau"),
        ([3.1, 2.4, 5.6, 1.2], True, None, True, True, False, True, "Số thực giảm dần, tại chỗ"),
        (["z", "a", "c", "b"], False, str.lower, False, True, False, False, "Chuỗi theo thứ tự chữ cái"),
    ]

    for arr, reverse, key, inplace, verbose, stability, stats, desc in test_cases:
        print(f"\n=== {desc} ===")
        print(f"Trước: {arr}")
        try:
            sorted_arr = bubble_sort(
                arr, reverse=reverse, key=key, inplace=inplace, verbose=verbose, stability=stability, stats=stats
            )
            print(f"Sau: {sorted_arr}")
        except (TypeError, ValueError) as e:
            print(f"Lỗi: {e}")

    # Trường hợp lỗi mẫu
    print("\n=== Trường hợp lỗi ===")
    try:
        bubble_sort("not a list")  # Truyền chuỗi thay vì danh sách
    except TypeError as e:
        print(f"Lỗi: {e}")