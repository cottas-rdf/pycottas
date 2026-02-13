<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/cottas-rdf/pycottas/main/logo/logo_inverse.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/cottas-rdf/pycottas/main/logo/logo.png">
    <img alt="3xmap-studio"  height="150" src="https://raw.githubusercontent.com/cottas-rdf/pycottas/main/logo/logo.png">
  </picture>
</p>

[![License](https://img.shields.io/pypi/l/pycottas)](https://github.com/cottas-rdf/pycottas/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/633315029.svg)](https://doi.org/10.5281/zenodo.15350990)
[![Latest PyPI version](https://img.shields.io/pypi/v/pycottas?style=flat)](https://pypi.python.org/pypi/pycottas)
[![Python Version](https://img.shields.io/pypi/pyversions/pycottas.svg)](https://pypi.python.org/pypi/pycottas)
[![PyPI status](https://img.shields.io:/pypi/status/pycottas?)](https://pypi.python.org/pypi/pycottas)
[![Documentation Status](https://readthedocs.org/projects/pycottas/badge/?version=latest)](https://pycottas.readthedocs.io)

**pycottas** is a library for working with **compressed** **[RDF](https://www.w3.org/TR/rdf11-concepts/)** files in the **COTTAS** format. COTTAS stores triples as a triple table in [Apache Parquet](https://parquet.apache.org/). It is built on top of [DuckDB](https://duckdb.org/) and provides an [HDT](https://www.rdfhdt.org/)-like interface.

## Features :sparkles:

- **Compression** and **decompression** of RDF files.
- Querying COTTAS files with **[triple patterns](https://www.w3.org/TR/sparql11-query/#sparqlTriplePatterns)**.
- [RDFLib](https://github.com/RDFLib/rdflib) store backend for querying COTTAS files with **[SPARQL](https://www.w3.org/TR/sparql11-query/)**.
- Supports [RDF datasets](https://www.w3.org/TR/rdf11-concepts/#section-dataset) (**quads**).
- Can be used as a **library** or via **command line**.
- Serve COTTAS files as an [SPARQL endpoint](https://github.com/cottas-rdf/pycottas-endpoint).

## Documentation :bookmark_tabs:

**[Read the documentation](https://pycottas.readthedocs.io/en/latest/documentation)**.

## Getting Started :rocket:

**[PyPI](https://pypi.org/project/pycottas/)** is the fastest way to install pycottas:

```bash
pip install pycottas
```

We recommend to use **[virtual environments](https://docs.python.org/3/library/venv.html#)** to install pycottas.

```python

import pycottas
from rdflib import Graph, URIRef

pycottas.rdf2cottas('my_file.ttl', 'my_file.cottas', index='spo')
res = pycottas.search('my_file.cottas', '?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?o')
print(res)
pycottas.cottas2rdf('my_file.cottas', 'my_file.nt')

# COTTASDocument class for querying with triple patterns
cottas_doc = pycottas.COTTASDocument('my_file.cottas')
# the triple pattern can be a string (below) or a tuple of RDFLib terms
res = cottas_doc.search('?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?o')

# COTTASStore class for querying with SPARQL
graph = Graph(store=pycottas.COTTASStore('my_file.cottas'))
res = graph.query('''
  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  SELECT DISTINCT ?s ?o WHERE {
    ?s rdf:type ?o .
  } LIMIT 10''')
for row in res:
    print(row)
```

To execute via **command line** check the [docs](https://pycottas.readthedocs.io/en/latest/documentation#command-line) or run:

```bash
pycottas -h
```

It is also possible to serve COTTAS files as an SPARQL endpoint with [pycottas-endpoint](https://github.com/cottas-rdf/pycottas-endpoint). 

## License :unlock:

**pycottas** is available under the **[Apache License 2.0](https://github.com/cottas-rdf/pycottas/blob/main/LICENSE)**.

## Author & Contact :mailbox_with_mail:

- **[Julián Arenas-Guerrero](https://github.com/arenas-guerrero-julian/) - [julian.arenas.guerrero@upm.es](mailto:julian.arenas.guerrero@upm.es)**

*[Universidad Politécnica de Madrid](https://www.upm.es/internacional)*.

## Citing :speech_balloon:

If you used pycottas in your work, please cite the **[ISWC paper](https://oa.upm.es/91920/1/arenas2026cottas.pdf)**:

```bib
@inproceedings{arenas2026cottas,
  title     = {{COTTAS: Columnar Triple Table Storage for Efficient and Compressed RDF Management}},
  author    = {Arenas-Guerrero, Julián and Ferrada, Sebastián},
  booktitle = {Proceedings of the 24th International Semantic Web Conference},
  year      = {2026},
  publisher = {Springer Nature Switzerland},
  isbn      = {978-3-032-09530-5},
  pages     = {313--331},
  doi       = {10.1007/978-3-032-09530-5_18},
}
```
