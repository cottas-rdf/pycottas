[`pycottas-endpoint`](https://github.com/cottas-rdf/pycottas-endpoint) can quickly serve COTTAS files through a SPARQL endpoint.

## Installation

Install from [PyPI](https://pypi.org/project/pycottas-endpoint/) with:

```bash
pip install pycottas-endpoint
```

The `uvicorn` and `gunicorn` dependencies are not included by default, if you want to install them use the optional dependency `web`:

```bash
pip install "pycottas-endpoint[web]"
```

If you want to use `pycottas-endpoint` as a CLI you can install with the optional dependency `cli`:

```bash
pip install "pycottas-endpoint[cli]"
```

## Run SPARQL Endpoint

Use `pycottas-endpoint` as a command line interface (CLI) in your terminal to quickly serve one or multiple COTTAS files as a SPARQL endpoint.

You can use wildcard to provide multiple files, for example to serve all COTTAS files in the current directory you could run:

```bash
pycottas-endpoint serve '*.cottas'
```

Then access the YASGUI SPARQL editor on http://localhost:8000

## Further Reading

See all the information in the [pycottas-endpoint GitHub repository](https://github.com/arenas-guerrero-julian/pycottas-endpoint).
