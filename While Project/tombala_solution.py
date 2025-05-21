def play_tombala(grandma_input, you_input, draw_input):
    print("Welcome to the New Year's night fun(!)")
    print("Please enter the Tombala card for Grandma: ")
    print(grandma_input)
    print("Please enter the Tombala card for You: ")
    print(you_input)
    print("Please enter the numbers drawn in the order: ")
    print(draw_input)

    print("----")
    grandma_numbers = [int(x) for x in grandma_input.strip().split("-")]
    you_numbers = [int(x) for x in you_input.strip().split("-")]
    draw_numbers = [int(x) for x in draw_input.strip().split("-")]

    grandma_remaining = set(grandma_numbers)
    you_remaining = set(you_numbers)

    winner = None
    tie = False

    for num in draw_numbers:
        line = f"Number {num} is drawn."
        if num in grandma_remaining:
            grandma_remaining.remove(num)
            line += " Grandma has it."
        if num in you_remaining:
            you_remaining.remove(num)
            line += " You have it."
        print(line)

        if len(grandma_remaining) == 0 and len(you_remaining) == 0:
            tie = True
            break
        elif len(grandma_remaining) == 0:
            winner = "Grandma"
            break
        elif len(you_remaining) == 0:
            winner = "You"
            break

    print("----")
    if tie:
        print("Grandma and You finish at the same round. It's a tie!")
    elif winner == "Grandma":
        print("Grandma wins.")
        remaining_you = [str(n) for n in you_numbers if n in you_remaining]
        print("Remaining numbers of You: " + "-".join(remaining_you))
    elif winner == "You":
        print("You win.")
        remaining_grandma = [str(n) for n in grandma_numbers if n in grandma_remaining]
        print("Remaining numbers of Grandma: " + "-".join(remaining_grandma))