def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

word = raw_input('give me a word:\n')
x = reverse(word)
print x
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')
