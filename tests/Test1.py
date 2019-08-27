from helper import AutograderTest, Max

def Test1_fn(ag, test: AutograderTest):
    test.print("This is the first test! It will always pass :)")
    return Max()

Test1 = AutograderTest(Test1_fn, "Test 1: First test", 2)