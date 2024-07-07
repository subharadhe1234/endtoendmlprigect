from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function read requirements.txt line by line and return list of requriments 
    '''
    requirements=[]
    with open(file_path) as fileobj:
        requirements=fileobj.readlines()
        requirements= [req.replace("\n","") for req in requirements] #this line use for to \n to null it may create to read the requirements.txt


        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
name="endtoendmlproject",
version='0.0.1',
author="radhe",
author_email="suhadippritihar09@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')




)