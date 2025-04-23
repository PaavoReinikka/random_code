# Task descriptions.

## Task 1

Tehtäväsi on tutkia, voiko annetuista kolikoista muodostaa tietyn summan. Esimerkiksi kolikoista [1,2,5] voi muodostaa summan 13 (esimerkiksi 5+5+2+1) mutta kolikoista [2,4,6] ei voi muodostaa summaa 13.
Toteuta tiedostoon coinsum.py funktio can_create, jolle annetaan lista kolikoista ja tavoitteena oleva summa. Funktion tulee palauttaa True, jos summa voidaan muodostaa, ja muuten False.
Toteuta funktio tehokkaasti dynaamisen ohjelmoinnin avulla samaan tapaan kuin kurssimateriaalin esimerkeissä.

```py
def can_create(coins, target):
    # TODO

if __name__ == "__main__":
    print(can_create([1, 2, 5], 13)) # True
    print(can_create([2, 4, 6], 13)) # False
    print(can_create([1], 42)) # True
    print(can_create([2, 4, 6], 42)) # True
    print(can_create([3], 1337)) # False
    print(can_create([3, 4], 1337)) # True

```