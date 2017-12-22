import click
import csv
import json
import gzip
from io import StringIO

HEADER = ['Species', 'Source', 'Type', 'Gene type', 'ID', 'Name', 'Full name', 'Description', 'Aliases']

@click.command()
@click.argument('organism', type=click.STRING)
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.Path(exists=False, dir_okay=False))
def converter(organism, input, output):
    data = json.load(input)
    genes = data['genes']
    # Do not import genes with no name
    genes = [g for g in genes if g['name']]
    str_buffer = StringIO()
    writer = csv.writer(str_buffer, dialect='excel-tab')
    writer.writerow(HEADER)
    for gene in genes:
        writer.writerow([
            'Homo sapiens',
            'BIGG',
            'gene',
            'protein_coding', # These are all enzymes
            gene['id'],
            gene['name'],
            '',
            '',
            ''
            ])
    str_buffer.seek(0)
    if output.endswith('.gz'):
        with gzip.open(output, 'w') as fp:
            fp.write(str_buffer.read().encode('utf-8'))
    else:
        with open(output, 'w') as fp:
            fp.write(str_buffer.read()

if __name__ == '__main__':
    converter()
