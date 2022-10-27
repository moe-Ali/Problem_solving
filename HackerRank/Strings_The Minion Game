word=input()
vowels="AEIOU"
word_vowels={}
word_consonants={}
stuart_points=0
kevin_points=0
len(word)
for i in range(0,len(word)):
    if word[i] in vowels:
        kevin_points+=len(word)-i
    else:
        stuart_points+=len(word)-i
if kevin_points < stuart_points:
    print("Stuart "+str(stuart_points))
elif kevin_points > stuart_points:
    print("Kevin "+str(kevin_points))
else:
    print("Draw")
