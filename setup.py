from setuptools import setup, find_packages

    

setup(
    name             ='reqio',
    version          ='0.0.0',
    description      ='Initial',
    author           ='Duckling Dean',
    author_email     ='duckling.dean@proton.me',
    package_dir      ={'': 'src'},
    packages         =find_packages(where='src'),
    include_package_data=True,
    project_urls     ={
        "Source" : "https://github.com/DucklingDean/reqio",
    },
)

