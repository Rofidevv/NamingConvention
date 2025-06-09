from calculator import Calculator
from strategi import AddOperation, SubtractOperation, MultiplyOperation, DivideOperation

print("=== Kalkulator Strategy Pattern ===")

try:
    bil1 = int(input("Masukkan bilangan pertama : "))
    bil2 = int(input("Masukkan bilangan kedua : "))
except ValueError:
    print("Input harus berupa bilangan bulat!")
    exit()

print("\nPilih operasi:")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali   (*)")
print("4. Bagi   (/)")
pilihan = input("Pilihan: ")

# Set default strategy
strategy = None

if pilihan == '1':
    strategy = AddOperation()
elif pilihan == '2':
    strategy = SubtractOperation()
elif pilihan == '3':
    strategy = MultiplyOperation()
elif pilihan == '4':
    strategy = DivideOperation()
else:
    print("Pilihan tidak valid!")
    exit()

kalkulator = Calculator(strategy)

try:
    hasil = kalkulator.calculate(bil1, bil2)
    print(f"\nHasil operasi: {hasil}")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
