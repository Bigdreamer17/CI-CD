def fizzbuzz(number : int):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

if __name__ == "__main__":
    num_inp = int(input("Enter a number: "))
    print(fizzbuzz(num_inp))