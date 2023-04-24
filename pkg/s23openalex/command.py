"""Python file for command line utility."""
import click
from s23openalex import Works


@click.command()
@click.argument("oaid")
@click.argument("entry")
def main(oaid, entry):
    """Take oaid and type to output RIS or Bibtex entry."""
    work = Works(oaid)
    if entry == "ris":
        print(work.ris)
    elif entry == "bibtex":
        print(work.bibtex)
