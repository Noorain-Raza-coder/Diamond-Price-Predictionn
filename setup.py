from setuptools import find_packages , setup
from typing import List


def requirements_list(file_path:str)->List[str]:
    with open(file_path , 'r') as file_obj:
        req_list = file_obj.readlines()
        req_list = [library.strip() for library in req_list]   # removing \n character from list of strings

        if '-e .' in req_list:          # removing -e . from requirement list
            req_list.remove('-e .')

    return req_list


setup(
    name= "DiamondPricePrediction",
    version= '0.0.1',
    author= 'Noorain Raza',
    author_email= 'noorain2raza@gmail.com',
    install_requirements = requirements_list('requirements.txt'),
    packages= find_packages()
)