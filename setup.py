from setuptools import setup, find_packages
from typing import List


HYPEN_DOT_E = '-e.'

def get_requirements(file_path:str)->list[str]:

    requirements= []

    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace('\n',"") for req in requirements]

        if HYPEN_DOT_E in requirements:
         requirements.remove(HYPEN_DOT_E)

    return requirements


setup(
name= 'mlproject1',
version='0.0.1',
author= 'Sumeet Yadav',
author_email= 'sumeetyadav.official@gmail.com',
packages= find_packages(),
install_requires= get_requirements('requirements.txt')
)