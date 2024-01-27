from setuptools import  setup
from typing import List







#Declaring varibales for set up function

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Ravi M B"
DESCRIPTION = "Trying to build Simple ML project"
PACKAGES= ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:

    """
    Description: This function is going to return list of requirments mentioned in requirments.txt file

    return: a list of name of libraries mentioned in requirements.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(

    name= PROJECT_NAME,
    version= VERSION,
    author= AUTHOR,
    description= DESCRIPTION,
    packages= PACKAGES,
    install_requires=get_requirements_list()
)


#if __name__=="__main__":
    #print(get_requirements_list())