from GradescopeBase import Autograder, global_tests
try:
    from tests import *
except Exception as exc:
    print("Failed to import a test!")
    print(exc)
try:
    Autograder.run()
except Exception as exc:
    print("Failed to run the autograder")
    print(exc)