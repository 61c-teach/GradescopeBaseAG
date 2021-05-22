"""
/*
 * @Author: ThaumicMekanism [Stephan K.] 
 * @Date: 2020-01-23 20:57:54 
 * @Last Modified by: ThaumicMekanism [Stephan K.]
 * @Last Modified time: 2020-01-23 21:04:49
 */
"""
from GradescopeBase import Autograder, RateLimit, global_tests

if __name__ == "__main__":
    rate_limit = False
    
    rlim = None
    if rate_limit:
        """
        Here is an example of how to use the ratelimit.
        We are giving students 6 tokens where a token will
        take 2 hours to regenerate. If you do not want to rate
        limit, can just set rlim to None.
        """
        rlim = RateLimit(6, hours=2)

    autograder = Autograder(rate_limit=rlim)
    autograder.import_tests(tests_dir="tests", blacklist=["__init__.py", "lib.py"])
    autograder.run()