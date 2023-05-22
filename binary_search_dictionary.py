def find_definition(word, dictionary):
    low = 0
    high = len(dictionary) - 1

    while low <= high:
        mid = (low + high) // 2

        if dictionary[mid][0] == word:
            return dictionary[mid][1]
        elif dictionary[mid][0] < word:
            low = mid + 1
        else:
            high = mid - 1

    return "Definisi kata tidak ditemukan"

# Kamus ajaib
dictionary = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

# Kata yang ingin dicari definisinya
word = "Cat"

# Mencari definisi kata
definition = find_definition(word, dictionary)

# Menampilkan definisi kata
print("Definisi kata", word + ":", definition)