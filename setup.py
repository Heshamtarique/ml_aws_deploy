from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
# definging a function that will exture the req file
def get_requirements(file_path:str)->List[str]:
     # this will return list of requiremts
     requirements = [] 
     with open(file_path) as file_obj:     # opening the file that will be passed below
         requirements = file_obj.readlines()   
         # once get hte reqirement.. remove \n eveytime new line is read
         # pandas and hten \n and then numpy will be there
         requirements = [ req.replace( "\n", "") for req in requirements  ]
         # -e .    need not to come while running the packages
         if HYPEN_E_DOT in requirements:
             requirements.remove(HYPEN_E_DOT)
             
     return requirements




setup(
    name = "ml_aws_deploy",
    version='0.0.1',
    author= 'Hesham',
    author_email='heshamtarique.jmi@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('/Users/shabi/Desktop/desk/Hesham/my_files/k_notes2023/my_codes_kvr/ml_aws_deploy/requirements.txt')   # anotehr wat 
    # install_requires = ['pandas', 'numpy', 'seaborn', 'matplotlib'] # you can mention the requiremts here.
    
    
)

## ml_aws_deploy.egg-info   once run is a success, we will get this folder