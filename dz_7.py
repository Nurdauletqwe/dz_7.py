'''1'''
# import math

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# def main():
#     print("Welcome to the Engineering Calculator!")
#     print("Available operations:")
#     print("1. Addition (+)")
#     print("2. Subtraction (-)")
#     print("3. Multiplication (*)")
#     print("4. Division (/)")
#     print("5. Exponentiation (x^y)")
#     print("6. Factorial (n!)")
#     print("7. Fibonacci sequence (Fib(n))")
#     print("8. Trigonometric functions (sin, cos, tan)")
#     print("Enter 'exit' to quit")

#     while True:
#         operation = input("Choose an operation: ").lower()

#         if operation == "exit":
#             break

#         if operation in ["+", "-", "*", "/"]:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#             if operation == "+":
#                 result = num1 + num2
#             elif operation == "-":
#                 result = num1 - num2
#             elif operation == "*":
#                 result = num1 * num2
#             elif operation == "/":
#                 if num2 != 0:
#                     result = num1 / num2
#                 else:
#                     print("Error: division by zero")
#                     continue
#         elif operation == "x^y":
#             num1 = float(input("Enter base number: "))
#             num2 = float(input("Enter exponent: "))
#             result = num1 ** num2
#         elif operation == "n!":
#             num = int(input("Enter a number to calculate its factorial: "))
#             result = factorial(num)
#         elif operation == "fib(n)":
#             num = int(input("Enter a number to calculate Fibonacci sequence: "))
#             result = fibonacci(num)
#         elif operation in ["sin", "cos", "tan"]:
#             angle = float(input("Enter angle in degrees: "))
#             if operation == "sin":
#                 result = math.sin(math.radians(angle))
#             elif operation == "cos":
#                 result = math.cos(math.radians(angle))
#             elif operation == "tan":
#                 result = math.tan(math.radians(angle))
#         else:
#             print("Invalid operation, please try again.")
#             continue

#         print("Result:", result)

# if __name__ == "__main__":
#     main()

'''3'''
from collections import Counter

def determine_winner(votes):
    vote_count = Counter(votes)
    max_votes = max(vote_count.values())
    winners = [candidate for candidate, votes in vote_count.items() if votes == max_votes]
    if len(winners) == 1:
        return winners[0], max_votes
    else:
        shortest_winner = min(winners, key=len)
        return shortest_winner, max_votes

def main():
    candidates = ["Аскаров", "Бекмуханов", "Ернур", "Пешая", "Карим", "Шаримазданов"]
    votes = []

    print("Кандидаты в выборы:", ", ".join(candidates))
    print("Для голосования введите имя кандидата или 'exit' для завершения")

    while True:
        vote = input("Вы отдаете голос за: ").strip().title()
        if vote == "exit":
            break
        elif vote in candidates:
            print(vote)
        else:
            print("Некорректный выбор. Пожалуйста, выберите кандидата из списка.")

    winner, vote_count = determine_winner(votes)
    print(f"Победитель выборов: {winner}. Количество голосов: {vote_count}")

if __name__ == "__main__":
    main()