from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser import dumps
import requests

class Works:
    def __init__(self, oaid):
        self.oaid = oaid
        self.req = requests.get(f'https://api.openalex.org/works/{oaid}')
        self.data = self.req.json()
        
    def __str__(self):
        return 'str'
        
    def __repr__(self):
        return 'repr'

    def bibtex(self):
        _authors = [au['author']['display_name'] for au in self.data['authorships']]
        if len(_authors) == 0:
            authors = 'Editorial'
        elif len(_authors) == 1:
            authors = _authors[0]
        else:
            authors = ', '.join(_authors[0:-1]) + ' and' + _authors[-1] 
        
        pages = '-'.join([self.data['biblio'].get('first_page', '') or '',
                          self.data['biblio'].get('last_page', '') or ''])
        
        db = BibDatabase()
        db.entries = [{
            'ID': self.data['id'],
            'title': self.data['title'],
            'author': authors,
            'journal': self.data['host_venue']['display_name'],
            'volume': self.data['biblio']['volume'],
            'number': self.data['biblio']['issue'],
            'pages': pages,
            'year': str(self.data['publication_year']),
            'url': self.data['doi'],
            'ENTRYTYPE': self.data['type']
        }]
        writer = BibTexWriter()
        entry = dumps(db, writer)
        return print(entry)
