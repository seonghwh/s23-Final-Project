import click

from s23openalex import Works

@click.command()
def main(oaid: str):
    work = Works(oaid)
    return work.ris


# if __name__ == '__main__':
  #   main(oaid)
