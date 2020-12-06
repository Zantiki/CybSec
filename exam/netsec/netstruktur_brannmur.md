# Nettstruktur
## Grunnleggende utstyr
Rutere virker på nettverkslaget, hvor de har som jobb
å sende pakker med ip-protokollen videre til neste ruter
dersom målet ikke er i lokalnettet.

Rutere har generelt en brannmur som kan brukes til å blokkere
uønsket nettverkstrafikk på stort sett alle nettverks-lagene.

En svitsj skiller seg fra ruter i den forstand at den
delegerer pakker i samme ip-addresse v.i.a MAC-addresser.
Flere svitsjer koblet sammen, er fortsatt samme IP-nett.
## VLAN-Svitsj
Dersom man ønsker flere mindre nettverk kan man
benytte seg av såkalt VLAN. Ved hjelp av VLAN kan man så
samle alle de mindre nettverkene under en svitsj.
## Kombinert utstyr
Ved kombinert utstyr menes bokser som ofte tar av seg flere
nettverks-problemer. Vanligst er følgende:
* Hjemmeruter: Svitsj til LAN og WAN til ISP.
* Ruter med server
* VLAN-switch og ruter
## Nettverks-eksempler:
Et vanligfirma-nett har ofte følgende struktur:

En ruter og brannmur mot isp, en switch for firmanett
og en switch for tjenester som skal være offentlig tilgjengelige.
Wifi er ofte koblet direkte til første ruter.

Dersom nett er avhenger av tilgang-stryring så kan man sette
opp dette ved hjelp av VLAN f.eks (ansattnett, gjestenett, osv).
Dersom det ønskes å fullstendig isolere ett ip-nett må dette
gjøres med egen ruter.
Videre kan det også sies at sys-admin har sitt eget VLAN, som
kun rutes til disse admin-ene

For firmanett har man ofte en DMZ hvor vi har tjenester
vi ønsker at offentligheten skal ha tilgang til. Her 
er ofte et firmas trådløse nett isolert da det lettere kan
misbrukes utenifra.

Dersom man er avhenger av høy oppetid kan man velge å ha to nett,
fra to ISP-er, dette er allikevel dyrt og bør unngåes.



## Svitsjer og sikkerhet
### VLAN
VLAN er logisk avskilte nett under samme ip-nett. Disse
defineres ofte i ruter hvor visse porter mappes til
visse VLAN (med porter menes Ethernet-porter). 

Kommunikasjon mellom porter på samme VLAN går fritt, men
dersom man ønsker å kommunisere med en maskin på et annet VLAN må det 
gå igjennom ruter.

Ved å bruke VLAN og svitsjer har vi mer fleksibilitet, 
i den forstand at en svitsj kan kobles opp mot ethvert
nettverk i virksomheten og tryggere tilgansgstyring.
### Portlåsing med MAC
Brukes til å sørge for at kun spesifikke MAC-addresser
kan koble seg til en port i veggen. F.eks printer på offentlig sted.
Dette er dessverre ikke spesielt sikker da man strengt tatt
bare kan endre på MAC-addressen som nettverkskortet bruker.
### Portlåsing med IEEE 802.1X
Portlåsing via IEEE 802.1X er hakket tryggere enn MAC-låsing.

Ved tilkobling tar svitsjen kontakt med en RADIUS-tjener for å sjekke
om enheten er autentisert. Eutentiseringen gjøres ofte via
sertifikat og/eller brukernavn/passord.

### Problemer med VLAN-protokoller
Når man kobler opp en ny svitsj finnes det protokoller for
å automatisk sette VLAN-strukturen ved å kommunisere med
de andre svitsjene. Disse protokollene heter _DTP_ og
_VTP_

Dessverre åpner dette for muligheten til at et angriper kan late
som de er en svitsj og som følge få tilgang til samtlige LAN. Dette
kan unngåes ved å omkonfigurere alle porter som ikke er
koblet til andre svitsjer men prisen av dette, annulerer mye
av fordelen implementasjonen av protokollene hadde i utgangspunktet.
### VLAN-hopping
For _VTP_ og _DTP_ brukes trunking for å sette opp svitsjer
dette er implementert ved at ethernet-pakkene kapsles inn med
et ekstra felt som beskriver hvilket VLAN de er del av.

Dette kan utnyttes ved å bruke såkalt double tagging hvor
man pakker inn ethernet-pakkene med to vlan-felt. Når
pakken da formidles til det andre VLAN-et poppes den første
og VLAN-et vil tro at pakken tilhører den.

## Trusselbilde
### Kriminelle
Her er det snakk om destruktiv hacking og/eller
stjeling av konfidensiell informasjon. Ofte er det også
brukt såkalte bot-nets som samler opp sårbare maskiner for
utnyttelse i framtiden. Dersom man er en organsisasjon med
høy profil er sannsyneligheten for et angrep veldig høy.
### Forrædere
Disse er det ofte vaskelige å tilpasse seg, da de kjenner
nettverket fra innsiden og ofte også har tilgang.
### Skyen
Likt som outsourcing kan man ikke alltid stole på at ekstrene
tjenster har god nok sikkerhet. Dersom du ikke har en kontrakt
med en sky-tjeneste skylder de deg ingenting ved data-brudd. Spesilet
viktig er det å ta høyde for forskjeller i lover (GDPR f.eks).
### Fremmede Makter
Her er det største eksemplet Stuxnet (Iran-ormen), og 
som følge kan det ofte ha katastrofale følger.

Videre kan det også sies at enkelte land krever innsyn i PC
ved inngang igjennom toll. Da er det spesielt viktig og enten ikke
ha sensitiv informasjon på maskinen eller kryptere disken.
### Uhell/inkompetanse
Sier seg selv...


# Brannmur

en brannmur er et filter mellom flere nettverk som
begrenser viss type trafikk av sikkerhets-hensyn.
To utrykk står sentralt her:
* sikker: Her finner man ofte filtjener og vanlige PCer
  ofte ikke kontakbar for eksterne.
* DMZ: Ofte webserver og epost, ingen begrensing for eksterne

Merk at i disse tider er ofte faller disse under samme brannmur
i motestning til slik det var før, hvor man ofte brukte indre/ytre 
brannmur. Moderne brannmurer beskytter også nettene 
(i.e DMZ og sikker) mot hverandre.

Brannmurer er generelt koblet opp mot internett.

## Typer brannmurer
### Enkelt pakkefiler:
Brannmur får en pakke, og slår opp i reglene sine, dersom
pakken passer, får den komme videre. Dette gjelder både
mot internett og lokalt.
###  Innholdsfiltere
Ser mer helhetlig på innformasjonen motatt, f.eks
filtrere bilder ut av epost, java ut av nettsider, etc.
For å oppnå dette må brannmuren sette sammen flere pakker sekvensielt.
Generelt må innholdsfiltrerring håndteres av tjener/programvare
som er ansvarlig for  å behandle innholdet: i.e mailserver
filtrerer epost, en proxy kan håndtere executable is nettsteder
osv. Nettsteder filteres også ofte av nettleseren.
### Personlig Brannmur
Pakkefilter på enkeltmaskiner og/eller se på hva slags
programmer som kommuniserer med hva.

Til vanlig begrenses ofte UDP og ICMP som brukes til ping.
## Pakkefiltere
### Protokoller
Filtere pakker basert på protokoll
Til vanlig begrenses ofte UDP og ICMP som brukes til ping.
### Portnumre
Filtrere pakker basert på portnummer. I.e, er porten ikke åpen?
Blokker trafikk. Ofte nyttig om man vet at kommunikasjon
kun skal skje over en port.
### IP
Kan filtrere på falske iper (spoofing), tvilsomme ip-adresser (eller
hvilke som helst andre). Man kan også blokkere kjente 
angrepsaddresser.
### Source Routing
Sorce-routing er en teknikk hvor man spesifiserer hvilke
rutere en pakke skal innom, som kombinert med en falsk ip, 
kan lure mer intelligente filtere i en Brannmur.
### Umulige pakker:
Pakker som inneholder umulige flagg-kombinasjoner og/eller
ugyldige fragmenter kan kastes bort.

### Tilstands/sesjonsfilter
Ved å se på tilstanden til de forskjellige pakkene fra samme
kilde iforhold til hverandre kan vi vidre beslutte om dette
er uønsket trafikk eller ikke.
Under er noen eksempler:
* Sette sammen fragmenter og se på sammenheng
* Har pakkene en eksisterende forbindelse?
* Se om pakker av en viss protokoll oppfører seg som forventert.

## Utgåendefilter
Å filtere utgående trafikk kan også være nyttig, da en
av de interne maskinene kan være kompromittert og
rapporterer tilbake fra innsiden.
## Autentisering
Ofte kan man sette opp autentisering for å få tilgang
til å manipulere brannmuren, et eksempel på dette kan være
å blokkere tilgang til en ruters web-grensesnitt for
utenforsående.
## NAT
Brukes til å la flere maskiner dele på en ip-addresse
og gir som følge en viss grad av sikkerhet da det er umulig å 
opprette en forbindelse utenifra og innover. Dette beskytter
dessverre ikke mot utgående trafikk.

## Ruting
### Veifinning
Når man bruker trace-route blir det ofte blokkert
av brannmur da den bruker UDP-pakker, ved å sette flagget
-I eller -T + -p kan vi bruke ICMP og TCP respektivt.

Alternative programmer som scapy f.eks kan brukes for å plotte
en rute.
### Rutetabeller
Fungerer veldig enkelt ved at ruter med WAN port, har en tabell med

> maskin-ip | ruter-ip

slik at ved en tilkobling 
kan man slå opp målet og man vet hvor pakken skal next.
Vi skiller mellom forskjellige typer ruter:
* Direkte forbindelser: ruter er kjent med nettverk den 
sender data til, og legger den derfor direkte i rute-tabell.
* Statiske Ruter: Konfigureres av sys-admin, pain å endre.
* Dynamiske ruter: Ruter får melding om endringer og
  oppdaterer tabellene sine med den relevante protokollen.
* Default-rute: Er dit pakken blir sendt om den ikke finnes i
rute-tabellen.
### Interne Rute-protokoller
Brukes i administrative områder:
* RIP: Routing Info Protocol, Begrenser antall hopp til mål
kommuniserer med nabo hver 30. sek.
* EIGRP: Enhanced Interior Gateway Routing Protocol, baserer
seg på å se på mer komplektse effektiviserings-mål for raskere rute.
* OSPF: Open Shortest Path First, basert på å finne beste vei basert
på hastighetene på forbindelsene.
* IS-IS: Itermediate System to Itermediate System, Lik OSPF
med unntak av at den bruker CLNS istedet for IP-adresser for
  å utveksle informasjon mellom rutere.
### Eksterne Ruteprotokoller
Brukes for ruting mellom administrative områder.
BGP-4 er den mest brukte og baserer seg på distansevektorer og kommuniserer
over TCP. Dersom man er en større organisasjon  kan dette også
brukes internt på separate nett.
### Autentisering
For å unngå forfalskede rute-pakker kan man benytte seg
av autentisering. Dette gjøres hovedsaklig på to måter:
_Ubeskyttet_ _Autentisering_: nøkkel sendes med pakke og sjekkes
hos mottakende ruter. Problemet med ette er at man lett får tak 
  i nøkkelen ved hjelp av sniffing. Videre kan det også sies
  at slike nøkkler ofte har en levetid, som kan føre til at
  oppdateringer stopper ved utløpt nøkkel. Denne typen autentisering
  er god beskyttelse mot tapper, men dårlig mot angripere

_MD5_ _autetisering_: Likner ubskyttet autentisering, bare at
istedet for nøkkel er denne erstattet med en hash basert på pakkeinnhold
i.e hver pakke har forskjellig nøkkel. Denne hashen produseres med
MD5 algoritmen og sjekkes hos mottaker. Dette kan jobbes rundt ved
å sende samme pakke på nytt, men enkelte rutere tar høyde for dette
ved å ha sekvens-nummer i hver pakke sendt.

_IPsec_: Denne krypterer hele forbindelsen,
men er ofte ikke brukt pga overhead. MD5 er da alternativet.