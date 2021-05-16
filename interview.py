# FIZZBUZZ

# buatkan loop mencetak angka 100, kelipatan 3 keluar fizz, jika keluar 5, keluar buzz

for i in range(1, 101):

    string = ""
    if i % 3 == 0:
        # print("Fizz")
        string += "Fizz"

    if i % 5 == 0:
        # print("Buzz")
        string += "Buzz"

    if i % 3 != 0 and i % 5 != 0:
        string += str(i)

    print(string)

# PALINDROME

# program / function mengembalikan true jika parameter yang diberikan palindrome. Parameter string

# def palindrome(cekPalindrome):
#     return cekPalindrome == cekPalindrome[::-1]  # membalikkan string


# userInput = input("Kata : ")

# checker = palindrome(userInput)

# print(checker)
# if checker:
#     print("Adalah palindrome")

# else:
#     print("Bukan Palindrome")


# WHO IS THE WINNER?

# def splitEach(kata):
#     # return [list(char) for char in kata]
#     return list(kata)


# input_score = input("Urutan skor : ")
# splitWord = splitEach(input_score)
# print(splitWord)

# A = splitWord.count('A')
# B = splitWord.count('B')

# if A > B:
#     print("A menang")
# else:
#     print("B menang")
