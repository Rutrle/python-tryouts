# disclaimer: tento kód je v pythonu, ne v C, takže se syntace občas může lišit, ale snad to půjde pochopit
# chci 5 krát vytisknout "Hello world" a zároveň i info pokolikátý to tisknu
# buďto to můžu napsat 5 krát za sebou:

print('1')
print('Hello world')

print('2')
print('Hello world')

print('3')
print('Hello world')

print('4')
print('Hello world')

print('5')
print('Hello world')

print('\n')  # odskoč o řádek

# todle sice funguje, ale
# 1) je to opruz psát a to je to jenom 5*, normálně není problém setkat se s něčim
#  co chci udělat třeba milionkrát (a klidně i víc), nemluvě o tom jaký peklo by bylo takovejdle program číst
#  (sidenote: průměrný kód výrazně víc času čteme než píšeme )
# proto existují cykly, třeba for cyklus, v případě že bych chtěl 5* vytisknout jenom "Hello world", udělám to takhle:

for i in range(1, 6):  # Pro i (může být cokoli jiného, ale i je takové oblíbené, i když je často lepší použít něco popisnějšího) od 1 do 5 (s krokem 1; 6 v kódu je proto jak je v pythonu definovaná funkce range)
    print('Hello world')


print('\n')  # odskoč o řádek
# každému proběhnutí cyklu se říká iterace, jedna iterace taky odpovídá vytisknutí "Hello world"
# promněnná i se po každé iteraci zvýší o 1 (je to takhle defaultně u for cyklu), takže kdybych chtěl vytisknout i ty čísla jako předtím, můžu udělat:
for i in range(1, 6):
    print(i)
    print('Hello world')


print('\n')  # odskoč o řádek

# nicméně todle občas nejde, anebo chceme aby se v každém cyklu zvýšila o 1 jiná promněnná než y, což se dá zapsat jako:
# důvod proč to občas nejde je že třeba iterujeme ne přes čísla ale přes členy nějaké množiny (např. tuple )
n = 0  # počáteční definice promněnné
l = 0  # počáteční definice promněnné
for i in range(1, 6):
    # todle je takový ten klasický způsob - v každém cyklu (iteraci) se k n přičte 1  a uloží se do promněnné n
    n = n+1
    l += 1  # todle je to samé, jenom je to zkrácený zápis, který se čte lépe a je pokud se nepletu v pythonu, ale v C ne
    # i++    =>kdyby tento kód nebyl v pythonu ale v C, todle by se chovalo úplně stejně jako předchozí dva řádky
    print('l je:')
    print(l)

    print('n je:')
    print(n)
