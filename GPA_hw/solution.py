# GPA değerleri için sözlük
grade_points = {
    "A": 4.00, "A-": 3.70, "B+": 3.30, "B": 3.00,
    "B-": 2.70, "C+": 2.30, "C": 2.00, "C-": 1.70,
    "D+": 1.30, "D": 1.00, "F": 0.00
}

# Dosya adı iste
filename = input("Please enter the filename: ")

# Sonuçları tutacak sözlük
student_gpa = {}

# Dosyayı oku
with open(filename, 'w') as file:
    header = file.readline()  # başlık satırını atla

    for line in file:
        line = line.strip()
        if not line:
            continue

        # Satırı boşluklara göre parçala
        tokens = line.split()

        # Harf notlarını sondan itibaren ayır
        grades = []
        while tokens and tokens[-1] in grade_points:
            grades.insert(0, tokens.pop())

        # Geriye kalanlar isimdir
        name = " ".join(tokens)

        # GPA hesapla
        total = sum(grade_points[g] for g in grades)
        gpa = total / len(grades) if grades else 0.0

        student_gpa[name] = gpa

# Sırala: önce GPA'ya göre azalan, sonra isme göre artan
sorted_students = sorted(student_gpa.items(), key=lambda x: (-x[1], x[0]))

# Çıktı
print("RANK - NAME - GPA")
for i, (name, gpa) in enumerate(sorted_students, start=1):
    print(f"{i} - {name} - {gpa:.2f}")