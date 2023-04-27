def romandToInt(s: str) -> int:
	romand = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000
	}

	res = 0

	for i in range(len(s)):
		if i + 1 < len(s) and romand[s[i]] < romand[s[i+1]]:
			res -= romand[s[i]]
		else:
			res += romand[s[i]]

	return res

print(romandToInt("III"))
print(romandToInt("LVXII"))
print(romandToInt("IVIV"))