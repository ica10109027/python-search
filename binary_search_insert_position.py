def find_insertion_position(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

# Data yang sudah diurutkan
data = [2, 4, 6, 8, 10, 12, 14]
target = 7

# Mencari posisi sisipan elemen
insertion_position = find_insertion_position(data, target)

# Menampilkan hasil
print("Elemen", target, "dapat disisipkan pada indeks", insertion_position,
      "untuk menjaga daftar tetap terurut.")