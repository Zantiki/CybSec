# Shellscripting
## xargs
Dersom du har en command som har output som en liste kan
xargs brukes til å passe hvert enkelt liste-element til
en viss kommando f.ex, for å slette alle text-filer:
```shell script
find ".txt" | xargs rm 
```
Vi kan også benytte oss av flere listelementer på en gang:
```shell script
ls | xargs -n 3 echo 
```
For å selv definere parameterene til en kommando, der {} er 
hvor parameterene fra xargs sendes inn:
```shell script
find . | xargs -I {} mv {}-old
```
Kjør 4 paralelle python-scripts.
```shell script
find -regex '*.py' | xargs -P 4 python {}
```
Merk at når man jobber med filnavn som har mellomrom i seg kan
det være en sikkerhetsrisiko.
## Grav aksent
\` \` er kjent som grav-aksent og brukes for å kalle kommandoer
ver den eller annen form for tilordning.
F.eks: 
```shell script
VARIABEL=`echo $USER`
echo `whoami`
``` 
## Doble og enkle apostrofer
Det er en liten forskjell mellom \" \" og \' \' i shellscripting
ved doble apostrofer utvides miljøvariabler. i.e
```shell script
echo "halla: $VARIABEL"
# Gir: halla bruker
echo 'halla $VARIABEL'
gir: 'halla $VARIABEL'
```
## Parametere
Typer parametere:
* $1-$N: er parametere tatt inn ved kjøring av kommandoen
* $0: Filnavnet til scriptet
* $*: alle parameterene tatt inn.

## basename og dirname
* Basename: gir oss siste del av en path
* Dirname: Gir oss pathen til den siste delen av input.
## Jobbe med linjer
* grep: finn linjer som inneholder en viss tekst
* wc: Tell antall ord
* cut: fjern ett visst område i teksten.
* uniq: fjern duplikater i en gitt tekst
* head: første linje
* tail: siste linje
## Read fil-input
Read kan lese fra fil, f.eks slik:
```shell script
NR=0
while read LINJE; do
  let NR=NR+1
  echo Linje $NR: $LINJE
done < $1
```

# oath
## Passord i minnet
Passord som er lest til minnet på backend er aldri helt trygge.
For å være sikker kan de hashes før lesing. Pass på at variabler
som inneholder passord blir destruert når de ikke trengs lengre.
## Open SSL
Open SSL er et c-biblotek som inneholder kryptografiske protokoller
, hash-funksjoner, symmetrisk og asymmetrisk enkryptering.
-Viktigt innhold:
* TLS
* MD5, SHA-1
* AES, RC4
* RSA, o.s.v
## HTTPS
Klartekst-passord skal aldri lagres, eller sendes noen plass.
_Alltid_ hash+salt. Man kan hverken stole på databasen eller server.
For å sørge for at vi ikke trenger å autentisere hver gang kan man
bruke access-tokens. Hash også på serversiden

HTTPS er vanlig HTTP over en encryptert TCP tilkobling ved
hjelp av TLS-sertifikater.
## Tokens
jwt-token funker bra på JS-server. Generelt består token av
4 deler:
* token-id
* bruker-id
* gruppe/rolle
* utløpsdato
Generelt gjelder følgende regler: Bruk alltid https, begrens
token-tilgangen til det som trengs. Sørg for at levetiden til Tokenet
ikke er lengre enn nødvendig. Ikke ha tokens i URL-en til siden. 
## To-Faktor
Består ofte av to deler, noe man vet og noe man har. Dette
er ofte mobil, sms, eller en token-generator. Slike token-generatorer
er da ofte sekvensbasert.