word = str(raw_input('give me a word:\n'))
if word[::-1] == word:
    print('This is a Palindrome')
else:
    print('This is NOT a Palindrome')
