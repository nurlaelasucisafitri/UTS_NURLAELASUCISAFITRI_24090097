berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (m): "))

bmi = berat_badan / (tinggi_badan ** 2)
if bmi < 18.5:
    kategori = "Berat badan kurang"
if 18.5 <= bmi < 24.9:
    kategori = "Berat badan normal"
if 25 <= bmi < 29.9:
    kategori = "Kelebihan berat badan"
if bmi >= 30:
    kategori = "Obesitas"

print(f"Berat badan: {berat_badan} kg")
print(f"Tinggi badan: {tinggi_badan} m")
print(f"Nilai BMI Anda: {bmi:.2f}")
print(f"Kategori BMI: {kategori}")