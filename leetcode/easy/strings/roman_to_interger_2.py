def romanToInt(s):
        def isException(char, s, int):
            if not index < len(s) - 1:
                return False
            nextLetter = s[index + 1]
            if char == "I" and (nextLetter == "V" or nextLetter == "X"):
                return True
            elif char == "X" and (nextLetter == "L" or nextLetter == "C"):
                return True
            elif char == "C" and (nextLetter == "D" or nextLetter == "M"):
                return True
            else:
                return False
        romanNumeralConversion = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        returnInt = 0
        for index, char in enumerate(s):
            if isException(char, s, index):
                returnInt -= romanNumeralConversion[char]
            else:
                returnInt += romanNumeralConversion[char]
        return returnInt
# cleaner solution
def romanToInt(s):
    romanNumeralConversion = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    return_value = 0
    prev = 0

    for char in s[::-1]:
        curr_val = romanNumeralConversion[char]
        if curr_val < prev:
            return_value -= romanNumeralConversion[char]
        else:
            return_value += romanNumeralConversion[char]
        prev = curr_val
    return return_value
