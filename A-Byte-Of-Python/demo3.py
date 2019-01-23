#判断回文字符串

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)
while True:
    something = input("Enter text: ")

    if something == 'end':
        break
    if is_palindrome(something):
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")
