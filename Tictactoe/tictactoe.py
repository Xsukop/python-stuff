def vytvor():
    # Inicializujeme prázdne políčka
    row1 = [' ' for _ in range(3)]  # 3 prázdne políčka v riadku
    row2 = [' ' for _ in range(3)]  # 3 prázdne políčka v riadku
    row3 = [' ' for _ in range(3)]  # 3 prázdne políčka v riadku
    return row1, row2, row3

def zobraz(row1, row2, row3):
    print(f"{row1}\n{row2}\n{row3}")

def tah():
    while True:
        x = int(input("Vyber riadok (1-3): "))
        y = int(input("Vyber stĺpec (1-3): "))
        if 1 <= x <= 3 and 1 <= y <= 3:
            break
        else:
            print("Prosím vlož čísla od 1 do 3!")
    return x, y

def zmen(row1, row2, row3, x, y, player):
    if x == 1:
        row1[y - 1] = player  # Zmena hodnoty v row1
    elif x == 2:
        row2[y - 1] = player  # Zmena hodnoty v row2
    else:
        row3[y - 1] = player  # Zmena hodnoty v row3

def kontrolavyhry(row1, row2, row3):
    # Skontrolujeme riadky
    for row in [row1, row2, row3]:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True  # Ak sú všetky tri hodnoty rovnaké a nie sú prázdne

    # Skontrolujeme stĺpce
    for col in range(3):
        if row1[col] == row2[col] == row3[col] and row1[col] != ' ':
            return True  # Ak sú všetky tri hodnoty v stĺpci rovnaké a nie sú prázdne

    # Skontrolujeme diagonály
    if row1[0] == row2[1] == row3[2] and row1[0] != ' ':
        return True  # Ak sú hodnoty na diagonále rovnaké a nie sú prázdne
    if row1[2] == row2[1] == row3[0] and row1[2] != ' ':
        return True  # Ak sú hodnoty na druhej diagonále rovnaké a nie sú prázdne

    return False  # Ak žiadna z podmienok nie je splnená, hra ešte nebola vyhraná



    
def game():
    row1, row2, row3 = vytvor()
    player = 'X'  # Začína hráč 'X'
    
    while True:
        zobraz(row1, row2, row3)
        
        # Získanie ťahu
        x, y = tah()
        
        # Kontrola, či je políčko už obsadené
        if (x == 1 and row1[y - 1] != ' ') or \
           (x == 2 and row2[y - 1] != ' ') or \
           (x == 3 and row3[y - 1] != ' '):
            print("Toto políčko je už obsadené, vyber iné!")
            continue
        
        # Zmena políčka na aktuálneho hráča
        zmen(row1, row2, row3, x, y, player)
        if kontrolavyhry(row1, row2, row3):
            zobraz(row1, row2, row3)
            print(f"Hráč {player} vyhral!")
            break  
        # Striedanie hráčov
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

game()