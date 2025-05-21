# tombala_game.py

def play_tombala():
    """
    Simulate a simplified Tombala game between Grandma and You.

    Yapılacaklar:
    - Kullanıcıdan 3 input al:
        1. Grandma'nın kartı (12 sayı, "-" ile ayrılmış)
        2. You'nun kartı (12 sayı, "-" ile ayrılmış)
        3. Çekiliş sırası (1-30 arası sayılar, "-" ile ayrılmış)
    - Çekilişleri sırasıyla kontrol et ve sonucu yazdır.
    """

    print("Welcome to the New Year's night fun(!)")
    print("Please enter the Tombala card for Grandma: ")
    grandma_input = input()
    print("Please enter the Tombala card for You: ")
    you_input = input()
    print("Please enter the numbers drawn in the order: ")
    draw_input = input()

    print("----")
    grandma_numbers = [int(x) for x in grandma_input.strip().split("-")]
    you_numbers = [int(x) for x in you_input.strip().split("-")]
    draw_numbers = [int(x) for x in draw_input.strip().split("-")]

    grandma_remaining = set(grandma_numbers)
    you_remaining = set(you_numbers)

    winner = None
    tie = False

    # Döngü: çekiliş sırasını sırayla işle
    for num in draw_numbers:
        line = f"Number {num} is drawn."

        # Burada Grandma ve You'nun kartlarını kontrol edeceksin:
        # Eğer Grandma'nın kartında varsa hem yazdır hem de karttan çıkar
        # Eğer You'nun kartında varsa hem yazdır hem de karttan çıkar

        # İPUCU: if num in grandma_remaining: ...

        # Burada oyunun bitip bitmediğini kontrol et:
        # - İkisi de bitirdiyse tie
        # - Sadece biri bitirdiyse winner belirle ve döngüyü kır


    print("----")
    # Sonuçları burada yazdır:
    # - Tie olduysa "Grandma and You finish at the same round. It's a tie!"
    # - Grandma kazandıysa:
    #   - "Grandma wins."
    #   - "Remaining numbers of You: ..." (YOU kartının sırasına göre kalanları yaz)
    # - You kazandıysa:
    #   - "You win."
    #   - "Remaining numbers of Grandma: ..." (GRANDMA kartının sırasına göre kalanları yaz)


if __name__ == "__main__":
    play_tombala()