# pycottas

**pycottas** is a library for working with **compressed** **[RDF](https://www.w3.org/TR/rdf11-concepts/)** files in the **COTTAS** format. COTTAS stores triples in a triple table in the [Apache Parquet](https://parquet.apache.org/) format. It is built on top of [DuckDB](https://duckdb.org/) and provides an [HDT](https://www.rdfhdt.org/)-like interface.

## Features

- **Compression** and **decompression** of RDF files.
- Querying COTTAS files with **[triple patterns](https://www.w3.org/TR/sparql11-query/#sparqlTriplePatterns)**.
- [RDFLib](https://github.com/RDFLib/rdflib) store backend for querying COTTAS files with **[SPARQL](https://www.w3.org/TR/sparql11-query/)**.
- Supports [RDF datasets](https://www.w3.org/TR/rdf11-concepts/#section-dataset) (**quads**).
- Can be used as a **library** or via **command line**.

## COTTAS Files

**COTTAS** is based on *CO*lumnar *T*riple *TA*ble *S*torage with the [Apache Parquet](https://parquet.apache.org/) file format. A COTTAS file consists on a table with **s**, **p**, **o**, **g** columns representing triples (and [named graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-named-graph)):

- The **s**, **p**, **o**, **g** are filled with the [RDF terms](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-term) of the triples/quads.
- When a triple belongs to the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph), **g** is *NULL*. If all the triples in the [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset) belong to the [default graph](https://www.w3.org/TR/rdf11-concepts/#dfn-default-graph), **g** can be omitted.

## Licenses

**pycottas** is available under the **[Apache License 2.0](https://github.com/cottas-rdf/pycottas/blob/main/LICENSE)**.

The **documentation** is licensed under **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**.

## Author

- **[Julián Arenas-Guerrero](https://github.com/arenas-guerrero-julian/) - [julian.arenas.guerrero@upm.es](mailto:julian.arenas.guerrero@upm.es)**  
*[Universidad Politécnica de Madrid](https://www.upm.es/internacional)*.

## Citing

If you used pycottas in your work, please cite the **[ISWC paper](https://oa.upm.es/91920/1/arenas2026cottas.pdf)**:

``` bib
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


![OEG](assets/logo-oeg.png){ width="150" align=left } ![UPM](assets/logo-upm.png){ width="161" align=right }
