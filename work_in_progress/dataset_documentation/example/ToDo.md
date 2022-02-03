# MVP for Dapla metadata

## **Datasettdokumentasjon (DatasetDoc)**

### ToDo JSON metadata

- Lage JSON eksempel-metadata for hver datatilstand
  - [ ] Kildedata
  - [x] Inndata
  - [x] Klargjorte data
- Oversette attributter til norsk???
  - Lage en "Python-translator" for automatisk å oversettte mellom egelsk-norsk-engelsk attributtnavn og enum-lister?

### ToDo JSON Schema modell

- Et [JSON Schema (modell)](https://json-schema.org/) per datatilstand
- Ta i bruk if-then-else-condition i JSON-Schema for XOR-logikk
- Legge inn "description" og "title/label" på norsk
- Støtte dokukumentasjon av hierarkiske kildedata og inndata for mer komplekse datamottak?

### ToDo datafil (CSV, Parquet, ...)

- Python-metode som leser ut info fra datafil (Parquet, ..) og genererer et utkast (draft) til JSON-dokument
  - name (dataset filename and column names)
  - datatype variables
  - disctinct values for variable?
  - created-date?
  - path?
  - dataPeriodFrom og dataPeriodUntil?

### ToDo Lage en Python validator class

- Validere metadata med bruk av [Python jsonschema](https://pypi.org/project/jsonschema/)
  - Python finner hvilket JSON Schema som skal brukes for å validere ut i fra "dataSetState" i JSON-metadatafil
- Python metoder for serialisering/deserialisering av metadata (JSON to/from Dict)

---

## **ToDo variabeldefinisjoner (VarDef)**

- Lage JSON Schema for VarDef-modell
- Variabeldefinisjonseksempler i form av JSON-dokumenter
- Python validator for variabeldefinisjoner
- Enkel VarDef-prototyp med bruk av [Python HTTP server](https://docs.python.org/3/library/http.server.html)

---

## **ToDo GUI / CLI**

- I første omgang støtte CLI
  - Eksempel:  `> python validate_dataset.py [my_dataset]`
- Ta i bruk en eller annen form for JSON Schema viewer som metadata editor (GUI)?
  - [react-jsonschema-form](https://react-jsonschema-form.readthedocs.io/en/latest/)
  - [jsonforms](https://jsonforms.io/)
- Eventuelt Jupyter notebook med bruk av [Ipywidgets](https://ipywidgets.readthedocs.io/en/latest/index.html) som metadata-editor?

---

## Datadokumentasjon og "data pipelines"
- Teste om det er mulig å inkludere dokumentasjonsarbeidet som en del av en "data pipeline"? F.eks. om det er mulig å få til dette i verktøy som [Elyra](https://elyra.readthedocs.io/en/stable/index.html)

---
