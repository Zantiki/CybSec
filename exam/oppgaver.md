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

i | bg^-i # modular inverse?
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

# 2019 1)
Generell definisjon:
```shell
E(x) = (ax+b) mod m
D(x) = (invers mod a)*(x-b) mod m
```
```shell
a)
E(20) = 303 % 26 = 17

b)
D(25) = 7 * 22 % 26 = 24
D(11) = 7 * 8 % 26 = 4
D(13) = 7 * 10 % 26 = 18
D(x) = 24-4-18

c)
Det finnes 12*26 unike nøkler for et affint chiffer
med alfabetstørrelse 26, da det er 12 primtall mindre
enn 26 i dette området.

d)
  definisjon idepotent: kun nyttig å gjennomføre operasjon
  en gang. Funksjonen er ikke indepotent.
``` 

# 2019 2)
a) 
En kryptografisk hashfunksjon er når man produserer en output 
på fast lengde basert på et input av vilkårlig lengde. Disse
brukes ofte for å verifisere integriteten til en gitt melding.

b) 
Følgende problemer må være vanskelige å løse dersom en hash skal være sikker:

* Første preimage-problem: dersom du har h og y finn en h(x) = y
* andre preimage-problem: dersom du har h og x, finn en h(x2) = h(x)
* kollisjon-problemet: gitt en h finn en x og en x2 som ikke er lik,
  hvor h(x2) = h(x)
  
Et bursdagsangrep er å generere tilfeldige hasher fram til det er mer enn 50%
sannsynelighet for at to av heshene er like. Dette forutsetter at første
preimage-problem er løst.

c)
En MAC har som hensikt å holde styr på integriteten til en melding
og hasher kan derfor brukes til dette. Generelt er MAC-er sikrere
da de ofte kobinerer hash-familier med itererende hashing, slik at hash er
vanskelig å re-produsere.

# 2019 3)
a) primtallene 47 og 59 vi lede til flest
løkkegjennomkjøringer og er derfor mest arbeidskrevende.

b)
```shell
61*71 = 4331

-steg1:
a = 2
i = 2
n = 4331
a = 4
d = gcd(3, 4331) = 1, fortsetter

-steg2:
a = 4
i = 3
a = 64
d = gcd(63, 4331) = 1, fortsetter

-steg3:
a = 64
i = 4
a = 3253
d = gcd(3252, 4331) = 1, fortsetter

-steg4:
a = 3253
i = 5
a = 2380
d = gcd(2379, 4331) = 61, avslutter

sjekker: 4331 / 61 = 71 er riktig.
```

# Høst 2018
## 1)
### a
Den mest grunnleggende forskjellen mellom symmetriske og
assymtriske kryptosystemer at at symmertriske benytter seg av en 
enslig nøkkel mens asymmetriske krypto-systemer bruker bruker
offentlig og privat nøkkel for å løse nøkkeldistribusjopnsproblemet.
Slike systmer kan ikke være ubetinget sikkert da de krever en 
enveis-funksjon, men de regnes som computationally secure.

### b 
PBKDF2 brukes til key-streching slik at alle chifferblokker er av lik lengde. ECB er bare ren kryptering.
PBKDF2 involverer i korte trekk å bruke den tidligere blokken  som del av enkrypteringen til den nye. På denne
måten kan vi fortsatt dekryptere med xen inverse funksjonen, men vi er mindre sårbare for ting som frekvensanalyse. videre
kan det også sies at å ha fast lengde på chiffertekst er å fortrekke for tigjengelihetsens skyld. Videre kan det også sies at hver blokk
har hver sin nøkkel og man kan ikke produsere klarteksten uten å ha alle nøklene.

## 2)
### a
Den signerte meldingen er ikke gyldig da
p og q må være primtall. Siden 32 er 
nøkkelen er dette ikke tilfellet. Videre kan det
også sies at n ikke er delelig på noen av verdiene i den
private nøkklen.

### b
```shell
n = 1403

mens d==1
a = 2
i = 2

a = a**i % n
d = gcd(a-1, n) = 1, fortsetter
i+=1

a = 4
d = 1
i = 3

a = 64
d = 1
i = 4

a = 142
d = 1
i = 5

a = 794
d = 61, break;

sjekker: 1403 / 61 = 23, som er et primtall.
```

Dette utgjør et angrep mot RSA da vi bestemmer primtalls
faktorene og kan bruke dette til å beregne den fulle nøklen.

## 3)
Dette vil ikke nødvendigvis øke sikkerheten 
da permutasjonen kan representeres som en operasjon-matrise
noe som i konteksten til Hill-chiffret blir som å bruke en annen nøkkel.
Dette øker ikke kompleksiteten eller computational kostnad. Detter
er også fordi at hill-chifferet er indepotent.

# Vår 2019
## 4)
PBKDF2 er en hash-funksjon som enten forlenger eller forkorter (i tillegg
til å returnere en chiffertekst) en gitt klartekst. For at denne skal bli
betraktet som "sikker" bør den brukes sammen med andre krytpografiske 
funskjoner som f.eks SHA. Normal tar PBKDF" inn følgende argumenter:
klartekst, salt og antall iterasjoner.

## 5)
Den av de største sikkehetsmessige gevinsten bak et assymetrisk chiffer
er at man løser nøkkeldistrubusjonsproblemet da RSA er en såkalt enveisfuksjon.
Dette betyr at RSA f.eks krever separate nøkler for å enkryptere/dekryptere.
Dette er ikke tilfellet for symmetriske nøkkler da disse også har behov for
trygg kanal for deling av nøkkel.
En ulempe med slike enveisfunksjoner er at de ikke er ubetinget sikre, men
de regnes som computationally secure ved godt valg av nøkkel.
En annen fordel med RSA er at den ikke er imdeponent og at det er et produkt
chiffer, noe som som gjør det serdeles vanskelig å brute-force uten å kjenne til
deler av nøkkel.
## 6)
Siden blokkstørrelsen er to gjøres utregningen på følgende måte:

```shell
x = [[04, 10]
     [03, 00]]
     
e = [[23, 05],
     [20, 06]]
     
 # Hill chiffer er definert som:
 e = x*K og x = e*K⁻¹
 # K = e/x =[[292, 69], [80, 15]]
 K = e * x⁻¹= [[107, 98], [230, 200]] = [[16, 8], [14, 19]]
 K⁻¹ = [[16, 8], [14, 19]] # mutliplkativ invers av K.
 
```

## 7)
En mac er en kode basert på innholdet i en tekst som brukes til å
verifisere autentisitet og integritet til en gitt melding. hamc er en hash-basert
amc, i.e en mac av faste lengde. Et CBC-Mac er en noe sikrere variant av en
HMAC der man utfører en blokkvis xor-operasjon på tidligere mac, klartekst par
for å sikre integriteten til en gitt melding

## 8)
```shell
a = j * m + i
g = 7
b = 12
x = log_7 12 (mod 23)
12 = 7^x % 23
7 er primitiv mod 23
m = sqrt(22) = 5

table1:
0 1.0
1 28.0
2 32.0
3 3.0
4 36.0
5 21

moduler inverse 
table2:
1 12
2 5
3 14
4 7
5 15
```

