from setuptools import setup, find_packages
from typing import List

file_path = 'requirements.txt'

HYPER_DOT_E = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as file:
        requirements= file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPER_DOT_E in requirements:
            requirements.remove(HYPER_DOT_E)
    return requirements
        


setup(
    name='Phishing Detector',
    author='Techbots_Team',
    version ='0.0.1',
    author_email='gaurlokesh1211@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)

