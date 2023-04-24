"""Python file for command line utility."""
import click
from s23openalex import Works


@click.command()
@click.argument("oaid")
@click.argument("type")
def main(oaid, type):
    """Take oaid and type to output RIS or Bibtex entry."""
    work = Works(oaid)
    if type == "ris":
        print(work.ris)
    elif type == "bibtex":
        print(work.bibtex)
