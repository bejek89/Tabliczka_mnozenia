import random, time

sleep = 2

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

print('Witaj Dawidzie w niesamowitej grze zwanej ...')
time.sleep(sleep)
print('TABLICZKĄ MNOŻENIA :D')
time.sleep(sleep)
print('aby móc zakończyć gre musisz zdobyć 5 punktów')
time.sleep(sleep)
print('za każde dobrze rozwiązane zadanie otrzymujesz jeden punkt')
time.sleep(sleep)
print('GOTOWY ?')
time.sleep(sleep)
print('ZACZYNAMY !!!')
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
print()

for i in range(5):
    print(zadanie())
    print()