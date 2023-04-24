"""Python file for command line utility."""
import click
from s23openalex import Works


@click.command()
@click.argument("oaid", "string")
def main(oaid, string):
    """Take oaid and type to output RIS or Bibtex entry."""
    work = Works(oaid)
    if string == "ris":
        print(work.ris)
    elif string == "bibtex":
        print(work.bibtex)
