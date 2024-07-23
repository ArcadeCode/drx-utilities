'''
This file update all pip packages
'''

import pkg_resources
from subprocess import call
from concurrent.futures import ThreadPoolExecutor

def update_package(package):
    call(["pip", "install", "--upgrade", package])

# Obtenez la liste des paquets installés
packages = [dist.project_name for dist in pkg_resources.working_set]

# Parallélisez la mise à jour des paquets
with ThreadPoolExecutor() as executor:
    executor.map(update_package, packages)