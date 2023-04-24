import click

from s23openalex import Works

@click.command()
@click.argument('doi', nargs=-1)
def main(doi):
    work = Works(doi)
    print(work.ris)


# if __name__ == '__main__':
  #   main(oaid)
