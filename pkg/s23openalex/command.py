import click

from s23openalex import Works

@click.argument('oaid', nargs=-1)
def main(oaid):
    work = Works(oaid)
    return work.ris


if __name__ == '__main__':
    main(oaid)
