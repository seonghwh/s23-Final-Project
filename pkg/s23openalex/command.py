import click
from s23openalex import Works

@click.command()
@click.argument('oaid', nargs=1)
def main(oaid):
    work = Works(oaid)
    return work.ris
