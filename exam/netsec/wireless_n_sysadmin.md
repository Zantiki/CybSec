# Trådløse Nett
Mest fundamentale protokollen for trådløst nett er IEEE 802.11.
De er ofte delt i to frekvensområder, 2.4GHz og 5Ghz.
## Operasjoner i et trådløst nettverk
Trådløst nett operer ofte i to modus: infrastrukturmodus og 
ad-hoc modus. infrastruktur-modus er den mest brukte. Et nett kalles
også for Extended Service set og kan være bestående av flere
Basic Service Sets.
## Sniffing
sniffing kan gjøres av alle som er i nærheten av aksesspunkt. 
Vi antar alltid at det finnes en potensiell avlutter.
## Hidden node problemet
Det finnes et skjult enhet som forårsaker kommunikasjons-problemer
for oss da sendingen til/fra akksesspunkt har kollisjoner
## MIMO
Multiple in, multiple out. Når akksesspunkt mottar signal på
en av antennene vil den svare dette signalet med samme spesifisering
den mottok. Slik blir signalet sterkere og i riktig retning.

## Uatorisert bruk og tilgang
Alle nett bør ha tilgangstyring da enhver som kommer seg inn evt. kan finne
sårbarheter å utnytter
## WPS
Privatbrukere er dårlige til å sette opp nett med god sikkerhet.
WPS ble da implementer som pin-beskyttelse på WiFi. I utgangspunktet
trenger vi bare 11k forsøk for å finne et WiFi-passord. 
## Sette netteverk ut av spill
Genere radiostør for å sakke ned nettet, noe som ofte er tilfellet
om man bor tettbygd og naboene har nett på samme kanal. Ved urimelige
frekvensforstyrrelser kan man ta kontakt med PT. 
## De-autentisering
Noen eksempler: Angriper kan sende deautentiseringspakker til en
enhet som så vil koble til å fra. Protokollen beskyttes ikke med kryptering
Dette brukes ofte sammen med andre angrep.
## Brute-force WPA knekking
Da WPA2-passord inneholder for mange tegn kan man anripe nett ved
å bruke deutentisering, slik at man kun brute-forcer pakken og ikke
selve nettet.
## Trådløse nett med/uten pwd
Brueker nette WPA/WPA2 er det generelt sikkert størte forskjellen
er at WPA ikke bruker passord som krypteringsnøkkel, bare som autentisering.

## Sikkerhetsrisikoer
Ingen WPA, ingen enkryptering. All trafikk kan sees av de som er tilkoblet.
WEP med felles passord er like usikkert da man kan dekryptere om man
har passordet tilgjengelig.
## Radioplanlegging
Her er prioriteringen å sette opp slik at vi får minst mulige forstyrrelser.
Dette gjør vi ved å ikke gjenbruke kanaler. Nyere akksesspunkter gjør
dette automatisk, men ikke forvent at dette alltid er like optimalt.
Merk også at kanaler har noe overlapp.
For å gjøre måliger kan vi bruke følgende verktøy for WLAN scanning:

* inSSIDer
* FreeBSD
* Kismet

inSSIDer bruker aktiv scanning mes de andre bruker passiv.

## WEP
Wiered equivalent Privacy, kan knekkes av aircrack-ng ganske fort.
## MAC-aksess
Eldre teknikk hvor kun godkjente enheter får koblet seg til Ruter.

## Skjult ESSID
Skjuler nettverket, men kan lett oppdages av pakkesniffere.
## WPA
Wifi Protected Access er vidt støttet how mange akksesspunkter og klienter.

## WPA2
Også kjent som IEEE 802.11i er lik WPA, men krever bruk av CMMP
og AES.
## Web-gui
Autentisere for nett VIA gui og ikke WPA2.
## VPN
Bruke VPN-tilkobling som en form for autentisering.

## DoS
Radio-jamming og/eller disassociation pakker til en gitt klient.
## Brute force
Funker for WPS men ikke WPA og WPA2.
## Man in the middle
Late som du er noen du ikke er for å ha muligheten til å lytte inn på
trafikken til en intetanende bruker.
## Spore opp trådløse sendere
Man kan peile inn på angripere ved å triangulere basert på signalstyrke.


# Systemadministasjon
## Admin-grensesnitt
Dersom det kun brukes SNMP for å administrere nettverket er det ikke
noe behov for å ha web-tjener og telnet på. Vi må også bytte
standardpassord. For lokal tilgang må man sørge for at uvedkommende
ikke kan nå de. Fjernstyring skal kun brukes når det kan krypteres.
## Aksess-begrensning
Det enkleste er ofte det beste, og da å kun begrense akksess til visse
nett kan være det sikreste. Et annet alternativ er å bruke VLAN. Man
kan også kombinere aksessfiltere og VLAN for å lage et Admin-nett
## Autentisering og authorisasjon
Brukere lagres i en sentral database og sjekkes via Radius er Tacacs+.
## Telnet og SSH
Generalt er SSH å foretrekke da det er enkryptert. Ved tilkobling
via ssh må tilgangen ofte eskaleres.
## Webgrensesnitt
Som nettadministrator bør du være klar over at endringer til
webgrensesnittet ofte ikke er enkryptert med https.
## SNMP
Brukes ofte til oppgaver som kan automatiseres som logging og
overvåkning av utstyr. Dette kan gjøres ved hjelp av SNMP gitt
at maskinen det hentes fra har en snmp daemon oppe.
## SNMP trap
Automatisk varlsing om entydige feilsituasjoner på et nettverk.
En slik trap fungerer ved at en SNMP agent varsler en SNMP trap-host
om visse hendvendleser som som blir håndtert av den i ettertid.
## Radius
Kort for Remote Authentication Dial in User Service og bruker
normal UDP 1812. Det finnes mange forskjellige Radius-servere, 
men Free-radius er vanligst. 
En av de mest brukte protokollene. er ikke kryptert.

## TACACS+
Står for Terminal Access Controller Access-Control System Plus.
Dette er en proprietær protokpll for autentisering og autorisasjon av brukere.
Originalt en CISCO portokoll. Er kryptert. Ikke vidt støttet.
Men fungerer bra på cisco-utstyr

## Sentralisert logging.
dette gjøres normalt med tjeneren rsyslogd og logger viktige
systemhendelser. Dette kan den også håndtere over et helt nettverk.
Disse loggene kan sees på mange måter, f.eks et web-grensesnitt 
eller klienten loganalyzer. Slike logger bør beskyttes slik at
loggene bevares og ikke tukles med.

