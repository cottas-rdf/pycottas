__author__ = "Julián Arenas-Guerrero"
__credits__ = ["Julián Arenas-Guerrero"]

__license__ = "Apache-2.0"
__maintainer__ = "Julián Arenas-Guerrero"
__email__ = "julian.arenas.guerrero@upm.es"


from pandas import DataFrame
from argparse import ArgumentParser

from .__init__ import *
from.constants import i_pos


EPILOG_TEXT = 'Copyright © 2023 Julián Arenas-Guerrero'


def main():
    parser = ArgumentParser(
        prog='pycottas',
        epilog=EPILOG_TEXT)

    subparsers = parser.add_subparsers(help='subcommand help', dest='subparser_name', required=True)

    parse_rdf2cottas = subparsers.add_parser('rdf2cottas', help='Compress an RDF file into COTTAS format', epilog=EPILOG_TEXT)
    parse_rdf2cottas.add_argument('-r', '--rdf_file', type=str, required=True, help='Path to RDF file')
    parse_rdf2cottas.add_argument('-c', '--cottas_file', type=str, required=True, help='Path to COTTAS file')
    parse_rdf2cottas.add_argument('-i', '--index', type=str, required=False, default='SPO', help='Zonemap index, e.g.: `SPO`, `PSO`, `GPOS`')
    parse_rdf2cottas.add_argument('-d', '--disk', type=bool, required=False, default=False, help='Whether to use on-disk storage')

    parse_cottas2rdf = subparsers.add_parser('cottas2rdf', help='Decompress a COTTAS file to RDF (N-Triples)', epilog=EPILOG_TEXT)
    parse_cottas2rdf.add_argument('-c', '--cottas_file', type=str, required=True, help='Path to COTTAS file')
    parse_cottas2rdf.add_argument('-r', '--rdf_file', type=str, required=True, help='Path to RDF file (N-Triples)')

    parse_cottas2rdf = subparsers.add_parser('search', help='Evaluate a triple pattern', epilog=EPILOG_TEXT)
    parse_cottas2rdf.add_argument('-c', '--cottas_file', type=str, required=True, help='Path to COTTAS file')
    parse_cottas2rdf.add_argument('-t', '--triple_pattern', type=str, required=True, help='Triple pattern, e.g., `?s <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?o`')
    parse_cottas2rdf.add_argument('-r', '--result_option', default='tuples', choices=['tuples', 'table', 'to_csv'], help='What to do with the result set')

    parse_info = subparsers.add_parser('info', help='Get the metadata of a COTTAS file', epilog=EPILOG_TEXT)
    parse_info.add_argument('-c', '--cottas_file', type=str, required=True, help='Path to COTTAS file')

    parse_verify = subparsers.add_parser('verify', help='Check whether a file is a valid COTTAS file', epilog=EPILOG_TEXT)
    parse_verify.add_argument('-c', '--cottas_file', type=str, required=True, help='Path to COTTAS file')

    parse_cat = subparsers.add_parser('cat', help='Merge multiple COTTAS files', epilog=EPILOG_TEXT)
    parse_cat.add_argument('--input_cottas_files', type=str, nargs='+', required=True, help='Path of the input COTTAS files')
    parse_cat.add_argument('--output_cottas_file', type=str, required=True, help='Path of the output COTTAS file')
    parse_cat.add_argument('-i', '--index', type=str, required=False, default='SPO', help='Zonemap index, e.g.: `SPO`, `PSO`, `GPOS`')
    parse_cat.add_argument('-r', '--remove_input_files', type=bool, required=False, default=False, help='Whether to remove input COTTAS files after merging')

    parse_diff = subparsers.add_parser('diff', help='Subtract the triples in a COTTAS files from another', epilog=EPILOG_TEXT)
    parse_diff.add_argument('-c', '--cottas_file', type=str, required=True, help='Path to the COTTAS file')
    parse_diff.add_argument('-s', '--subtract_cottas_file', type=str, required=True, help='Path to the COTTAS file to subtract')
    parse_diff.add_argument('-o', '--output_cottas_file', type=str, required=True, help='Path to the output COTTAS file')
    parse_diff.add_argument('-i', '--index', type=str, required=False, default='SPO', help='Zonemap index, e.g.: `SPO`, `PSO`, `GPOS`')
    parse_diff.add_argument('-r', '--remove_input_files', type=bool, required=False, default=False, help='Whether to remove the input COTTAS files after merging')

    args = parser.parse_args()

    if args.subparser_name == 'rdf2cottas':
        rdf2cottas(args.rdf_file, args.cottas_file, args.index, args.disk)

    elif args.subparser_name == 'cottas2rdf':
        cottas2rdf(args.cottas_file, args.rdf_file)

    elif args.subparser_name == 'search':
        if args.result_option == 'table':
            print(duckdb.query(translate_triple_pattern(f"{args.cottas_file}", args.triple_pattern)))
        elif args.result_option == 'to_csv':
            duckdb.query(translate_triple_pattern(f"{args.cottas_file}", args.triple_pattern)).df().to_csv(
                'cottas_search.csv', index=False)
        elif args.result_option == 'tuples':
            print(search(args.cottas_file, args.triple_pattern))

    elif args.subparser_name == 'info':
        print(info(args.cottas_file))

    elif args.subparser_name == 'verify':
        print(verify(args.cottas_file))

    elif args.subparser_name == 'cat':
        cat(args.input_cottas_files, args.output_cottas_file, args.index, args.remove_input_files)

    elif args.subparser_name == 'diff':
        index = args.index if args.index else 'spo'
        remove_input_files = args.remove_input_files if args.remove_input_files else False
        diff(args.cottas_file, args.subtract_cottas_file, args.output_cottas_file, args.index, args.remove_input_files)


if __name__ == "__main__":
    main()
