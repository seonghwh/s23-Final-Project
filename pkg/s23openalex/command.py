import argparse

# from s23openalex import Works
from .works import Works


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--doi', type=str, help='The doi of the work.')
    parser.add_argument('--format', type=str, choices=['ris', 'bibtex'], default='ris', help='The output format.')
    args = parser.parse_args()

    work = Works(args.doi)

    if args.format == 'ris':
        work.ris
    elif args.format == 'bibtex':
        work.bibtex


if __name__ == '__main__':
    main()
