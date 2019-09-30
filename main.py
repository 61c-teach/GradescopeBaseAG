from GradescopeBase import Autograder, RateLimit, global_tests
try:
    from tests import *
except Exception as exc:
    print("Failed to import a test!")
    print(exc)
try:
    """
    Here is an example of how to use the ratelimit.
    We are giving students 3 tokens where a token will
    take 12 hours to regenerate. If you do not want to rate
    limit, you can replace the following three lines with:
    Autograder.run()
    """
    rate_limit = RateLimit(3, hours=12)
    rate_limit_ag = Autograder(rate_limit)
    Autograder.run(rate_limit_ag)
except Exception as exc:
    print("Failed to run the autograder")
    print(exc)