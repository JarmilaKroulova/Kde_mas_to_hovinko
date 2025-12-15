import random
from zakladni_data import cara, domov, nazev, pravidla, moznosti, moznosti_polohy, volba_polohy


def uvitani():
    """
    Uvítá hráče, zobrazí pravidla a možnosti volby tipu.
    """
    print(f"\n{cara}\nVítej v tipovací hře")
    print(f"\n{cara}\n{nazev}")
    print(f"{cara}\nTato hra vznikla na motivy seriálu Jak jsem poznal vaši matku")
    print(f"{cara}\n{pravidla}\n{domov}\n{moznosti}")


def zpracovani_vstupu(poloha_hovinka, pocet_pokusu):
    """
    Přijme a zpracuje vstup od hráče. Pracuje s dvěma parametry:
    
    param poloha_hovinka: náhodně vygenerovaná poloha ze slovníku možností
    param pocet_pokusu: slouží k počítání pokusů, nutných k uhádnutí polohy, defaultně 0
    """
    try:
        while True:
            volba = input("Takže? Kde máš to hovínko? (Zadej 1 - 10):  ").strip().lower()
            pocet_pokusu += 1
            if not volba in volba_polohy:
                print("Tohle ani nezkoušej!")
                continue      
            volba_slovnik = moznosti_polohy[volba]
            if volba_slovnik != poloha_hovinka:
                print(f"Tvůj tip - {volba_slovnik} je těsně vedle, zkus to znovu!")
                print(f"Toto byl tvůj {pocet_pokusu}. pokus.")
                continue
            else:
                print(f"\n{cara}\nHovínko nalezeno! Bylo {volba_slovnik}. Teď jen uklidit :oD")
                print(f"Zvládl jsi to na {pocet_pokusu}. pokus. Gratuluji.\n{cara}\n")
                return False
    except Exception as e:
        print(f"Promiň, zachytil jsem chybu {e}, zkus to znovu")

    

def hlavni_hra():
    """
    Ovládá hlavní mechanismus hry.
    """
    poloha_hovinka = moznosti_polohy[random.choice(volba_polohy)]
    uvitani()
    pocet_pokusu = 0
    poloha = poloha_hovinka
    # print(poloha)
    zpracovani_vstupu(poloha, pocet_pokusu)

if __name__ == "__main__":
    hlavni_hra()