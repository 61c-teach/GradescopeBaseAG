"""
This is a test in gradescope.
"""

from . import Visibility

global_tests = []

class Max:
    pass

default_visibility = None
class AutograderTest:
    def __init__(self, 
        test_fn,
        name: str=None, 
        max_score: float=None, 
        number: str=None, 
        tags: [str]=None, 
        visibility: Visibility=default_visibility, 
        extra_data=None,
        kill_autograder_on_error: bool=False
    ):
        """
        The test_fn MUST take in parameters Autograder and AutograderTest in that order.
        It is how the test will interact with the autograder.
        """
        self.test_fn = test_fn
        self.max_score = max_score
        self.name = name
        self.number = number
        self.tags = tags
        self.visibility = visibility
        self.extra_data = extra_data
        self.score = None
        self.output = ""
        self.kill_autograder_on_error = kill_autograder_on_error
        global_tests.append(self)

    def print(self, *args, sep=' ', end='\n', file=None, flush=True):
        self.output += sep.join(args) + end

    def set_score(self, score):
        self.score = score

    def run(self, ag):
        def f():
            r = self.test_fn(ag, self)
            if isinstance(r, (int, float)):
                self.set_score(r)
            if isinstance(r, Max) and self.max_score is not None:
                self.set_score(self.max_score)
        def handler():
            if self.kill_autograder_on_error:
                return True
            self.print("An unexpected error occured in the Autograder when attempting to run this testcase! Please contact a TA if this persists.")
            return False
        ag.safe_env(f, handler=handler)

    def get_results(self):
        data = {"output": self.output}
        if self.max_score is not None:
            data["max_score"] = self.max_score
        if self.name is not None:
            data["name"] = self.name
        if self.number is not None:
            data["number"] = self.number
        if isinstance(self.tags, list):
            data["tags"] = self.tags
        if self.visibility is not None:
            data["visibility"] = self.visibility
        if self.extra_data is not None:
            data["extra_data"] = self.extra_data
        if self.score is not None:
            data["score"] = self.score
        return data

    