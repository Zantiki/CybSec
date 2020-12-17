# Nettbaserte angrep
## innbrudd
### via Nett
Gjøres ofte med portscanning som hjelp. Vanskelig
å forhindre helt. Lytt etter ICMP-pakker mot mange addresser
på en gang eller forsøk på å åpne alle porter på en maskin.
Blokker ip der denne trafikken kommer fra.

### via Avlytting
Krever tilgang til nett av fiende. HIDS kan oppdage
programvare-basert lytting, men ikke fysisk på moden/svitsj-port.
Bruk forskjellig passord på epost og andre tjenester slik at 
at det ikke kan misbrukes.
### via modem
Ofte automatiske angrep som baserer seg på å ringe opp 
maskin via mobilnett og bruke det for å komme seg forbi brannmur.
En tiltak mot dette er å sørge for at brannmur går begge veier.

### via telefoner
Som modem kan de brukes til eget nett til å infisere maskin
på firmanett, dette kan ha svakheter for både Spyware, virus
og sniffeprogrammer.
### trådløst
Sentrale svakheten her er at det ikke er behov for 
fysisk tilgang. En del av disse nettene har også dårlig sikkerhet
og er som følge vidt åpne.

### fysisk
Innbærer et fysisk innbrudd, hvor de ansvarlige kan stjele/få
tilgang til innloggede PCer eller plante enheter/programvare
som kan brukes til dette etterpå.

## imperosnation
Ved tilgang til passord kan man late som man er noen
andre, enten ved autentiseringsinformasjon man får avlytting
eller andre sikkerhetshull.

## Denial of service
Innbærer at en angrip overbelater system til en slik 
grad at det blir ubrukelig. 
### DDOS
Står for distributed denial of service og innebærer å 
ta kontroll over mange forskjellige maskiner og angripe
alle på en gang. Slike maskiner kalles et botnet. Et slikt
angrep kan være så enkelt som å få alle maskinene i botnettet
til å sende samme forspørsel på en og samme gang. Synlige,
upopulære eller organisasjoner med svært god sikkerhet er
ofte mål for denne typen angrep.

### DNS
Overloade så mange DNS-tjener som mulig med falsk fra-addresse.
Dette gjøres for å overbelaste båndbredden til et offer.
Kalles også for speiling/bouncing.

Mottilltak mot denne typen angrep innebærer å ikke formidle
pakker fra falsk adresse, må skille tydlig mellom rekursive
dns-tjenere og innholdstjenere. De rekursivje tjenerene bør også
kun vær tilgjengelig innenifra. Innholdtjenere bør ha et 
begrenset ansvarsområde som en redundans. 
## Spyware
Kan være intergrert i annen programvare, spres via virus og tvilsomme nettsider.
Noen sentrale:

* Keyloggere: registrere all typing for å stjele passord
  
* Stjeling av kontaktlister fra epost eller tlf.
  
* Programmer som overvåker om du har piratkopier eller ikke
  
* Programmer som overvåker alt for mye info, i.e FB, TikTok, etc.

## tiltak mot spyware
Spyware kan være vanskelig å oppdage, men visse typer kan oppdages via IDS 
og eller pakkesniffere. Dette er allikvel situasjonsbestemt. 
Dersom du mistenker at et gitt programvare har spyware kan du teste det ut i
en sandkasse.

Det beste mottiltaket er å reinstallere maskinen, men detter er ofte ikke 
praktisk. Dersom man oppdager dette i "programmer med tillit" bør man klage, 
og skinne lys på det slik at leverandøren ikke fortsetter med slikt i fremtiden. 
Alternativt kan du også slette programmet og/eller skru av tjenester med kjente
svakheter.

## utpressing
I nyere tider ønsker hackere å oppnå noe ved angrepene sine.
dette gjøres ofte ved å kryptere viktige filer og holde de gissel mot løsepenger.
Dette kan motvirkes med god nettsikkerhet og ved å ta sikkerhetskopier av alt. 
dette involverer å ha off-site og offline sikkerhetskopier. 
## sikkerhetsproblemer 
### TCP/IP sekvensnummere:
Sekvensnummeret i TCP pakker kan forfalskes og pakker kan utnyttes til å lure
tjener på et vis. Å "gjette" seg fram til sekvensnummeret er ikke nødvendigvis
vaskelig da algoritmene for å genere de er velkjente.

Dette er best motarbeidet ved å bruke pakkefilter som sjekker gyldighet til
fra-addresser, da disse ofte er falske i slike pakker. 
### KApring
Også kjent som "session hijacking" hvor en angriper tar over sesjonen til en
klient og får tilgang til ressursene de krevde. Dette er et angrep det
er vanskelig å oppdage før det er for sent. Slike angrep er man best sikret mot
dersom man bruker enkryptering.
### Syn-angrep
Innebærer å overbelste minnet til en gitt tcp forbindelse ved ønsket three-way handshake
slik at en TCP forbindelse ikke kan settes opp.

Dette kan forbygges ved hjelp av proxier hvor kun tilkoblingen til proxy-tjeneren
får tilkoblingen overbelastet. I linux har man såkalte syncookies som 
kan aktiveres som et mot-tiltak.Brannmur kan også sette rate-begrensinger på
Syn-pakker.
### Land.c
Innbærer å sende pakker med samme fra addresse og til addresse på samme port slik
at TCP-forbindelsen går i vranglås. Dette er en svakhet i naive tcp-forbindelser.
### UDP-problemer
Har færre felter enn TCP og lettere å forfalske. Løses best ved å filtrere
ut UDP på brannmur.
### Smurf
Sende ping-pakke med addressen til offer, slik får offeret plagsomt mange svar 
og båndbredden overbelastes. Man kan også sette dette til en broadcast-addresse
men det kan filtrers ut av både ping-implementsjon og brannmur.
### Teardrop
Sende fragmenterte pakker hvor det er overlapp i fragmentene for å
utnytte kjente svakheter i dårlige IP-implementassjoner.
### Fragementering
Involverer å dele opp portnummer til mål i flere pakker slik at brannmur
ikke kan stoppe pakker. I linux er dette løst ved å sette sammen pakken 
før sjekk i pakkefilter.

### Juletrepakker
Dette er en TCP-pakke hvor alle flaggene er satt, siden dette aldri skal skje
bør disse filtrers ut av brannmur.
### IPv6
Mange av de samme angrepene rettet mot IPv4 kan også rettes mot IPv6. Generelt
er regelen at alle tiltak som implementeres for IPv4, bør implementeres for 
IPv6 også, dersom det skal brukes aktivt. Ta heller ikke for gitt at IPv6
implementasjoner bruker NAT som default. Merk også at TCP, UDP og ICMP nå
er ersattet med v6-versjoner.


# Fysiske sikringstiltak
Vi deler inn i 3 grupper:

* preventaive tiltak

* Detekterende Tiltak

* Skademinimerende Tiltak
## Preventive tiltak
### Angripere
For avlytting av transportmedia er pakkesniffing største trussel, og løses
best ved å bruke enkryptering.

Innbrudd er også et faremoment og man bør ikke undervurdere hvor langt en fiendes 
er villig til å gå for å få tilgang til sensitive data/tukle med utstyr. 
Et godt tiltak mot dette er å låse inn alt av nettverkutstyr der de er
utligjenmgelige og maskiner bør låses når ingen er til stede. Man skal
heller ikke utelukke muligheten for at andre i organsiasjonen vil tukle med
nettverksutstyret. Hvem som har tilgang til hva bør inkluderes i sikkerhets-policy.
Man kan også forbygge innbrudd ved bruk av alarm og døgnvakt.

Når det gjelder sikring av maskinvare kan det låses med en såkalt kensington-lock
For å sikre seg mot industrispioner bør disker krypteres og programmvare
som sletter/varsler ved tyveri kan installeres.

Generelt bør man også ha klar policy på å ikke slippe inn ukjente.

### Miljø
Det er en del miljømessige riskoer som bør taes høyde for:
* brann og slokking: her bør det brukes gass slik at utstyr ikke blir ødelagt.
Det finnes komposisjoner som også gjør at mennesker ikke kveles dersom de er oppbevart
  i et slikt rom.

* problemer med vann og flom: Installer luftfukt-detektorer slik at evt.
feil kan oppdages tidlig. Lekkasje og kondens fra aircon kan forårsake skade.

* Strømbrudd og nødstrøm: Ved steder der strøm kan være utsabilt bør det
innstallerers såkalte UPS som tar over ved ustabil strømforsyning.

* tempratur og luftfuktighet: Ta alltid høyde for at tap av vannforsyning
eller feil i andre kjølesystemer kan ha en negativ effekt på ditt utstyr.
Nødstrøm dekker sjeldent kjøleannlegg.

* Naturkatastorfer: Lynnedslag og orkaner er en risiko her. Lyn-treff kan
forebygges med lynavleder.

* EM-skader: Der hvor det passerer store mengder størm er dette en risiko.
Dette gjelder ikke bare industrielt utstyr, men også tog og andre el-kjøretøy.

* Renhold: Utstyr vil forvitre ved dårlig renhold av rom, støv i vifte
etc.

* Jordfeil: kan enkelt ødelegge utstyr ved spenningsforskjell

## Skademinimerende tiltak
Dette er også kjent som redundans og består i korte trekk ut på å ha en 
plan b når det brenner på dass. 

### Strøm
Ingen strøm, ingen enheter. det kan derfor lønne seg å installere såkalt
Uninterruptable Power Supply, UPS slik at strømmen går uforstyrret. Profesjonell
nett-elektronikk har ofte også doble strømforsyninger, men da bør man sørge
for at det er koblet inn i to forksjellige nett. Størrelsen på UPS og separate
strømnett er behovprøvd med størrelsen på virksomheten og systemet.
### Nett
For hvert komponent i et nett burde man ha en backup som tar over 
ved feil i den første. Vi kan også benytte oss av redundante kabler for 
å ha flere veier å vlege mellom. dette kalles ofte for redundant topologi og
er ofte del av ruter/svitsj.

Spanning tree protocol som brukes av ethernet har behov for redundans i form
av at det alltid er mer enn en vei å gå fra en svitsj til en annen. Programvare
er ansvarlig fopr stenging av porter som styrer dette. Automatisk håndtering
av redundans gjøres av protokollen Rapid Spanning Three.

## Sannhet om sikkerhet
Mennesker er alltid den største sikkerhets-risikoen for en virksomhet og alle
er utsatt for sikkerhetsproblemer. Videre kan det også sies at prisen av
skikkelig sikkerhet er billigere en prisen av kritiske sikkerhets-hendelser.

Sikkerhetstiltak burde alltid måles opp mot nytteverdi og kompleksitet gjør
større rom for feil som kan utnyttes. Mer også at det ofte finnes en omvei rundt
eventuelle sikkerhets-tiltak man har tatt, noe som vil insentiviviserer medlemmene
i organisasjonen til å unngå å gjøre det på den sikre måten. Generelt gjelder
også at den sikreste infrastrukturen er den som er under kontroll, dette
betyr at alt er oppdatert og kun nødvendig programvare kjører.

## misforståelser om sikkerhet
Å bare ha brannmur er ikke nok til å sørge for at et nettverk er sikkert.
Teknologien og nettadministrasjon er kun en liten del av fullstendig sikring.
Videre kan det også sies at brannmurer ikke sikrer mot feil på innsiden. 
Man skal heller ikke ha for mye tillit i ip-spesifikke brannmursregler da
det å skaffe seg nye ip-adresser ikke er spesielt vanskelig, samt at 
å vedlikeholde individuelle addresser bare er smertefullt.

Å bruke DHCP på å sjekke MAC-adresser er ikke god nok tilgangs-styring.
Dette er fordi at MAC-adresser lett kan forfalskes med et annet nettverkort.
Dersom nettet er kablet, burde slik tilgangstyring skje i svitsjene.
## Tre faser i hendelseshåndtering
Man benytter seg av gode innarbeidede rutiner ved krise-situasjoner. 
Etter kriser burde det gjøres etterarbeid på å forbedre prosessen av håndtering
av krisen.
## Planleggingsfasen
I større organisasjoner defineres det tydelig i en sikkerhetspolicy hva
som er tillat/ikke, samt hvordan brudd skal håndteres. Her burde plicyen testes
og følgende punkter avklares:

* hvem varsles ved hendelsen?
  
* Hvordan kontrollerer vi informasjonflyten om hendelsen?

* Hvordan fordeles hånteringen av probelemet?

* Hvor langt er man villig til å gå for å beskytte ressursen på spill?

* Hva regnes som normalt?

Sørg også for at hele datasystemt er fulgt opp, da negliserte maskiner ofte
er de som står bak mange sikkerhets-hendelser. Del av dette er å drive 
flittig logging slik at man har kontroll over systemets tilstand, og en sort 
boks når flyet krasjer.

## Handlingsfasen
Ofte kan en miskonfigurering eller bug misforståes som en sikkerhets
hendelse. Det er derfor viktig å avklare dette tidlig, og så gå videre til
å analysere situasjonen.
Her må man ta stilling til to ting:
omfanget av hendelsen, og hvordan det skal angripes. Dette er selvagt
situasjonbestemt, men generelt er det best å ta en utsatt maskin av nettet.

Man må også ta stilling til følgende ved avkobling av maskin:

* Skal du bruke tid på å samle informasjon om hva som har skejdd?

* Må maskinen settes opp på nytt?

* Hvordan skal vi håndtere innholdet på maskinen?

## Etterarbeid
Sikkerhetshendelser må dokumenteres slik at de kan bli brukt til evt. 
anmeldelser og/eller utbedre rutiner. Det er også viktig at pårørte parter
blir informert om hendelsens status og konklusjon.

## Oppsummering av sikkerhetshendelser.
Som sysadmin er det viktig at det er enighet mellom deg og ledelsen 
i hvordan man skal håndtere sikkerhetshendelser. Bruke Gjerne IDS (Intrusion
detection System) for å detektere brudd tidlig. Ved sikkerhetshendlser bør
man holde hodet kaldt. Hold også alle parter in-the-loop.