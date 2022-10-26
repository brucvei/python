import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6, 
    "D": 8
}

def deposit():
    while True:
        amount = input("O quanto você gostaria de depositar? R$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("O valor deve ser maior que 0.")
        else:
            print("Insira um número.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Insira a quantidade de linhas (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("O valor deve ser estar entre 1 e " + str(MAX_LINES) + ".")
        else:
            print("Insira um número.")

    return lines

def get_bet():
    while True:
        amount = input("O quanto você gostaria de apostar em cada linha? R$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"O valor deve estar entre R${MIN_BET} - ${MAX_BET}")
        else:
            print("Insira um número.")

    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Você não possui o suficiente para apostar essa quantidade, sua balança é R${balance}")
        else:
            break

    print(f"Você está apostando R${bet} em {lines} linhas. O total é igual a R${total_bet}")


main()