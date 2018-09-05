VOWELS = "aeiou"
vowelcount = 0
concount = 0
vowelsused = " "
consonants = ''
while vowelcount < 5 and concount < 5:
    word = input("Input a word: ")
    vowelindex = 0
    for char in word:
        if char in VOWELS:
            if char is "a" :
                if "a" not in vowelsused:
                    vowelsused = vowelsused + "a"
                    vowelcount += 1
                    
            if char is "e":
                if "e" not in vowelsused:
                    vowelsused = vowelsused + "e"
                    vowelcount+=1
                    
            if char is "i":
                if "i" not in vowelsused:
                    vowelsused = vowelsused + "i"
                    vowelcount += 1
            if char is "o":
                if "o" not in vowelsused:
                    vowelsused = vowelsused + "o"
                    vowelcount += 1
            if char is "u":
                if "u" not in vowelsused:
                    vowelsused = vowelsused + "u"
                    vowelcount += 1
    for j, ch in enumerate(word):
        if ch in VOWELS:
           vowelindex = j
    lastconsonants = word[vowelindex + 1:]
    for j, ch in enumerate(lastconsonants):
            if ch not in consonants:
                consonants = consonants + ch
                concount += 1
                
print("\n"+"="*12)               
print("{:8s}{:7s} | {:12s}{:7s}".format("vowels","length","consonants","length"))
print("{:8s}{:<7d} | {:12s}{:<7d}".format(vowelsused,vowelcount,consonants,concount))
