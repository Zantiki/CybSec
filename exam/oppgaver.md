## 2020 1)
### a
Både blokkchiffer og strømmeschiffer er
symmetriske chifferen. Den største forksjellen er
at et strømmeschiffer operer bit-vis, eller tegnvis, 
hvor et blokk-siffer opererer i blokker av N størrelse.

### b
Nøkkel: V

Vi kan bruke
<a href="https://en.wikipedia.org/wiki/Tabula_recta">tabula recta</a>
for enkryptering og dekryptering.

_START_ enkryptert: USTART:KITRH
18-19-0-17-19

```
21+18%29=10 # K
18+19%29=8 # I
19+0=19 #T
0+17=17 #R
17+19%29=7 # H
```

_ÆJVULO_ dekryptert: FERDIG
```
26-9-21-20-11-14
21: V 
26-21 = 5 # F
9-5 = 4 # E
21-4 = 17 # R
20-17 = 3 # D
11-3 =  8 # I
14-8 = 6 # G
```

## 2020 2)

### a
Det diskrete logaritme-problemet er i korte trekk slik:
```shell script
Gitt variabler a, B som elementer av en mengde Zp
Finn en x >= 0 og x =< p slik at pow(a, x) = B, som elementer
i mengden Zp
```
### b
```
p = 23
5⁹ kongurens 11 (mod 23)
alfa = 11
a = 9
k = 3
b = 11⁹ % 23 = 19
x = 5
```
Enkryptering:
```
11³ % 23 = 20
19³ % 23 = 5
5 * 5 % 23 = 2
(ak, xbk) = (20, 2)

```
Dekryptering: 
```
20⁹ % 23 = 5
5⁻¹ = 14 # Samme som invers modulus
2 * 14  % 23 = 5
```

### c
Fordi at: 
```
5²² kongurent 1(%p)
```
Og 5 passer da definisjonen til primitiv rot

### d

```
a = log_g b
log2 11 (mod 13)
11 = 2^x % 13
m = |sqrt(12)| = 4
a = j * 4 + i
j | g^(m*j) % n
0 = 1
1 = 3
2 = 9
3 = 1
4 = 3

i | bg^-i
0 = 11
1 = 7 * 11 %13 = 12
2 = 10 * 11 %13 = 6
3 = 5 * 11 % 13 = 3

a = 1 * 4 + 3 = 7
a = 7 
```
## 2020 3)

### a
Message Authentication Code brukes til å sjekke
om innholdet til en kryptert melding er autentisk 
eller ikke og å bekrefte integriteten til en melding.

### b
En mac  er sikker om den ikke kan reproduseres fra 
et annet MAC, Meldings-par.

Med et MAC, Meldingspar kan man benytte seg av et kjent
klar-tekst angrep for å produsere en MAC for en 
brukerdefinert melding. Men kan også være en såkalt
(ems, Q)-Forfalsker

### c

```
d = 0100 0111 0010
# c = 0010 1110 0100
IV = 0000

d1 = 0000 xor 0100 = 0100
e1 = 0010
d2 = 0010 xor 0111 = 0101
e2 = 1010
d3 = 1010 xor 0010 = 1000

CBC-MAC av d: 1000 


```