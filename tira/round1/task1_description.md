# Task descriptions.

## Task 1

Avainkoodissa on neljä numeroa väliltä 1 \dots 9. Koodissa ei esiinny kahta
kertaa samaa numeroa. Annettuna on koodin kuvaava merkkijono. Jokainen merkki on joko koodissa esiintyvä numero tai merkki ?, joka tarkoittaa tuntematonta numeroa. Tehtäväsi on muodostaa lista mahdollisista koodeista. Esimerkiksi kun merkkijono on 24?5, mahdolliset koodit ovat 2415, 2435, 2465, 2475, 2485 ja 2495. Toteuta tiedostoon keycode.py funktio find_codes, jolle annetaan parametrina koodin kuvaus merkkijonona. Funktion tulee palauttaa lista, jossa on pienimmästä suurimpaan kaikki koodit merkkijonoina. Funktion tulee toimia tehokkaasti kaikissa tapauksissa.

```python
def find_codes(pattern):
    # TODO

if __name__ == "__main__":
    codes = find_codes("24?5")
    print(codes) # ['2415', '2435', '2465', '2475', '2485', '2495']

    codes = find_codes("1?2?")
    print(codes[:5]) # ['1324', '1325', '1326', '1327', '1328']
    print(len(codes)) # 42

    codes = find_codes("????")
    print(codes[:5]) # ['1234', '1235', '1236', '1237', '1238']
    print(len(codes)) # 3024
```

*The solution is implemented in keycode.py*

## Task 2

Tehtäväsi on muodostaa kaikki sanat, jotka saadaan annetun sanan kirjaimista ja joissa ei ole peräkkäin kahta samaa kirjainta.
Tässä sana tarkoittaa mitä tahansa kirjainyhdistelmää, eikä sen tarvitse olla esimerkiksi suomen kielen sana. Esimerkiksi jos sana on kala, halutut sanat ovat akal, akla, alak, alka, kala ja laka.
Toteuta tiedostoon allwords.py funktio create_words, jolle annetaan sana. Funktion tulee palauttaa listana kaikki halutut sanat aakkosjärjestyksessä.
Voit olettaa, että sanan pituus on välillä  1 $\dots$ 8 merkkiä. Funktion tulee toimia tehokkaasti kaikissa tällaisissa tapauksissa.

```python
def create_words(word):
    # TODO

if __name__ == "__main__":
    print(create_words("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create_words("aab")) # ['aba']
    print(create_words("aaab")) # []

    print(create_words("kala"))
    # ['akal', 'akla', 'alak', 'alka', 'kala', 'laka']

    print(create_words("syksy"))
    # ['ksysy', 'kysys', 'skysy', 'syksy', 'sykys', 'sysky', 
    #  'sysyk', 'yksys', 'ysksy', 'yskys', 'ysyks', 'ysysk']

    print(len(create_words("aybabtu"))) # 660
    print(len(create_words("abcdefgh"))) # 40320
```

*The solution is implemented in allwords.py*

## Task 3

Sinulla on korttipelissä kädessä tietyt kortit ja sinun tulisi löytää korttien yhdistelmä, jonka summa on haluttu. Montako tällaista yhdistelmää korteista voi muodostaa?
Tässä tehtävässä kortit esitetään lukujen listana. Esimerkiksi lista [2,1,4,6] tarkoittaa, että kädessä on neljä korttia, joiden arvot ovat 2, 1, 4 ja 6. Korttien mailla (esim. risti) ei ole merkitystä tehtävässä.
Esimerkiksi kun kortit ovat [2,1,4,6] ja haluttu summa on 6, tällainen yhdistelmä voidaan muodostaa kahdella tavalla. Yksi tapa on valita kortit 2 ja 4, ja toinen tapa on valita pelkkä kortti 6.
Toteuta tiedostoon cardgame.py funktio count_combinations, jolle annetaan parametrina korttien arvot listana ja haluttu summa. Funktion tulee palauttaa yhdistelmien määrä.
Voit olettaa, että korttien määrä on välillä 1 $\dots$ 10. Funktion tulee toimia tehokkaasti kaikissa tällaisissa tapauksissa.

```python
def count_combinations(cards, target):
    # TODO

if __name__ == "__main__":
    print(count_combinations([2, 1, 4, 6], 6)) # 2
    print(count_combinations([1, 1, 1, 1], 2)) # 6
    print(count_combinations([2, 1, 4, 6], 15)) # 0
    print(count_combinations([1], 1)) # 1
    print(count_combinations([1, 2, 3, 4, 5], 5)) # 3
    print(count_combinations([1, 1, 4, 1, 1], 4)) # 2
    print(count_combinations([1] * 10, 5)) # 252
```

## Task 4

Annettuna on lista, jossa on kokonaislukuja. Tehtäväsi on selvittää, voiko luvut jakaa kahteen listaan niin, että molemmissa listoissa lukujen summa on sama.
Esimerkiksi kun lista on [1,2,3,4], voidaan muodostaa jako listoihin [1,4] ja [2,3], jossa kummankin listan lukujen summa on 5. Sen sijaan listassa [1,2,3,5] missään jakotavassa listojen lukujen summa ei ole sama.
Toteuta tiedostoon samesum.py funktio check_sum, jolle annetaan lista luvuista. Funktion tulee palauttaa True, jos jako on mahdollinen, ja muuten False.
Voit olettaa, että lukujen määrä on välillä 1 $\dots$ 10. Funktion tulee toimia tehokkaasti kaikissa tällaisissa tapauksissa.

```py
def check_sum(numbers):
    # TODO

if __name__ == "__main__":
    print(check_sum([1, 2, 3, 4])) # True
    print(check_sum([1, 2, 3, 5])) # False
    print(check_sum([0])) # True
    print(check_sum([2, 2])) # True
    print(check_sum([2, 4])) # False
    print(check_sum([1, 5, 6, 3, 5])) # True
    print(check_sum([1, 5, 5, 3, 5])) # False
    print(check_sum([10**9, 2*10**9, 10**9])) # True
    print(check_sum([1, 1, 1, 1, 1, 1, 1, 1, 1, 123])) # False
```

## Task 5

Tehtäväsi on pakata annetut tuotteet laatikoihin. Tiedossasi on kunkin tuotteen paino sekä suurin sallittu tuotteiden yhteispaino laatikossa. Montako laatikkoa tarvitset vähintään?
Esimerkiksi jos tuotteiden painot ovat [2,3,3,5] ja laatikon maksimipaino on 7, tarvitaan vähintään kaksi laatikkoa:

Laatikko 1: tuotteiden painot 2 ja 5 (yhteispaino 7)
Laatikko 2: tuotteiden painot 3 ja 3 (yhteispaino 6)

Toteuta tiedostoon boxweight.py funktio min_count, jolle annetaan tuotteiden painot sekä laatikon maksimipaino. Funktion tulee palauttaa pienin laatikoiden määrä. Jos tehtävä on mahdoton, funktion tulee palauttaa -1.
Voit olettaa, että tuotteiden määrä on välillä 1 $\dots$ 8. Funktion tulee toimia tehokkaasti kaikissa tällaisissa tapauksissa.

```py
def min_count(weights, max_weight):
    # TODO

if __name__ == "__main__":
    print(min_count([2, 3, 3, 5], 7)) # 2
    print(min_count([2, 3, 3, 5], 6)) # 3
    print(min_count([2, 3, 3, 5], 5)) # 3
    print(min_count([2, 3, 3, 5], 4)) # -1

    print(min_count([], 1)) # 0
    print(min_count([1], 1)) # 1
    print(min_count([1, 1, 1, 1], 1)) # 4
    print(min_count([1, 1, 1, 1], 4)) # 1

    print(min_count([3, 4, 1, 2, 3, 3, 5, 9], 10)) # 3
```

## Task 6

Sinulle annetaan etäisyystaulukko, joka ilmaisee kunkin kahden kaupungin välisen etäisyyden. Kaupungit on numeroitu 1 \dots n.
Etäisyystaulukko voi näyttää vaikkapa seuraavalta:
$$
\begin{matrix}
0 & 2 & 2 & 1 & 8 \\
2 & 0 & 9 & 1 & 2 \\
2 & 9 & 0 & 8 & 3 \\
1 & 1 & 8 & 0 & 3 \\
8 & 2 & 3 & 3 & 0 \\
\end{matrix}
$$
Tässä tapauksessa kaupungit ovat 1 \dots 5. Esimerkiksi kaupunkien 2 ja 3 välinen etäisyys on 9. Tämä etäisyys on taulukossa rivin 2 sarakkeessa 3 sekä rivin 3 sarakkeessa 2.
Tehtäväsi on etsiä lyhin reitti, joka lähtee kaupungista 1, käy kaikissa muissa kaupungeissa ja palaa lopuksi takaisin kaupunkiin 1. Jos reittejä on useita, tulee valita reitti, joka siirtyy joka askeleella kaupunkiin, jonka numero on mahdollisimman pieni. Äskeisessä etäisyystaulukossa haluttu lyhin reitti on $1 \rightarrow 3 \rightarrow 5 \rightarrow 2 \rightarrow 4 \rightarrow 1$, jonka pituus on 9.
Toteuta tiedostoon visitall.py funktio find_route, jolle annetaan etäisyystaulukko listana listoja. Funktion tulee palauttaa parina lyhimmän reitin pituus sekä esimerkki tavasta muodostaa reitti.
Voit olettaa, että kaupunkien määrä etäisyystaulukossa on välillä 2 \dots 8. Funktion tulee toimia tehokkaasti kaikissa tällaisissa tapauksissa.

```py
def find_route(distances):
    # TODO

if __name__ == "__main__":
    distances = [[0, 2, 2, 1, 8],
                 [2, 0, 9, 1, 2],
                 [2, 9, 0, 8, 3],
                 [1, 1, 8, 0, 3],
                 [8, 2, 3, 3, 0]]

    length, route = find_route(distances)
    print(length) # 9
    print(route) # [1, 3, 5, 2, 4, 1]

    distances = [[0, 7, 5, 9, 6, 3, 1, 3],
                 [7, 0, 3, 2, 3, 3, 7, 8],
                 [5, 3, 0, 4, 2, 7, 7, 1],
                 [9, 2, 4, 0, 2, 3, 2, 4],
                 [6, 3, 2, 2, 0, 9, 5, 9],
                 [3, 3, 7, 3, 9, 0, 4, 5],
                 [1, 7, 7, 2, 5, 4, 0, 7],
                 [3, 8, 1, 4, 9, 5, 7, 0]]

    length, route = find_route(distances)
    print(length) # 18
    print(route) # [1, 7, 4, 6, 2, 5, 3, 8, 1]

```

## Task 7

Kokonaisluku on nouseva, jos jokainen numero on sama tai suurempi kuin edellinen numero. Esimerkiksi luvut 2, 347 ja 25568 ovat nousevia.
Tehtäväsi on laskea, montako nousevaa tietyn pituista kokonaislukua annetuista numeroista voidaan muodostaa.
Esimerkiksi kun luvun pituus on 3 ja sallitut numerot ovat 1, 2 ja 3, haluttu vastaus on 10, koska tässä tapauksessa nousevat luvut ovat 111, 112, 113, 122, 123, 133, 222, 223, 233 ja 333.
Toteuta tiedostoon incnum.py funktio count_numbers, jolle annetaan luvun pituus ja sallitut numerot merkkijonona. Funktion tulee palauttaa nousevien lukujen määrä.
Funktion tulee toimia tehokkaasti, kun luvun pituus on 1 $\dots$ 10 numeroa.

```py
def count_numbers(length, numbers):
    # TODO

if __name__ == "__main__":
    print(count_numbers(3, "123")) # 10
    print(count_numbers(5, "1")) # 1
    print(count_numbers(2, "137")) # 6
    print(count_numbers(8, "25689")) # 495
    print(count_numbers(1, "0")) # 1
    print(count_numbers(2, "0")) # 0
    print(count_numbers(10, "12")) # 11
    print(count_numbers(10, "123456789")) # 43758
```

Huomaa, että nousevassa luvussa ei saa olla etunollaa, jos luvussa on kaksi tai useampia numeroita. Tämän takia esimerkiksi 00 ja 012 eivät ole nousevia lukuja, mutta 0 on nouseva luku.

## Task 8

Avainkoodissa on neljä numeroa väliltä 1 \dots 9. Koodissa ei esiinny kahta kertaa samaa numeroa.
Sinulle on annettu olio ("oraakkeli"), jonka sisällä on salainen avainkoodi. Tehtäväsi on selvittää koodi tekemällä kyselyitä oraakkelille. Jokainen kysely on avainkoodi ja oraakkeli kertoo, moniko numero on oikealla paikalla koodissa ja moniko numero kuuluu koodiin mutta on väärällä paikalla.
Esimerkiksi jos oikea koodi on 4217 ja teet kyselyn 1234, oraakkeli antaa vastauksena luvut 1 ja 2. Tämä tarkoittaa, että yksi numero (2) on oikealla paikalla koodissa ja lisäksi kaksi numeroa (1 ja 4) kuuluvat koodiin mutta niiden paikat ovat väärät.
Tehtävän haasteena on, että saat tehdä enintään 16 kyselyä oraakkelille. Tämän jälkeen sinun täytyy pystyä ilmoittamaan salainen koodi.
Jokaisessa kyselyssä oraakkelille tulee olla kelvollinen avainkoodi. Huomaa erityisesti, että koodissa ei saa olla kahta samaa numeroa eli esimerkiksi koodi 1212 ei kelpaa.
Toteuta tiedostoon findcode.py funktio find_code, jolle annetaan parametrina oraakkeli. Funktion tulee kutsua oraakkelin metodia check_code, joka palauttaa vastauksen kahden kokonaisluvun parina.
Funktio ei saa yrittää selvittää vastausta oraakkelilta muulla tavalla kuin kutsumalla metodia check_code. Palvelimella oleva oraakkeli saattaa erota tehtäväpohjan toteutuksesta.

```py

import re

class Oracle:
    def __init__(self, code):
        self.code = code
        self.counter = 0

    def check_code(self, code):
        self.counter += 1
        if self.counter > 16:
            raise RuntimeError("too many check_code calls")

        if type(code) != str or not re.match("^[1-9]{4}$", code) or len(code) != len(set(code)):
            raise RuntimeError("invalid code for check_code")

        in_place = in_code = 0
        for pos in range(4):
            if code[pos] in self.code:
                if code[pos] == self.code[pos]:
                    in_place += 1
                else:
                    in_code += 1

        return in_place, in_code

def find_code(oracle):
    # TODO

if __name__ == "__main__":
    # esimerkki oraakkelin toiminnasta
    oracle = Oracle("4217")
    print(oracle.check_code("1234")) # (1, 2)
    print(oracle.check_code("3965")) # (0, 0)
    print(oracle.check_code("4271")) # (2, 2)
    print(oracle.check_code("4217")) # (4, 0)

    # esimerkki funktion find_code toiminnasta
    oracle = Oracle("4217")
    code = find_code(oracle)
    print(code) # 4217
    
```