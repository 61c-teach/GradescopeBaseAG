import os
import importlib
#The exclude list is any python file you do not want to include.
exclude_list = ["lib.py"]
for r, d, f in os.walk(__file__[:-len("__init__.py")]):
    for file in sorted(f, reverse=True):
        if file.endswith(".py") and file[:-3] not in exclude_list:
            try:
                importlib.import_module(".{}".format(file[:-3]), package="tests")
            except Exception as e:
                print("Could not add a test file!")
                import traceback
                traceback.print_exc()
                print(e)
