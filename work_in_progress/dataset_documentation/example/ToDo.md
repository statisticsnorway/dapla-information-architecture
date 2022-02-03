# ToDo metadata-arbeid

## ToDo JSON metadata

- Lage JSON eksempel-metadata for hver datatilstand
  - [ ] Kildedata
  - [x] Inndata
  - [x] Klargjorte data
- Oversette attributter til norsk???
  - Lage en Python-translator for å automatisk oversettte mellom egelsk-norsk-engelsk?

## ToDo JSON Schema modell

- Et JSON Schema (modell) per datatilstand
- Ta i bruk if-then-else-condition i JSON-Schema for XOR-logikk
- Legge inn "description" og "title/label" på norsk
- Støtte dokukumentasjon av hierarkiske kildedata og inndata

## ToDo datafil (CSV, Parquet, ...)

- Python-metode som leser ut info fra datafil hvis mulig
  - name (dataset and variables)
  - datatype variables
  - disctinct values variable?
  - created-date?
  - path?

## ToDo Python validator class

- Validere med bruk av  [Python jsonschema](https://pypi.org/project/jsonschema/)
  - Python finner hvilket JSON Schema som skal brukes for å validere ut i fra "dataSetState" i JSON-metadatafil
- Metode for serialisering/deserialisering  (JSON to/from Dict)

## ToDo GUI / CLI

- JSON Schema viewer?
- Ipywidgets?
- CLI - f.eks. `python validate [dataset]`
