# Epost
Epost har noen sentrale svaketer og sikkerhetsproblemer:

* Spam
* Virus
* Phising
* Web bugs
* Avlytting
* Angrep

Den første epostormen utnyttet buffer-overflow i programmet
send-mail.

## Sikkerhetstiltak
### Filtre
Har brukes både inn og utfiltre for å begrense skade innad og
å motarbeide angrep utenifra. Normal filterer man ut executables
og scanner zippede vedlegg for kjente virus (denne typen sjekking
er avhenger av at vi vet hvilke virus vi forholder oss til).

### Svartelister
Svartelister brukes til å blokkere ut visse typer maskiner
som identifiserer via novn og ip, dersom man havner på en slik liste
kan det være vanskelig å komme seg av igjen.
### Velkonfigurert server
En god del open source epost-servere leveres helt åpnet
og det er derfor viktig å konfigurere serveren riktig. Det
er også verdt å notere seg at å sperre for uautorisert videresending
kun beskytter de utad systemet. Når det gjelder  kommersielle 
epost-tjenere er de ofte lettere å sette opp sikkert.
### Fornuftige klienter
Klienter som outlook er ofte sårbare, noe som kombinert med 
at brukere kjører mystiske programmer de får i posten,
kan lede til mange feil. Det kan derfor lønne seg å bruke
klienter som ikke er windows/outlook-basert.
### DNS-verifisering
Spammere bruker ofte midlertidig server uten DNS-records, 
vi kan derfor sjekke om dette er legitime server ved å slå dem opp
i dns-tabellen. Dette kan vi gjøre ved å sjekke om tjeneren faktisk
har et A-record. Når det gjelder individuelle eposter kan disse
slåes opp for å sjekke om MX-recorden faktisk eksisterer. Alle
disse tingene krever budsjett og kan inndras ved misbruk, noe
spammere er utsatt for.
### SPF
Også kjent som Sender Policy Framework.
En form for tilgang-styreing på hvem som kan/ikke
kan sende epost fra en tjener Disse lagres som et
TXT-record hos DNS. Dersom vi mottar en epost som ikke kommer
fra en godkjent tjener, kaster vi den vekk.
### SMTP auth
Dette brukes kun for utgående epost og implementeres ofte i form av
brukernavn og passord. Dette kobinerers ofte med TLS/SSL slik 
at utenforstående ikke kan få tak i passord med pakkesniffere.
### Grålister
Ofte følger ikke spammere eller virus normal epost-standard,
noe som kan utnyttes til å skille disse fra normale brukere.
Har introduserer man en forsinkelse som spammere ofte er 
sårbare for. 
### Brannmur
Her kan vi sette epost-server i dmz og kun tillate kommunikasjon
over smtp fra server til andre siden av brannmur. Dette gjelder 
både innkommende og utgående smtp-pakker.
### kryptering
Så enkelt som å kryptere filene du vil sende.
### Feller
Et typisk eksempel er en såkalt tjæregrop hvor vi lager en
"falsk" server med kunstige begrensninger for å betraktelig sakke
ned operasjonen til en spam-tjeneste.
### Vampyrer
Laster ned nettressurser igjen og igjen for å pumpe opp nettkostnadene til et gitt mål

# VPN
VPN er et alternativ til å åpne opp et gitt nettverk for verden,
hvor vi også har mulighet til å kryptere all trafikken.
VPN gir sikker tilgang til tjenester over et åpent nettverk.
Et VPN kalles ekte når tilgangen til nettverket er styr og at
uvedkommeded har innsyn i trafikken.

VPN har disse fordelene:
* Rimelig og fleksibelt alternativ
* ensete gode alternative til tilgang av interne tjenester fra
utsiden.
* Gir tilgang til tjenester normalt forbeholdt det lokale nettverket.

Vi skiller mellom to typer VPN:
* klient-VPN
* nettverk-nettverk-VPN

## VPN og kompleksitet
VPN er hakket mer komplekst en de normale protokollene 
vi forholder oss til. Dette er av mange grunner, hovedsakelig:

* mange ulike teknologier
* VPN-teknologi er stadig under utvikling
* implementasjon av protokoller snakker ikke
nødvendigvis godt sammen.
* Generelt en kompleks teknologi.
## VPN-løsninger
### IP-sec
IETF-utviklet sett med protokoller for å kommuniserer sikkert over
TCP/IP-laget. Formålet med IPsec er å tilby en generisk mekanisme
for sikker kommunikasjon over internett. IP sec tilbyr
autentisering, integritet og konfidensialitet. Her pakkes den
gamle ip-pakken inn i en ESP (encapsulating security payload) og
får en authentication header. IP-sec har to modus: transport
og tunnel. Tunnel brukes mellom nettverk og transport brukes mellom maskiner

ip-sec har ofte blitt rammet som den endelige løsningen til sikker
datakom er på grunn av kompleksitet, kompabilitet og bruk av
uvanlige protokoller og porter.
Følgende leverandører har tatt i bruk ip-sec:
* Checkpoint VPN
* Cisco VPN
* Windows

### Tunneler og virituelle nettverkskort
En av de mer populære metodene for å koble to maskiner sammen
over et VPN er ved såkalte virituelle nettverkskort. Dette fungerer
ved at to maskiner på et nettverk koblet til hverandre over et virituel
nettverkskort som så blir kryptert av VPN-programmvare.
### TLS, SSL, TCP og UDP
Et alternativ til VPN er å benytte seg av Peer-2-Peer, 
men dette er ikke sikkert i en kommunikasjonmessig forstand.
Derfor bør all VPN-kommunikasjon foregå over TLS/SSL (som er det samme)
slik at vi kan regne kommunikasjonen som sikker. 

Når det gjelder TCP (brukt av Microsoft) og UDP(brukt av openVPN)
gir hver protokoll pros og kons: 

TCP er tryggere og gir automatisk feilhåndering på bekostning
overhead og effektivitet. UDP er mindre trygt og krever at VPN
-programmet håndterer feil dersom noe skulle mangle i UDP-transmisjonen.
OpenVPN har en egen implementasjon av TLS som håndterer denne typen
feil.
### OpenVPN
Første skikkelige VPN med TLS som støttes cross-plattform. 
Her trenger man en VPN-access server på det aktuelle nettverket og 
og en klient for å koble sammen. OpenVPN støtter også Nettverk
til nettverk.
### SSTP
Står for secure socket protocol og er VPN bygd av MicroSoft.
Denne fungerer kort ved å opprette en p2p tilkobling og sende
https over TCP.
### Cisco VPN
Baserer seg på UDP-pakker som holdes sikker ved hjelp av DTLS
(Datagram Transport Layer security)
### Open SSH VPN
VPN bygd på SSH.
### PPTP
Er basert på arbeid gjort av microsoft og har nå blitt en standard.
PPTP er lett å ta i bruk på windows-stacken. Denne er allikvel svak
da krypteringsnøklene er bestemt som en funksjon av brukerens
passord.
### L2TP
L2TP er nok en microsoft-basert protokoll som bruker IPsec
til sin enkryptering.
### Web-basert VPN
Såkalt uekte VPN, hvor man sender klient gjennom proxy i nettleser
dette er også kjent som SSL-VPN. Med tanke på at dette er rent
web-leser-basert er det forholdsvist enkelt å sette opp/bruke.
Derfor har man sett stor vekst i denne delen av VPN-sektoren.
### Port Forwarding
Kombo av SSH og PPP for å ha sikker tunnelering mellom to addresser.
Her brukes ofte Open SSH da dette er den mest brukte SSH-implementasjonen.