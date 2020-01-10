from GradescopeBase import Autograder, RateLimit, global_tests
rate_limit = False
try:
    from tests import *
except Exception as exc:
    print("Failed to import a test!")
    print(exc)
try:
    print("Successfully imported tests")
    rlim = None
    if rate_limit:
        """
        Here is an example of how to use the ratelimit.
        We are giving students 6 tokens where a token will
        take 2 hours to regenerate. If you do not want to rate
        limit, can just set rlim to None.
        """
        rlim = RateLimit(6, hours=2)
    ag = Autograder(rlim)
    # ag.print("We are currently performing maintenance on the autograder so test may suddenly break. Thank you for your patients!")
    Autograder.run(ag)
except Exception as exc:
    print("Failed to run the autograder")
    print(exc)