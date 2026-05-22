def f(x):
    return x

a = 20251337009

h = 0.0001

kiri = f(a - h)
kanan = f(a + h)

print("Limit dari kiri :", kiri)
print("Limit dari kanan:", kanan)

if abs(kiri - kanan) < 0.001:
    print("hasil limit =", (kiri + kanan) / 2)
else:
    print("Limit tidak ada")
