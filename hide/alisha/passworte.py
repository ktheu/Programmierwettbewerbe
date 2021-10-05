import secrets

def Passwort_Generator():
    vowals = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    safety = ["A", "H", "sch", "Ch", "39", "4e", "sch4", "he6", "He8"]
    password = ""
    for i in range(1,3):
        a = secrets.choice(numbers)
        b = secrets.choice(consonants)
        c = secrets.choice(vowals)
        d = secrets.choice(safety)
        e = secrets.choice(consonants)
        f = secrets.choice(vowals)
        password = password + a + b + c + d + e + f
    print(password)

print("Wähle ein Passwort: \n")
for i in range(1, 20):
    Passwort_Generator()
print("\n\n")

'''
Super - das gefällt mir sehr gut. Insbesondere die Verwendung von secrets statt des normalen random ist
bemerkenswert!

'''