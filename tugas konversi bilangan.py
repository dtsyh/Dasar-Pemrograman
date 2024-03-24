x = int(input("Masukkan Nilai Bit : "))

bil_biner = ""
for item in range (x) :
    bil_biner += str(2 * item % 2)

print("Bilangan Biner : ", bil_biner)
print("Bilangan Oktal : ", oct(int(bil_biner, 2))[2 :])
print("Bilangan Desimal : ", int(bil_biner, 2))
print("Bilangan Heksadesimal : ", hex(int(bil_biner, 2))[2:])