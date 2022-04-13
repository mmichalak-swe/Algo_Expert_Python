def caesarCipherEncryptor(string, key):
	ans = []
	new_key = key % 26

	for char in string:
		letter_code = ord(char) + new_key
		if (letter_code > 122):
			ans.append(chr(96 + letter_code % 122))
		else:
			ans.append(chr(letter_code))

	return "".join(ans)
