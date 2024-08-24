from setuptools import setup, find_packages

    

setup(
    name             ='reqio',
    version          ='0.1.0.0',
    description      ='reqio Library',
    author           ='Duckling Dean',
    author_email     ='duckling.dean@proton.me',
    package_dir      ={'': 'src'},
    packages         =find_packages(where='src'),
    include_package_data=True,
    project_urls     ={
        "Source" : "https://github.com/DucklingDean/reqio",
    },
    install_requires = [
        "requests>=2.32.2,<3.0.0",
        "fake-useragent==1.5.1",
    ]
)

