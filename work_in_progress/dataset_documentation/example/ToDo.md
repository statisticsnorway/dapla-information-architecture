# MVP 1, 2, 3 for Dapla metadataløsning

## **Prorotyp for variabeldefinisjonssystem (VarDef)**

- Oversette informasjonsmodell for VarDef til [JSON Schema (modell)](https://json-schema.org/)
  - Variabeldefinisjonseksempler i form av JSON-dokumenter til testing, demo og opplæring
- *"VarDef Validator"* - validere variabeldefinisjoner i JSON-filene mot JSON Schema
- Enkel VarDef-prototyp implementert med bruk av JSON-filer, JSON Schema og [Python HTTP server](https://docs.python.org/3/library/http.server.html)?

---

## **Prototyp for datasettdokumentasjonssystem (DataDoc)**

### Oversette DataDoc-informasjonsmodell til JSON Schema

- Utarbeide et [JSON Schema (modell)](https://json-schema.org/) **per datatilstand**
  - Det er forskjellige krav til metadata for hver datatilstand. Vi må enten ta i bruk et JSON Schema per datatilstand, alternativt ta i bruk nye if-then-else-condition muligheter i JSON Schema
  - Støtte enten-eller-logikk (XOR) i schema 
  - Legge inn "description" og "title/label" på norsk
- *Utvikle modell for dokumentasjon av hierarkiske kildedata og inndata for mer komplekse datamottak?*

### JSON metadata eksempler til bruk i testing, demo og opplæring i SSB

- Lage JSON eksempel-metadata for hver datatilstand
  - [ ] Kildedata
  - [x] Inndata
  - [x] Klargjorte data
  - [ ] Statistikk(data)?
- Oversette attributter til norsk??
  - Lage en "Python-translator" for automatisk å oversettte mellom egelsk-norsk-engelsk attributtnavn og enum-lister?

### Hente "basis metadata" fra eksisterende datafil (CSV, Parquet, ...)

- Python-metode som leser ut info fra datafil (Parquet, ..) og genererer et utkast (draft) til JSON-dokument
  - name (dataset filename and column names)
  - datatype for variablene
  - "disctinct values" for hver variabel
  - created-date?
  - path?
  - dataPeriodFrom og dataPeriodUntil?

### Lage en Python validator class (bibliotek for bruk i notebooks til validering)

- Validere metadata med bruk av [Python jsonschema](https://pypi.org/project/jsonschema/)
  - Python finner hvilket JSON Schema som skal brukes for å validere ut i fra datatilstand (dataSetState) i JSON-metadatafil
- Enventult også støtte mer avansert validering av data-filen (Parquet, CSV, ...) med oppslag i KLASS osv.?
- Python metoder for serialisering/deserialisering av metadata (JSON to/from Dict)

---

## **Brukergrenesneitt - GUI / CLI**

- I første omgang støtte CLI
  - Eksempel:  `> python validate_dataset.py [my_dataset]`
- Ta i bruk en eller annen form for JSON Schema viewer som metadata editor (GUI)?
  - [react-jsonschema-form](https://react-jsonschema-form.readthedocs.io/en/latest/)
  - [jsonforms](https://jsonforms.io/)
  - Andre løsinger?
- Eventuelt Jupyter notebook med bruk av [Ipywidgets](https://ipywidgets.readthedocs.io/en/latest/index.html) som metadata-editor?

---

## **Datadokumentasjon som en del av "data pipelines"**

- Teste om det er mulig å inkludere dokumentasjonsarbeidet (DataDoc) som en del av en "data pipeline"? F.eks. om det er mulig å få til dette med bruk av notebooks i verktøy som [Elyra](https://elyra.readthedocs.io/en/stable/index.html)

---

## **Kartlegge mulige kandidater til «datakatalog» for søk/gjenfinning av datasett og variabler internt og eksternt (ssb.no)**

Hvis vi faller ned på en slags "distribuert" (fragmentert) lagring av metadata som JSON-filer spredt i datakataloger (bøtter), så må informasjonen i disse være søkbar/gjenfinnbar i en overordnet datakatalog-tjeneste (metadata-utforsker). 

Metadata må på sikt også gjøres tilgjengelig både internt og eksternt, f.eks. som en metadata-utforsker på ssb.no?

*Eksempel på datakatalog-tjeneste (metadata-utforsker):*
- [Variabelutforsker i microdata.no](https://microdata.no/discovery/datastore/?datastore=no.ssb.fdb)
- [ELVIS - Kretregisterets Elektronisk Liste over Variabler I Systemene](https://metadata.kreftregisteret.no/variables/search?selection=cancer_sites)

---

## **Behov for integrasjon mellom databaser/sky-datatjenester (CloudSQL, BigQuery, ..) og datadokumentasjonsløsningen (DataDoc)?**

Det må avklares om skybaserte datatjenester som CloudSQL, BigQyery og PubSub skal kunne brukes til å lagre stabile datatilstander av data (kildedata, inndata, klargjorte data, ..), eller om det er et krav at slike data må lagre som filer i kataloger (bøtter).

**Det er viktig å være klar over at kravet til uforanderlighet (immutable data) og versjonering av datasett er mye enklere å implementere for "statiske datafiler" i en katalog (bøtte), enn for data i medlingssystemer og databaser som av natur er mye mer dynamiske (oppdateres fortløpende).**

Hvis vi skal støtte full dokumentasjon av data i databaser og meldingssystemer må vi også ha en API-basert løsning for registrering av metadata i et sentralisert lager for DataDoc (i tillegg til DataDoc-løsningen med JSON-filer i kataloger).

---