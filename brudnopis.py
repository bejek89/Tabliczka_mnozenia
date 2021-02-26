import random

def zadanie():
    while True:
        a = random.randint(2, 100)
        b = random.randint(2, 100)
        if a * b > 300:
            continue
        else:
            break
    print('Rozwiąż zadanie')
    print(f'{a} * {b} = ?')
    c = int(input('Wynik: '))
    if c == a * b:
        print('Bardzo dobrze Dawidzie!!!')
    else:
        return (f'No chyba coś ci się pomyliło Dawidzie;) Prawidłowy wynik to {a * b}')

for i in range(5):
    print(zadanie())
    print()