import click
import csv
from cobra.io import read_sbml_model
from tqdm import tqdm

HEADER = ['relation_type', 'source_species', 'source_db', 'source_id', 'target_species', 'target_db', 'target_id']

@click.command()
@click.argument('organism', type=click.STRING)
@click.argument('bigg_model', type=click.Path(exists=False, dir_okay=False))
@click.argument('output', type=click.File('w'))
def mapping(organism, bigg_model, output):
    model = read_sbml_model(bigg_model)
    writer = csv.writer(output, dialect='excel-tab')
    writer.writerow(HEADER)
    for gene in tqdm(model.genes):
        try:
            ncbigene = gene.annotation['ncbigene']
        except KeyError:
            print(f'NCBI gene not found for {gene.id}')
        else:
            writer.writerow([
                'crossdb',
                organism,
                'BIGG',
                gene.id,
                organism,
                'NCBI',
                gene.annotation['ncbigene']
            ])

if __name__ == '__main__':
    mapping()
