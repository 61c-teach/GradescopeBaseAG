from helper import AutograderTest, Max

def Test2_fn(ag, test: AutograderTest):
    test.print("Second test!")
    test.print("It only gives half points.")
    return test.max_score / 2

Test2 = AutograderTest(Test2_fn, "Test 2: Second Test - Partial", 2)