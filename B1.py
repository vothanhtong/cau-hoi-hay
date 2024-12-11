def bubble_sort(arr, reverse=False):
    """
    Sắp xếp danh sách bằng thuật toán Bubble Sort.

    Tham số:
        arr (list): Danh sách cần sắp xếp.
        reverse (bool): True nếu sắp xếp giảm dần, False nếu sắp xếp tăng dần.

    Trả về:
        list: Danh sách đã được sắp xếp.
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        # Sử dụng enumerate để rõ ràng và tối ưu
        for j, _ in enumerate(arr[:n - i - 1]):
            if (arr[j] > arr[j + 1]) ^ reverse:  # XOR để xác định hướng sắp xếp
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Dừng sớm nếu không có hoán đổi
            break
    return arr

# Minh họa sử dụng
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sắp xếp tăng dần
    print("Tăng dần:", bubble_sort(arr.copy()))

    # Sắp xếp giảm dần
    print("Giảm dần:", bubble_sort(arr.copy(), reverse=True))

    # Kiểm tra danh sách rỗng
    print("Danh sách rỗng:", bubble_sort([]))

    # Kiểm tra danh sách một phần tử
    print("Danh sách một phần tử:", bubble_sort([42]))

    # Kiểm tra danh sách có giá trị giống nhau
    print("Danh sách giá trị giống nhau:", bubble_sort([5, 5, 5, 5]))
