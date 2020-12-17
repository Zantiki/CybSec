# IDS og IPS
Brukes oftest til å lete etter tegn til innbrudd, eller om det har skjedd.
IPS står for in trusion prevention system, IDS for intrusion detection system.
Forskjellen er hovedsakelig at IPS forsøker å reagere på det den oppdager, noe en IDS ikke
gjør.
## HIDS
Står for Host intrusion Detection system. Det lages en sjekksum av maskinens
innhold som HIDSen så har kontroll over, ved uregemessigheter kan sys-admin 
varsles.
## HOST-IPS
Her konsulteres programvaren hver gang en fil åpnes, og det vil vurdere om
noe er trygt å gjøre eller ikke. De fleste anti-virus programmene fungerer på
denne måten. For å unngå at dette går utover effektivitet kan man begrense dette
til systemfiler.
## NIDS
Network intrusion detection system oppdager innbrudd og forsøk i et gitt 
nettverk. Dette settes opp til å fange trafikk som passerer et netteverkort.
Dette er ofte en maskin som er plugget imellom svitsj og nettverk som sender
trafikk videre. Alternativt kan det også kjøres direkte på ruter.

## IPS for Nettverk
NIDS kan bli et IPS ved å konfigurere om, slik at det sender beskjeder til
brannmurer og eller anndre sikkerhets-enheter. -kan også brukes til å blokkere
ip-er som pingscanner nettverket. Generelt er et NIPS avhenger av å kunne
snakke med andre programmer/maskiner for å fungere.

## IPS Farer:
Dersom man bruker ips ukritisk kan det lede til uforutsette konsekvenser. 
F.eks kan det lures til å blokkere et organisasjons egne addresser. Ta heller
ikke for gitt at en IPS kan stoppe et angrep.

## Programmer
* snort: NIDS med brukerdefinerte regler, veldig fleksibelt, krever forståelse.

* Falil2Ban: IPS, dette beskytter en viss enhet mot bruteforce på ssh, epost og 
web-innlogging.

* Eagle X: Windows-basert med utgangspunkt i snort.

* Suricata: IPS som er godt egnet til å kjenne igjen protokoller når
de kjøres på uvanlige porter.

* Bro/Zeek: effektiv NIDS som oppdaterer i real-time. 

* SAX2: NIDS + IPS for windows.

* Tripwire: unix-basert HIDS

* Afick: HIDS som tripwire, men mulighet for å kjøre på windows.

* OSSEC: master/worker basert IDS. windows støtter bare workers. 

* Verysis: HIDS for windows.
