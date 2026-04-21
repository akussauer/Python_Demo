import pandas as pd

version = pd.__version__
print(f"pandas version: {version}")

import distutils.core
from pkgutil import ImpImporter

print(f"Package distutils.core is available: {distutils.core is not None}")
print(f"Package pkgutil.ImpImporter is available: {ImpImporter is not None}")