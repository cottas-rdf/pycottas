# Documentation

## Installation

In the following we describe different ways in which you can install pycottas.

### PyPI

**[PyPI](https://pypi.org/project/pycottas/)** is the fastest way to install pycottas.
```bash
pip install pycottas
```

We recommend to use **[virtual environments](https://docs.python.org/3/library/venv.html#)** to install pycottas.

### From Source

You can also grab the latest source code from the **[GitHub repository](https://github.com/arenas-guerrero-julian/pycottas)**.
```bash
pip install git+https://github.com/arenas-guerrero-julian/pycottas.git
```

## API Reference

### General Functions

#### rdf2cottas

`{++pycottas.rdf2cottas(rdf_file_path, cottas_file_path, index='spo', disk=False)++}`

Compress an RDF file in a plain text format into COTTAS. The compressed file is indexed for efficient querying.

**`Parameters:`**

* **rdf_file_path : *str***
  
    Path to the input RDF file. Supported formats:  N-Triples, N-Quads, Turtle, TriG, N3, and RDF/XML.

* **cottas_file_path : *str***
  
    Path to the output COTTAS file.

* **index : *{‘spo’, ‘sop’, ‘pso’, ‘pos’, ‘osp’, ‘ops’}, default ‘spo’***
  
    Computed index for the compressed COTTAS file. For [RDF datasets](https://www.w3.org/TR/rdf11-concepts/#section-dataset) index permutations include **`g`**, e.g., `spog`.

* **disk : *bool, default False***
  
    Whether to use on-disk storage.

#### cottas2rdf

`{++pycottas.cottas2rdf(cottas_file_path, rdf_file_path)++}`

Uncompress a COTTAS file to RDF in N-Triples format.

**`Parameters:`**

* **cottas_file_path : *str***
  
    Path to the input COTTAS file.

* **rdf_file_path : *str***
  
    Path to the output RDF file (N-Triples).

#### search

`{++pycottas.search(cottas_file_path, triple_pattern)++}`

Evaluate a [triple pattern](https://www.w3.org/TR/sparql11-query/#sparqlTriplePatterns) over a COTTAS file.

**`Parameters:`**

* **cottas_file_path : *str***
  
    Path to the COTTAS file.

* **triple_pattern : *str*, *list* or *tuple***
  
    The triple pattern can be a string or a list or tuple with the sequence of [RDFLib](https://github.com/RDFLib/rdflib) (subject, predicate, object) terms with variables given by `None`. The pattern can be a *quad pattern* in the case of querying an [RDF dataset](https://www.w3.org/TR/rdf11-concepts/#section-dataset).

``` py title="Example: Querying COTTAS files with triple patterns" hl_lines="4 5"
import pycottas
from rdflib import URIRef

res = pycottas.search('my_file.cottas', '?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?o') # (1)
res = pycottas.search('my_file.cottas', (None, URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), None)) # (2)

print(res)
```

1.  :star2: Triple pattern as a **string**.
2.  :star2: Triple pattern as a **tuple of RDFLib terms** (`None` for variables).

#### cat

`{++pycottas.cat(cottas_file_paths, cottas_cat_file_path, index='spo', remove_input_files=False)++}`

Merge multiple COTTAS files into one.

**`Parameters:`**

* **cottas_file_paths : *str***
  
    Paths of the input COTTAS files to merge. E.g., `['file1.cottas', 'file2.cottas']`.

* **cottas_cat_file_path : *str***
  
    Path to the output COTTAS file. 

* **index : *{‘spo’, ‘sop’, ‘pso’, ‘pos’, ‘osp’, ‘ops’}, default ‘spo’***
  
    Computed index for the merged COTTAS file. For [RDF datasets](https://www.w3.org/TR/rdf11-concepts/#section-dataset) index permutations include **`g`**, e.g., `spog`.

* **remove_input_files : *bool, default False***
  
    Whether to remove the input COTTAS files after merging.

#### diff

`{++pycottas.diff(cottas_file_1_path, cottas_file_2_path, cottas_diff_file_path, index='spo', remove_input_files=False)++}`

Substract a COTTAS file from another.

**`Parameters:`**

* **cottas_file_1_path : *str***
  
    Path to the initial COTTAS file.

* **cottas_file_2_path : *str***
  
    Path to the COTTAS file to substract.

* **cottas_diff_file_path : *str***
  
    Path to the output COTTAS file.

* **index : *{‘spo’, ‘sop’, ‘pso’, ‘pos’, ‘osp’, ‘ops’}, default ‘spo’***
  
    Computed index for the resulting COTTAS file. For [RDF datasets](https://www.w3.org/TR/rdf11-concepts/#section-dataset) index permutations include **`g`**, e.g., `spog`.

* **remove_input_files : *bool, default False***
  
    Whether to remove the input COTTAS files after subtracting.

#### info

`{++pycottas.info(cottas_file_path)++}`

Query COTTAS file metadata.

**`Parameters:`**

* **cottas_file_path : *str***
  
    Path to the COTTAS file.

#### verify

`{++pycottas.verify(cottas_file_path)++}`

Check whether a COTTAS file is valid.

**`Parameters:`**

* **cottas_file_path : *str***
  
    Path to the COTTAS file.

### COTTASDocument

`{++pycottas.COTTASStore(path)++}`

Class for evaluating [triple patterns](https://www.w3.org/TR/sparql11-query/#sparqlTriplePatterns) over COTTAS files. 

**`Parameters:`**

* **path : *str***
  
    Path to the COTTAS file.

``` py title="Example: Querying COTTAS files with triple patterns using COTTASDocument" hl_lines="4"
from pycottas import COTTASDocument
from rdflib import Graph, URIRef

cottas_doc = COTTASDocument('my_file.cottas')

res = cottas_doc.search('?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?o') # (1)
res = cottas_doc.search((None, URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), None)) # (2)

# limit and offset
res = cottas_doc.search('?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?o', limit=10, offset=20) # (3)

# RDF terms in the result set can be in N3 (default) or as RDFLib terms 
res = cottas_doc.search('?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?o', results_in_n3=False) # (4)

print(res)
```

1.  :star2: Triple pattern as a **string**.
2.  :star2: Triple pattern as a **tuple of RDFLib terms** (`None` for variables).
3.  :star2: Limit and offset can be optionally provided for pagination.
3.  :star2: The RDF terms in the result set are RDFLib terms.

### COTTASStore

`{++pycottas.COTTASStore(path)++}`

[RDFLib](https://github.com/RDFLib/rdflib) store backend to query COTTAS files with [SPARQL](https://www.w3.org/TR/sparql11-query/).

**`Parameters:`**

* **path : *str***
  
    Path to the COTTAS file.

``` py title="Example: Querying COTTAS files with SPARQL using COTTASStore" hl_lines="4"
from pycottas import COTTASStore
from rdflib import Graph

store = COTTASStore('my_file.cottas')

graph = Graph(store) # (1)

res = graph.query('''
  SELECT DISTINCT ?s ?o WHERE {
    ?s a ?o .
  } LIMIT 10''')

for row in res:
    print(row)
```

1.  :rocket: From here `graph` can be used as a read-only **RDFLib store**.


## Command Line

To execute COTTAS from the command line, call `pycottas`, specify the operation to perform (`rdf2cottas`, `search`, `cat`, etc.), and provide the required parameters.
As an alternative, `python3 -m pycottas` is also supported.

``` hl_lines="1"
$ pycottas -h

usage: pycottas {rdf2cottas,cottas2rdf,search,info,verify,cat,diff} ...

positional arguments:
  {rdf2cottas,cottas2rdf,search,info,verify,cat,diff}
                        subcommand help
    rdf2cottas          Compress an RDF file into COTTAS format
    cottas2rdf          Decompress a COTTAS file to RDF (N-Triples)
    search              Evaluate a triple pattern
    info                Get the metadata of a COTTAS file
    verify              Check whether a file is a valid COTTAS file
    cat                 Merge multiple COTTAS files
    diff                Subtract the triples in a COTTAS files from another
```

#### rdf2cottas

``` hl_lines="1"
$ pycottas rdf2cottas -h

usage: pycottas rdf2cottas -r RDF_FILE -c COTTAS_FILE [-i INDEX]

options:
  -h, --help            show this help message and exit
  -r RDF_FILE, --rdf_file RDF_FILE
                        Path to RDF file
  -c COTTAS_FILE, --cottas_file COTTAS_FILE
                        Path to COTTAS file
  -i INDEX, --index INDEX
                        Zonemap index, e.g.: `SPO`, `PSO`, `GPOS`
  -d DISK, --disk DISK  Whether to use on-disk storage
```

#### cottas2rdf

``` hl_lines="1"
$ pycottas cottas2rdf -h

usage: pycottas cottas2rdf -c COTTAS_FILE -r RDF_FILE

options:
  -c COTTAS_FILE, --cottas_file COTTAS_FILE
                        Path to COTTAS file
  -r RDF_FILE, --rdf_file RDF_FILE
                        Path to RDF file (N-Triples)
```

#### search

``` hl_lines="1"
$ pycottas search -h

usage: pycottas search -c COTTAS_FILE -t TRIPLE_PATTERN [-r {table,tuples,to_csv}]

options:
  -c COTTAS_FILE, --cottas_file COTTAS_FILE
                        Path to COTTAS file
  -t TRIPLE_PATTERN, --triple_pattern TRIPLE_PATTERN
                        Triple pattern, e.g., `?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?o`
  -r {table,tuples,to_csv}, --result_option {table,tuples,to_csv}
                        What to do with the result set
```

#### info

``` hl_lines="1"
$ pycottas info -h

usage: pycottas info -c COTTAS_FILE

options:
  -c COTTAS_FILE, --cottas_file COTTAS_FILE
                        Path to COTTAS file
```

#### verify

``` hl_lines="1"
$ pycottas verify -h

usage: pycottas verify -c COTTAS_FILE

options:
  -c COTTAS_FILE, --cottas_file COTTAS_FILE
                        Path to COTTAS file
```

#### cat

``` hl_lines="1"
$ pycottas cat -h

usage: pycottas cat --input_cottas_files INPUT_COTTAS_FILES [INPUT_COTTAS_FILES ...] --output_cottas_file OUTPUT_COTTAS_FILE [-i INDEX] [-r REMOVE_INPUT_FILES]

options:
  --input_cottas_files INPUT_COTTAS_FILES [INPUT_COTTAS_FILES ...]
                        Path of the input COTTAS files
  --output_cottas_file OUTPUT_COTTAS_FILE
                        Path of the output COTTAS file
  -i INDEX, --index INDEX
                        Zonemap index, e.g.: `SPO`, `PSO`, `GPOS`
  -r REMOVE_INPUT_FILES, --remove_input_files REMOVE_INPUT_FILES
                        Whether to remove input COTTAS files after merging
```

#### diff

``` hl_lines="1"
$ pycottas diff -h

usage: pycottas diff -c COTTAS_FILE -s SUBTRACT_COTTAS_FILE -o OUTPUT_COTTAS_FILE [-i INDEX] [-r REMOVE_INPUT_FILES]

options:
  -c COTTAS_FILE, --cottas_file COTTAS_FILE
                        Path to the COTTAS file
  -s SUBTRACT_COTTAS_FILE, --subtract_cottas_file SUBTRACT_COTTAS_FILE
                        Path to the COTTAS file to subtract
  -o OUTPUT_COTTAS_FILE, --output_cottas_file OUTPUT_COTTAS_FILE
                        Path to the output COTTAS file
  -i INDEX, --index INDEX
                        Zonemap index, e.g.: `SPO`, `PSO`, `GPOS`
  -r REMOVE_INPUT_FILES, --remove_input_files REMOVE_INPUT_FILES
                        Whether to remove the input COTTAS files after merging
```

#### Quick Check

Use this minimal end-to-end example to validate the CLI:

``` bash
cat > example.ttl << 'EOF'
<http://example.org/Alice> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
<http://example.org/Bob> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://example.org/Person> .
EOF

pycottas rdf2cottas -r example.ttl -c example.cottas -i SPO
pycottas verify -c example.cottas
pycottas info -c example.cottas
pycottas search -c example.cottas -t '?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?o'
pycottas cottas2rdf -c example.cottas -r example.nt
```

Expected behavior:

- `verify` returns `True`.
- `search` returns two tuples.
- `example.nt` is created with the same two triples.

## Tricks

### Multiple Files

Multiple COTTAS files can be simultaneously accessed with *list parameters* and *glob patterns*. Check [here](https://duckdb.org/docs/stable/data/multiple_files/overview.html#glob-syntax) the syntax for glob patterns.

``` py title="Example: Accessing multiple files with list parameters and glob patterns" hl_lines="3 5"
from pycottas import COTTASDocument

cottas_doc = COTTASDocument(['file1.cottas', 'file2.cottas', 'file3.cottas']) # (1)

cottas_doc = COTTASDocument('some_dir/*.cottas') # (2)

cottas_doc = COTTASDocument(['dir1/*.cottas', 'dir2/*.cottas']) # (3)

res = cottas_doc.search('?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?o')
```

1.  :rocket: Query three COTTAS files and treat them as a single one.
2.  :rocket: Query all COTTAS files that match the glob pattern.
3.  :rocket: Query all COTTAS files from two specific directories.

### Remote Files

COTTAS files can be read over HTTP.

``` py title="Example: Accessing a file over HTTP" hl_lines="3"
from pycottas import COTTASDocument

store = COTTASDocument('https://some.url/my_file.cottas')

res = cottas_doc.search('?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?o')
```


![OEG](assets/logo-oeg.png){ width="150" align=left } ![UPM](assets/logo-upm.png){ width="161" align=right }
