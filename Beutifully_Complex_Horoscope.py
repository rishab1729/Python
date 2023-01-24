s = input()
A = []
B = []

for c in s:
    if c.isalpha() and c.lower() not in B: 
        A += [ord(c)%32]
        B += [c.lower()]
    if len(A) == 3: break
X = "altruistic acts, an award, a breakup, career change, completion of a big project, crime, disappointment, disaster, an epic experience, new love, forgiveness, illness, injury, incarceration, inspiration, investment gain, lifestyle change, a new friend, moments of wonder and clarity, a move, realizing something important, reconciliation, redemption, solving a problem, a transformative experience, a trip".split(', ')

print(s+":")
print("There will be", ' and '.join(X[i-1] for i in A), 'in your future.')
