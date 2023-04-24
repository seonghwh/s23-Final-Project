import argparse

from s23openalex import Works


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--oaid', type=str, help='The OpenAlex ID of the work.')
    parser.add_argument('--format', type=str, choices=['ris', 'bibtex'], default='ris', help='The output format.')
    args = parser.parse_args()

    work = Works(args.oaid)

    if args.format == 'ris':
        work.ris
    elif args.format == 'bibtex':
        work.bibtex


if __name__ == '__main__':
    main()
