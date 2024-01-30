
# Scraping di Repubblica

Questo è un breve esempio di utilizzo delle librerie `requests` e `Beautifulsoup4`. Voglio ottenere rapidamente un elenco di tutti i nuovi articoli su Repubblica, per vedere se vale la pena aprire il sito del giornale. I hash degli articoli vecchi vengono memorizzati per mostrare solo i nuovi articoli.

## Tabella dei contenuti

- [Installazione](#installazione)
- [Utilizzo](#utilizzo)
- [Contributi](#contributi)
- [Licenza](#licenza)

## Installazione

Clona il repository, verifica di avere installato Python, esegui `pipenv install` o preferibilmente `pipenv install`.

Utilizza le librerie pypi `requests`, `beautifulsoup` e `hashlib`. La funzione di hash standard incorporata non può essere utilizzata per l'hashing persistente in quanto ottiene un nuovo seed di numero casuale ogni volta.

## Utilizzo

Esegui 
```python3 RepublicaScraping.py```

riceverei solo gli articoli nuovi. Se desideri tutti gli articoli attualmente presenti, prima dell'invocazione del programma,  cancella la cartella dei valori hash degli articoli.
```rm last_run_hash.json```

## Licenza

Nessuna restrizione di uso è riutilizzo, nessuna garanzia o responsabilità da parte del autore. L'utilizzo responsabile ė responsabilità esclusiva del utente.

# Repubblica scraping

This is a short example of using the `requests` and `Beautifulsoup4` libraries. I want to get a quick list of all new Articles in Repubblica, to see whether it is worthwhile to open the newspaper site. Old article's hashes are remembered to only give the new articles.
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

check out the repository, check you have installed python, run pipenv install, or preferably pipenv install

uses the pypi libraries requests and beautiful soup and hashlib. The standard built-in hash function cannot be used for persitant 
hashing as it gets a new random number seed every time. 




## Usage
run

```python3 RepublicaScraping.py```

The first time you'll get all article with an < H2 > tag. Subsequently only new article headings. 
The hashes of the articles already obtained in previous invocation are remembered in last_run.json and no longer shown.

If you want to get all harvested headings 

```rm last_run_hash.json```

before invocation.

## Contributing

Exercise inspired by Coding with Mosh
## License
no legal restrictions for re-use. No liabilities for the code either.


Information about the project's license.
