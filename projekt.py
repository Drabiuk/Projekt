from time import sleep
#funkcje--------------------------------------
def inf(data):
    for k, v in data.items():
        print(f"{k}: {v}")

def forma(data):
    print("Siła: ", data['siła'])
    print("Szybkość: ", data['szybkość'])
    print("Wystrzymałość: ", data['wytrzymałość'])

def trening():
    print("""
    Wybierz rodzaj treningu: 
    A - Skakanka(+10 do wytrzymałości)
    B - Ciężki worek(+10 do siły)
    C - Walka z cieniem(+10 do szybkości)
    """)
    wybor = input()
    global zawodnik
    if wybor.upper() == "A":
        zawodnik[x]['wytrzymałość'] += 10
    elif wybor.upper() == "B":
        zawodnik[x]['siła'] += 10
    elif wybor.upper() == "C":
        zawodnik[x]['szybkość'] += 10

def walka():
    global wygrane, przegrane
    rezultat = [
        zawodnik[x]['siła'] > przeciwnik[i]['siła'],
        zawodnik[x]['szybkość'] > przeciwnik[i]['szybkość'],
        zawodnik[x]['wytrzymałość'] > przeciwnik[i]['wytrzymałość']

    ]
    odliczanie = [5,4,3,2,1]
    for c in odliczanie:
        print(c),
        sleep(1)
    
    if any(rezultat):
        print("="*15)
        print("Zwycięstwo")
        wygrane += 1
    else:
        print("="*15)
        print("Przegrana")
        przegrane += 1

#postacie--------------------------
zawodnik = [
    {
        'imię':'Michał',
        'pseudonim': 'Terminator',
        'nazwisko':'Dawidko',
        'wiek': 17,
        'wzrost': 172,
        'waga': 90,
        'siła': 100,
        'szybkość': 70,
        'wytrzymałość': 90 
    },

    {
        'imię':'Andrzej',
        'pseudonim': 'Top-G',
        'nazwisko':'Tatkowski',
        'wiek': 35,
        'wzrost': 190,
        'waga': 89,
        'siła': 80,
        'szybkość': 90,
        'wytrzymałość': 60 
    },

    {
        'imię':'Kasjusz',
        'pseudonim': 'The greatest',
        'nazwisko':'Klej',
        'wiek': 22,
        'wzrost': 191,
        'waga': 93,
        'siła': 90,
        'szybkość': 120,
        'wytrzymałość': 100 
    }
]

przeciwnik = [
    {
        'imię':'Anthony',
        'pseudonim': 'AJ',
        'nazwisko':'Joshua',
        'wiek': 33,
        'wzrost': 198,
        'waga': 111,
        'siła': 120,
        'szybkość': 100,
        'wytrzymałość': 90 
    },

    {
        'imię':'Ołeksandr',
        'pseudonim': 'The Cat',
        'nazwisko':'Usyk',
        'wiek': 35,
        'wzrost': 191,
        'waga': 100,
        'siła': 130,
        'szybkość': 150,
        'wytrzymałość': 140 
    },

    {
        'imię':'Deontay',
        'pseudonim': 'The Bronze Bomber',
        'nazwisko':'Wilder',
        'wiek': 37,
        'wzrost': 201,
        'waga': 98,
        'siła': 150,
        'szybkość': 140,
        'wytrzymałość': 140 
    },

    {
        'imię':'Tyson',
        'pseudonim': 'Gypsy King',
        'nazwisko':'Fury',
        'wiek': 34,
        'wzrost': 206,
        'waga': 122,
        'siła': 170,
        'szybkość': 180,
        'wytrzymałość': 160 
    },

    {
        'imię':'Mike',
        'pseudonim': 'Kid Dynamite',
        'nazwisko':'Tyson',
        'wiek': 20,
        'wzrost': 178,
        'waga': 99,
        'siła': 200,
        'szybkość': 210,
        'wytrzymałość': 230 
    }
]

while True:
    print(
        f"""
                  WYBIERZ ZAWODNIKA \n
    {'='*50} \n
    Nr 1                   Nr 2                  Nr 3
    Imię: {zawodnik[0]['imię']}           Imię: {zawodnik[1]['imię']}         Imię: {zawodnik[2]['imię']}
    Pseudonim: {zawodnik[0]['pseudonim']}  Pseudonim: {zawodnik[1]['pseudonim']}      Pseudonim: {zawodnik[2]['pseudonim']}
    Nazwisko: {zawodnik[0]['nazwisko']}      Nazwisko: {zawodnik[1]['nazwisko']}   Nazwisko: {zawodnik[2]['nazwisko']}
    Wiek: {zawodnik[0]['wiek']}               Wiek: {zawodnik[1]['wiek']}              Wiek: {zawodnik[2]['wiek']}
    Wzrost: {zawodnik[0]['wzrost']}            Wzrost: {zawodnik[1]['wzrost']}           Wzrost: {zawodnik[2]['wzrost']}
    Waga: {zawodnik[0]['waga']}               Waga: {zawodnik[1]['waga']}              Waga: {zawodnik[2]['waga']}
    Siła: {zawodnik[0]['siła']}              Siła: {zawodnik[1]['siła']}              Siła: {zawodnik[2]['siła']}
    Szybkość: {zawodnik[0]['szybkość']}           Szybkość: {zawodnik[1]['szybkość']}          Szybkość: {zawodnik[2]['szybkość']}
    Wytrzymałość: {zawodnik[0]['wytrzymałość']}       Wytrzymałość: {zawodnik[1]['wytrzymałość']}      Wytrzymałość: {zawodnik[2]['wytrzymałość']}
        """)
    nr = int(input("PODAJ NUMER ZAWODNIKA: "))
    if nr == 1 or nr == 2 or nr == 3:
        break
    else:
        print("Nie ma takiego zawodnika!!!")
x = nr - 1
wygrane = 0
przegrane = 0
tyg = 5
i = 0
while i < len(przeciwnik):
    print("="*15)
    print("Aktualny przeciwnik: ")
    inf(przeciwnik[i])
    while tyg > 0:
        print("\nTwoja forma: ")
        forma(zawodnik[x])
        print("Tygodnie do walki: ", tyg)
        trening()
        tyg -= 1
    walka()
    print(f"Rekord: {wygrane} - {przegrane}")
    tyg += 5
    i += 1
print("="*15)
print(f"Kończysz kariere z rekordem: {wygrane} - {przegrane}")