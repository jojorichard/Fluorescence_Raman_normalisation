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
     dependency_links=[
        'https://github.com/jojorichard/Fluorescence_Raman_normalisation.git#egg=Fluorescence_Raman_normalisation'
    ],
    url='https://github.com/jojorichard/Fluorescence_Raman_normalisation',  
    author='Jonas Richard', 
    author_email='jonas.richard@hotmail.fr',  
    maintainer='Justine Serra, Coralie Reuse, Jonas Richard',  
    maintainer_email='justine.serratosio@gmail.com, coralie.reuse23@gmail.com, jonas.richard@hotmail.fr', 
    description='Un package pour l’analyse des données de fluorescence',  
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown', 
)
