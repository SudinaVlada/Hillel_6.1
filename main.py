import string
print(string.ascii_letters)
letters = input("Введіть літери: ")
a = letters[0]
b = letters[-1]
first_l = string.ascii_letters.index(a)
second_l = string.ascii_letters.index(b)
if first_l > second_l:
    print(False)
ran = string.ascii_letters[first_l:second_l+1]
print(ran)