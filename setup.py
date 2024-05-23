from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines if line.strip() and not line.startswith('#')]

setup(
    name='EEM',  
    version='0.1',  
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    url='https://github.com/jojorichard/EEM',  
    author='Jonas Richard', 
    author_email='jonas.richard@hotmail.fr',  
    maintainer='Justine Serra, Coralie Reuse',  
    maintainer_email='justine.serratosio@gmail.com, coralie.resu23@gmail.com', 
    description='Un package pour l’analyse des données de fluorescence',  
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown', 
)
