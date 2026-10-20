# fibonacci_sequence.py

def generate_fibonacci(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def main():
    while True:
        user_input = input("How many Fibonacci numbers would you like to see? (1-20): ")
        try:
            num = int(user_input)
            if 1 <= num <= 20:
                fibonacci_numbers = generate_fibonacci(num)
                print("Fibonacci sequence:", " ".join(map(str, fibonacci_numbers)))
                break
            else:
                print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    main()


