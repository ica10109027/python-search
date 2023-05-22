def binary_serch_rotation(data):
    low = 0
    high = len(data) - 1

    while low < high:
        mid = (low + high) // 2
        if data[mid] > data[high]:
            low = mid + 1
        else:
            high = mid

    return

my_list = [6, 7, 8, 9, 1, 2, 3, 4, 5,]
rotation_index = binary_serch_rotation(my_list)
print(f"index rotasi terkecil adalah {rotation_index}")