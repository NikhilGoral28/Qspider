while True:
    print("\n1. Palindrome number")
    print("2. Armstrong Number")
    print("3. Storng number")
    print("4. Exist")

    choice = int(input("Enter choice: "))

    if choice == 4:
        print("Execution complete")
        break

    num = int(input("Enter a number: "))

    match choice:
        
        case 1:
            temp = num
            rev = 0

            while temp > 0:
                digit = temp % 10
                rev = rev * 10 + digit
                temp //= 10

            if num == rev:
                print(f"{num} is the palindrome number")

            else:
                print(f"{num} is not a palindrome number")

        case 2:
            temp = num
            sum_digit = 0
            length = len(num)

            while temp > 0:
                digit = temp % 10
                sum_digit = sum_digit + digit ** length

                temp = temp // 10

            if num == sum_digit:
                print(f"{num} is the armstrong number")
            else:
                print(f"{num} is not the armstrong number")
            
        case 3:
            temp = num
            digit_fact = 0

            while temp > 0:
                digit = temp % 10
                fact = 1
                for i in range(1, digit + 1):
                    fact *= i

                digit_fact = digit_fact + fact
                temp = temp // 10

            if num == digit_fact:
                print(f"{num} is the strong number")
            else:
                print(f"{num} is not strong number")
        
        case _:
            print(f"=")