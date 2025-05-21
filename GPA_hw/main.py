# GPA değerleri için sözlük
grade_points = {
    "A": 4.00, "A-": 3.70, "B+": 3.30, "B": 3.00,
    "B-": 2.70, "C+": 2.30, "C": 2.00, "C-": 1.70,
    "D+": 1.30, "D": 1.00, "F": 0.00
}

# Dosya adını kullanıcıdan al
filename = input("Please enter the filename: ")

# Öğrencilerin isim-GPA verisini tutacak sözlük
student_gpa = {}

# Dosyayı aç ve işle
with open(filename, 'r') as file:
    header = file.readline()

    for line in file:
        line = line.strip()
        if not line:
            continue

        # Adım 1: Satırı parçalayarak isim ve notları ayır
        tokens = line.split()

        # Adım 2: Harf notlarını ve ismi ayır (kendi mantığını kur)
        grades = []
        # Öğrencinin adı ve notlar ayrılmalı
        # BU KISMI SEN TAMAMLA

        # Adım 3: GPA hesapla (grade_points sözlüğünü kullan)
        # BU KISMI SEN TAMAMLA

        # Adım 4: Sözlüğe kaydet
        # BU KISMI SEN TAMAMLA

# GPA'ya göre azalan, isme göre artan sıraya göre sırala
sorted_students = sorted(student_gpa.items(), key=lambda x: (-x[1], x[0]))

# Çıktıyı formatlı olarak yazdır
print("RANK - NAME - GPA")
for i, (name, gpa) in enumerate(sorted_students, start=1):
    print(f"{i} - {name} - {gpa:.2f}")