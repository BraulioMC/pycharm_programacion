from setuptools import setup, find_packages
setup(
    name="PyLogin",
    version="0.1",
    packages=find_packages(),
    # scripts=['pylogin.py', 'db.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    # install_requires=[''],

    # package_data={
    #     # If any package contains *.txt or *.rst files, include them:
    #     '': ['*.txt', '*.rst'],
    #     # And include any *.msg files found in the 'hello' package, too:
    #     'hello': ['*.msg'],
    # },

    # metadata to display on PyPI
    author="Braulio",
    author_email="A18BraulioMC@iessanclemente.net",
    description="This is an Project Package",
    license="PSF",
    keywords="login window with db connect",
    url="http://example.com/",   # project home page, if any
    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # }

    # could also include long_description, download_url, classifiers, etc.
)