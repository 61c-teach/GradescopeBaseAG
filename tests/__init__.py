import os
import importlib
#The exclude list is any python file you do not want to include.
exclude_list = []
for r, d, f in os.walk(__file__[:-len("__init__.py")]):
    for file in f:
        if file.endswith(".py") and file[:-3] not in exclude_list:
            importlib.import_module(".{}".format(file[:-3]), package="tests")
