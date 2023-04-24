"""Setup for s23openalex package."""
from setuptools import setup


setup(
    name="s23openalex",
    version="0.0.1",
    description="Works class with bibtex and RIS attributes.",
    maintainer="Seonghwan Hong",
    maintainer_email="seonghwh@andrew.cmu.edu",
    license="MIT",
    packages=["s23openalex"],
    entry_points={"console_scripts": ["openalex = s23openalex.command:main"]},
    scripts=[],
    long_description="""Works class with bibtex and RIS attributes.""",
)
