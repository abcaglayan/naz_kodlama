import io
import sys
from tombala_solution import play_tombala
import difflib

# Test data ve beklenen çıktılar
input_data_1 = (
    "5-7-22-29-6-26-23-19-11-30-4-27\n"
    "7-25-14-23-9-15-26-17-1-11-12-5\n"
    "5-7-22-29-6-26-23-19-11-30-4-27-24-17-28-15-10-3-16-14-1-2-12-13-21-9-25-20-8-18\n"
)

expected_output_1 = (
    "Welcome to the New Year's night fun(!)\n"
    "Please enter the Tombala card for Grandma: \n"
    "Please enter the Tombala card for You: \n"
    "Please enter the numbers drawn in the order: \n"
    "----\n"
    "Number 5 is drawn. Grandma has it. You have it.\n"
    "Number 7 is drawn. Grandma has it. You have it.\n"
    "Number 22 is drawn. Grandma has it.\n"
    "Number 29 is drawn. Grandma has it.\n"
    "Number 6 is drawn. Grandma has it.\n"
    "Number 26 is drawn. Grandma has it. You have it.\n"
    "Number 23 is drawn. Grandma has it. You have it.\n"
    "Number 19 is drawn. Grandma has it.\n"
    "Number 11 is drawn. Grandma has it. You have it.\n"
    "Number 30 is drawn. Grandma has it.\n"
    "Number 4 is drawn. Grandma has it.\n"
    "Number 27 is drawn. Grandma has it.\n"
    "----\n"
    "Grandma wins.\n"
    "Remaining numbers of You: 25-14-9-15-17-1-12\n"
)
input_data_2 = (
    "17-2-24-19-29-8-26-4-12-14-10-28\n"
    "14-2-27-21-25-23-29-24-5-3-4-20\n"
    "10-5-18-3-22-1-20-2-14-6-13-25-27-15-4-26-8-24-21-23-28-12-29-7-17-16-11-19-9-30\n"
)

expected_output_2 = (
    "Welcome to the New Year's night fun(!)\n"
    "Please enter the Tombala card for Grandma: \n"
    "Please enter the Tombala card for You: \n"
    "Please enter the numbers drawn in the order: \n"
    "----\n"
    "Number 10 is drawn. Grandma has it.\n"
    "Number 5 is drawn. You have it.\n"
    "Number 18 is drawn.\n"
    "Number 3 is drawn. You have it.\n"
    "Number 22 is drawn.\n"
    "Number 1 is drawn.\n"
    "Number 20 is drawn. You have it.\n"
    "Number 2 is drawn. Grandma has it. You have it.\n"
    "Number 14 is drawn. Grandma has it. You have it.\n"
    "Number 6 is drawn.\n"
    "Number 13 is drawn.\n"
    "Number 25 is drawn. You have it.\n"
    "Number 27 is drawn. You have it.\n"
    "Number 15 is drawn.\n"
    "Number 4 is drawn. Grandma has it. You have it.\n"
    "Number 26 is drawn. Grandma has it.\n"
    "Number 8 is drawn. Grandma has it.\n"
    "Number 24 is drawn. Grandma has it. You have it.\n"
    "Number 21 is drawn. You have it.\n"
    "Number 23 is drawn. You have it.\n"
    "Number 28 is drawn. Grandma has it.\n"
    "Number 12 is drawn. Grandma has it.\n"
    "Number 29 is drawn. Grandma has it. You have it.\n"
    "----\n"
    "You win.\n"
    "Remaining numbers of Grandma: 17-19\n"
)
input_data_3 = (
    "22-24-28-23-7-11-6-29-17-21-16-4\n"
    "4-11-24-26-22-19-15-14-20-12-29-7\n"
    "21-20-26-2-8-23-18-30-12-1-16-17-24-3-28-7-10-4-14-11-27-25-13-29-6-9-5-15-19-22\n"
)

expected_output_3 = (
    "Welcome to the New Year's night fun(!)\n"
    "Please enter the Tombala card for Grandma: \n"
    "Please enter the Tombala card for You: \n"
    "Please enter the numbers drawn in the order: \n"
    "----\n"
    "Number 21 is drawn. Grandma has it.\n"
    "Number 20 is drawn. You have it.\n"
    "Number 26 is drawn. You have it.\n"
    "Number 2 is drawn.\n"
    "Number 8 is drawn.\n"
    "Number 23 is drawn. Grandma has it.\n"
    "Number 18 is drawn.\n"
    "Number 30 is drawn.\n"
    "Number 12 is drawn. You have it.\n"
    "Number 1 is drawn.\n"
    "Number 16 is drawn. Grandma has it.\n"
    "Number 17 is drawn. Grandma has it.\n"
    "Number 24 is drawn. Grandma has it. You have it.\n"
    "Number 3 is drawn.\n"
    "Number 28 is drawn. Grandma has it.\n"
    "Number 7 is drawn. Grandma has it. You have it.\n"
    "Number 10 is drawn.\n"
    "Number 4 is drawn. Grandma has it. You have it.\n"
    "Number 14 is drawn. You have it.\n"
    "Number 11 is drawn. Grandma has it. You have it.\n"
    "Number 27 is drawn.\n"
    "Number 25 is drawn.\n"
    "Number 13 is drawn.\n"
    "Number 29 is drawn. Grandma has it. You have it.\n"
    "----\n"
    "Grandma and You finish at the same round. It's a tie!\n"
)
input_data_4 = (
    "3-5-7-9-11-13-15-17-19-21-23-25\n"
    "2-4-6-8-10-12-14-16-18-20-22-24\n"
    "2-4-6-8-10-12-14-16-18-20-22-24-1-3-5-7-9-11-13-15-17-19-21-23-25-26-27-28-29-30\n"
)

expected_output_4 = (
    "Welcome to the New Year's night fun(!)\n"
    "Please enter the Tombala card for Grandma: \n"
    "Please enter the Tombala card for You: \n"
    "Please enter the numbers drawn in the order: \n"
    "----\n"
    "Number 2 is drawn. You have it.\n"
    "Number 4 is drawn. You have it.\n"
    "Number 6 is drawn. You have it.\n"
    "Number 8 is drawn. You have it.\n"
    "Number 10 is drawn. You have it.\n"
    "Number 12 is drawn. You have it.\n"
    "Number 14 is drawn. You have it.\n"
    "Number 16 is drawn. You have it.\n"
    "Number 18 is drawn. You have it.\n"
    "Number 20 is drawn. You have it.\n"
    "Number 22 is drawn. You have it.\n"
    "Number 24 is drawn. You have it.\n"
    "----\n"
    "You win.\n"
    "Remaining numbers of Grandma: 3-5-7-9-11-13-15-17-19-21-23-25\n"
)
input_data_5 = (
    "1-3-5-7-9-11-13-15-17-19-21-23\n"
    "2-4-6-8-10-12-14-16-18-20-22-24\n"
    "1-3-5-7-9-11-13-15-17-19-21-23-2-4-6-8-10-12-14-16-18-20-22-24-25-26-27-28-29-30\n"
)

expected_output_5 = (
    "Welcome to the New Year's night fun(!)\n"
    "Please enter the Tombala card for Grandma: \n"
    "Please enter the Tombala card for You: \n"
    "Please enter the numbers drawn in the order: \n"
    "----\n"
    "Number 1 is drawn. Grandma has it.\n"
    "Number 3 is drawn. Grandma has it.\n"
    "Number 5 is drawn. Grandma has it.\n"
    "Number 7 is drawn. Grandma has it.\n"
    "Number 9 is drawn. Grandma has it.\n"
    "Number 11 is drawn. Grandma has it.\n"
    "Number 13 is drawn. Grandma has it.\n"
    "Number 15 is drawn. Grandma has it.\n"
    "Number 17 is drawn. Grandma has it.\n"
    "Number 19 is drawn. Grandma has it.\n"
    "Number 21 is drawn. Grandma has it.\n"
    "Number 23 is drawn. Grandma has it.\n"
    "----\n"
    "Grandma wins.\n"
    "Remaining numbers of You: 2-4-6-8-10-12-14-16-18-20-22-24\n"
)

# Testler listesi
test_cases = [
    (input_data_1, expected_output_1, "Grandma wins scenario"),
    (input_data_2, expected_output_2, "You wins scenario"),
    (input_data_3, expected_output_3, "Tie scenario"),
    (input_data_4, expected_output_4, "You wins different cards"),
    (input_data_5, expected_output_5, "Grandma wins different cards"),
]

total_tests = len(test_cases)
passed_tests = 0

def parse_input(input_data):
    """Parse input_data into 3 parçaya ayır: Grandma kartı, You kartı, Çekiliş sırası."""
    lines = input_data.strip().splitlines()
    grandma_card = lines[0]
    you_card = lines[1]
    draw_order = lines[2]
    return grandma_card, you_card, draw_order

def extract_result(expected_output):
    """Beklenen çıktıdan kazananı ve kalanları çek."""
    lines = expected_output.strip().splitlines()
    winner_line = [line for line in lines if "wins" in line or "tie" in line]
    remaining_line = [line for line in lines if "Remaining numbers" in line]
    winner_text = winner_line[0] if winner_line else "Sonuç bulunamadı"
    remaining_text = remaining_line[0] if remaining_line else "Kalan numaralar yok"
    return winner_text, remaining_text

def run_test(input_data, expected_output, description, current_index):
    grandma_card, you_card, draw_order = parse_input(input_data)
    winner_text, remaining_text = extract_result(expected_output)

    print(f"\n--- Test {current_index}/{total_tests}: {description} ---")
    print(f"Grandma kartı: {grandma_card}")
    print(f"You kartı: {you_card}")
    print(f"Çekiliş sırası: {draw_order}")
    print(f"Beklenen sonuç: {winner_text}")
    print(f"Beklenen kalanlar: {remaining_text}")

    original_stdin = sys.stdin
    original_stdout = sys.stdout
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    try:
        play_tombala()
        output = sys.stdout.getvalue()
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout

    # Sonuç kontrolü
    if output != expected_output:
        print(f"\n❌ Test {description} BAŞARISIZ!")
        print(f"--- Üretilen Çıktı ---\n{output}")
        print(f"--- Beklenen Çıktı ---\n{expected_output}")
        diff = difflib.ndiff(output.splitlines(keepends=True), expected_output.splitlines(keepends=True))
        print('--- Farklar ---')
        print(''.join(diff))
        print(f"➡️ Şu ana kadar {passed_tests}/{total_tests} test geçti, {total_tests - passed_tests} test kaldı.")
        raise AssertionError(f"Test başarısız: {description}")

    print(f"✅ Test geçti: {description}")
    print(f"➡️ Şu ana kadar {passed_tests + 1}/{total_tests} test geçti, {total_tests - (passed_tests + 1)} test kaldı.")

    return True

# Tüm testleri sırayla çalıştır
for index, (input_data, expected_output, description) in enumerate(test_cases, start=1):
    try:
        if run_test(input_data, expected_output, description, index):
            passed_tests += 1
    except AssertionError as e:
        print("\n🛑 Testler burada durdu. Hata bulundu.")
        break

if passed_tests == total_tests:
    print("\n🎉 TÜM TESTLER BAŞARILI!")
else:
    print(f"\n✅ {passed_tests} test geçti, ❌ {total_tests - passed_tests} test başarısız.")