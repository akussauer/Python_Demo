import distutils.core
from pkgutil import ImpImporter

print(f"Package distutils.core is available: {distutils.core is not None}")
print(f"Package pkgutil.ImpImporter is available: {ImpImporter is not None}")