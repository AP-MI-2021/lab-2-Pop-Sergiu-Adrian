def get_largest_prime_below(n):
    try:
        n = int(n)
    except:
        return None
    if n < 1:
        return None
    elif n == 1 or n == 2:
        return n
    for number in reversed(range(1, n)):
        if number % 2 != 0:
            prime = True
            for divisor in range(3, int(number / 2), 2):
                if number % divisor == 0:
                    prime = False
            if prime == True:
                return number


def is_palindrome(n):

    if int(n) < 0:
        n = 0 - int(n)
    n_copy = int(n)
    palindrom = 0
    while (n):
        digit = n % 10
        palindrom = palindrom * 10 + digit
        n = n // 10
    if palindrom == n_copy:
        return True
    return False
def is_antipalindrome(n):
    """
    Este o functie care stabileste daca un numer este sau nu antipalindrom
    return:  true daca elementul este anipalindrom si false daca nu

    """
    if n == n[::-1]:
        return False
    return True

def test_is_antipalindrome():
    assert is_antipalindrome("12721") is False
    assert is_antipalindrome("14842394") is True
    assert is_antipalindrome("26") is False



def test_get_largest_prime_below():
    assert (get_largest_prime_below(39) == 37)
    assert (get_largest_prime_below(14) == 13)
    assert (get_largest_prime_below(121) == 113)


def test_is_palidrom():
    assert (is_palindrome(333) == True)
    assert (is_palindrome(12121) == True)
    assert (is_palindrome(127) == False)


def main():
    test_get_largest_prime_below()
    test_is_palidrom()
    while True:
        print(" 1. Afisati cel mai mare numar prim mai mic decat x. ")
        print(" 2. Verifica daca x este palindrom. ")
        print (" 3. Verifica daca n este antipalindrom. ")
        print(" x. Exit")
        option = input("Optiunea voastra: ")
        if option == "1":
            number = input("Introduceti valoarea lui x: ")
            print(f"Cel mai mic numar prim mai mic decat {number} este {get_largest_prime_below(number)}")
        elif option == "2":
            number = int(input("Introduceti valoarea lui x: "))
            print(is_palindrome(int(number)))
        elif option == "3":
            n = input("introduceeti numarul: ")
            print("Rezultatul: ", is_antipalindrome(n))
        elif option =="x":
            break
        else:
            print("Valoarea introdusa nu este corecta!")


if __name__ == "__main__":
    main()
