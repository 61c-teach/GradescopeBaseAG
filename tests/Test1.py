from GradescopeBase import AutograderTest, Max, Test

@Test("Test 1: First test", 2)
def Test1_fn(ag, test: AutograderTest):
    test.print("This is the first test! It will always pass :)")
    return Max()