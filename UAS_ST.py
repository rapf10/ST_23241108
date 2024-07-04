# Menghitung nilai akhir dari 3 nilai mata kuliah

# Membuat variabel
nilai_akhir = 0

# Perulangan buat menginput nilai 3 mata kuliah
for i in range(3):
  print("Masukkan nilai mata kuliah ke-", i+1, ": ")
  nilai = float(input())

  # Percabangan menentukan nilai
  if nilai >= 90:
    grade = "A"
  elif nilai >= 80:
    grade = "B"
  elif nilai >= 70:
    grade = "C"
  elif nilai >= 60:
    grade = "D"
  else:
    grade = "E"

  print("Grade mata kuliah ke-", i+1, "adalah", grade)
  nilai_akhir += nilai

# nilai akhir
nilai_akhir /= 3

#print hasil
print("Nilai akhir adalah", nilai_akhir)
