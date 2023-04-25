"""Test for bibtex attribute."""
from s23openalex import Works


REF_BIBTEX = """@journal-article{https://openalex.org/W2288114809,
 author = {John R. Kitchin},
 journal = {ACS Catalysis},
 number = {6},
 pages = {3894-3899},
 title = {Examples of Effective Data Sharing in Scientific Publishing},
 url = {https://doi.org/10.1021/acscatal.5b00538},
 volume = {5},
 year = {2015}
}
"""


def test_bibtex():
    """Test function for bibtex."""
    work = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert REF_BIBTEX == work.bibtex
