## Oppgave 1
### 1
64 for å overskrive streng-buffer + 8 for å overskrive
programpeker, totalt 72 tegn.
### 2
0x0000000000401163
### 3
toatlt addresserom:
401142 - 40116a
40 totale addresser
39² antall gjennomkjøringer for å få addresser til 
å overlappe.

## Oppgave 2
### a
importerer et etablert hash-biblotek og bruker
både på klient og server. Ved brukerinput av passord
hash og saltes det, som igjen hashes og saltes hos server, dette
slåes så opp i det tidligere lagret i databasen.
Videre kan det også sias at hashing ikke god nok
sikkerhet for kommunikasjon, så systemet burde også
ha HTTPS for å unngå sniffing.
Grunnen til at vi gjør det slik er for å 
unngå å ha klartekspassord lagret et noen somhelst
steder i systemet, samtidig som vi dobbelthasher for
å videre obfuskere for evt. angripere.
### b
Hvordan vi fjerner/overskriver passord er avhnger av
hva slags språk vi bruker. Dersom vi forholder oss
til C kan vi bruker free eller overskrive minneområdet.
I andre språk kan det være så ankelt at man bare assigner
en ny verdi til variabelen som holder dataen. 
Det beste er, slik beskrevet i a, å hashe umiddelbart
slik at du unngår å behandle passord i minnet.
### c
libFuzzer finner feil i kildekode ved å lage
inputpermutasjoner og kontinuerig analysere
hvordan en gitt funksjon reagerer. Videre har den
også relativt intelligent implementasjon av å genere
permutasjoner som produserer mest coverage av funksjonen.

I funksjonen gitt er sannsyneligheten høy for at vi får 
index-out of bounds, det er ingen sjekker for dette.
Som følge av buffer overrun av passord-streng. 
Dersom en string ikke innholder bokstaver og tall, vil
vi få en evig løkke, som kan lede til at i får integer overflow.

## Oppgave 6 + 7:
```shell
find / -name $1.docx -exec cp {} {}.backup
echo `whoami` kopierte $1 > > script.log
```
Dette scriptet finner alle docx-filer i systemets rot-mappe
og kopierer filene til en ny fil ved navn filnavn.backup.
Scripet tar så og appender hvem som flyttet hva til en
script-log.

```shell
find /mappesti -print0 | xargs -0 . . .
```
Disse parameterene forteller kommandoene at vi ikke
terminerer elementer ved mellomrom men med enn null-byte
istedet. Dette kan gi tryggre oppførsel ved visse xargs
operasjoner som f.eks rm, da find gi filnaven med mellomrom f.eks.

## Oppgave 8
Et pakkefilter fungerer ved å filtrere ut visse pakker ved hjelp av brannmur.
Disse bestemmes ofte etter protokoll, størrlse og/eller til-fra adresse. En nyttig
regel som nå er standard i de fleste brannmurer er å filtrer ut visse typer ICMP-pakker.
Det er noen tilfeller hvor ICMP-pakker er nyttige som ved pinging og vi kan f.eks filtrere
basert på antall pakker motatt/størrelse på pakker for å forebygge f.eks ping of death.

## Oppgave 9
Sette opp brannmur som filterer alt med unntak av http/https, VPN og smtp. Det kan
også være behov for å åpne opp for UDP. Avhenger av hvordan de ansatte jobber kan man
vurdere å åpne for SSH og ICMP, men vi unngår generelt å åpne for ting som kan bli utnyttet.
Denne brannmuren har en DMZ for webtjener
og epost-server.
I den sikre sonen av nettet har vi delt i to virituelle nett via en svitsj for tjenester
man kan koble seg til VPN med og et for tjenester man vil ha utilgjengelig for utsiden.
Filtjeneren bør gjøres tilgjengelig via VPN slik at ansatte kan hente bedriftens dokumenter.
Videre kan det også sies at vi burde separere i et tredje og fjerde nettverk. Det tredje 
for trådløst ansattnett og fjerde for sys-admin. Ansattnettet og VPN bør kun være tilgjengelig
ved hjelp av to-faktor autentisering for å forebygge evt. diginnbrudd. 
I forhold til fysiske sikringstiltak bør alle dører ha kort-lås og alle disker krypteres.
For å forebygge riskioer relatert til tap av arbeid og data bør man ha server-sentralen
i et vanntett sted, gjerne med batteristøm ved nødstilfeller.
Det viktigste vi kan kurse ansatte i er Phising og Social engineering da den menneskelige faktoren
ofte er den som feiler. Videre bør det innføres en streng policy på å varsle dersom man
ser uvedkommende i bygget. De burde også informeres om hvorfor passord ikke er nok og
to-faktor bør være obligatorisk.

Enkelt nettverkskart:
![A test image](map.png)