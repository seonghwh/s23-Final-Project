from s23openalex import Works


ref_bibtex = """@journal-article{https://openalex.org/W2288114809,\n author = {John R. Kitchin},\n journal = {ACS Catalysis},\n number = {6},\n pages = {3894-3899},\n title = {Examples of Effective Data Sharing in Scientific Publishing},\n url = {https://doi.org/10.1021/acscatal.5b00538},\n volume = {5},\n year = {2015}\n}\n"""


def test_bibtex():
    w = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert ref_bibtex == w.bibtex
