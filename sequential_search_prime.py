def bil_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def angka_prima(angka):
    prima = []
    for num in angka:
        if bil_prima(num):
            prima.append(num)
    return prima

angka = [7, 10, 13, 6, 17, 22, 19]
prima = angka_prima(angka)
print("Bilangan prima didalam daftar adalah :", prima)