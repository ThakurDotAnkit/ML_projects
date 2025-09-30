from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirment
    '''
    HYPEN_E_DOT='-e .'
    requirements=[]
    with open(file_path) as fie_obj:
        requirements=fie_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(
    name="ml_project",
    version='0.0.1',
    auther="Ankit Thakur",
    author_email="ankitkitu456@gmail.com" ,
    package=find_packages(), 
    install_requires=get_requirements("requirement.txt")
)