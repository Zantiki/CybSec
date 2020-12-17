# 1
a)

En av ulempene ved at bibloteket er programert i 
C er at det lett kan oppstå bugs, feil og evt. exploits 
som relatert til håndtering med minne. Feil som dangling pointers,
buffer-overflow/overread. Vi kan også være utsatt for streng
-formaterings exploits og vi kan møte på en av de mange undefined 
behaviors i C. Allikevel er C et felksibelt kompilert språk som
egner seg godt for lav-nivås applikasjoner. Videre er C
også kompatibelt med de fleste systemer (spesielt Posix) da
det har en godt utviklet standard.

b)

Med tanke på at vi har en 95% dekningsgrad er det ikke særlig behov
for å skrive flere enhetstester. Når vi så setter opp CI-systemet
burde det gjøre tre ting:
* kjøre alle enhetstestene
* fuzze alle funksjoner som manipulerer minne på noe vis.
* benytte seg av address sanitizing

De to siste punktene tar da høyde for de viktigste svakhetene
i C-språket. Siden dette er et åpenkilde-bibilotek tar jeg
utgangspunkt i at versjonkontrollen er på GitHub. De kan da
intergrere travis som CI-system ved å legge til en travis.yml fil
i rooten til prosjektet. 

# 2
1)

Strengformattering kan utnyttes for å peke til flag-adressen. De
fleste andre angrep baserer seg på å utnytte buffer-overflow, noe vi ikke 
kan her. 
PIE gjør det også vanskelig for oss å finne addressene vi trenger fra stacken.

2)
Vi utnytter format-string for å kjøre flag. Vi er da nødt til å bestemme
addresserommet til stacken og så teste adresser til den forventede teksten 
skrives ut. Vi vi vet at vi er på et AMD-64 system kan vi slå opp spesifikasjoner
om addresserom osv for å etteforske dette.

# 3
Skriptet leter etter en spesifisert fil-type over hele systemet og fjerne det
Hvem som fjernet hva legges så inn i en log kalt script.log.

# 4
Vi bruker argumentene -print0 og -0 for å bruke en null
byte til terminering istedet for mellomrom, da xargs ofte
kan brukes til destruerende operasjoner og slette uforventede
ting dersom et filnavn inneholder mellomrom f.eks.

# 5
```shell
# $ filnavn
line_count=0
while IFS= read -r line
do
	$line_count=$(($line_count + 1))
done <`$1`
echo "antall linjer: $line_count"
```

# 6

## Problemer
* Problem 1: Plukklister via epost. Det er ingen garanti
at denne eposten er sikker nok, og det lekker nok mye info
fra lageret.
  
* Problem 2: bør ha brannmur uansett slik at firmanett ikke ble tatt
ned ved en infisert pc.
  
* Problem 3: Salgsjefen kommer til å havne på en spam-liste

* Problem 4: Dårlig tilgjengelighet og mangel av brannmur til filserver
## Løsninger og ønsker
Noen tiltak:
* Nett på lager, med plukkliste fra internt system.
  
* Brannmur mot ruter og svitjs med muligheter for VPN.
  
* Eget VLAN for personalsjef, gjerne med Radius autentisert
dersom man ønsker tråløs tilkobling. 
  
* Kurse ansatte (spesielt fra Lageret) om phising, tilgang
og drive med bearbeidende arbeid mot illojalle ansatte (se
  fallskjermordning).
  
* Interne og eksternt  tilgjengelige tjenester burde skilles
ved hjelp av DMZ i brannmur slik at salgssjef får det slik han vil

* Velger å ha fil-server sammen med resten av firma-nettet
med tanke på at vi vil at det skal være tilgjengelig via VPN 
og at Adm.dir ikke ønsker å bruke penger på to forskjellige VPN
  løsninger.