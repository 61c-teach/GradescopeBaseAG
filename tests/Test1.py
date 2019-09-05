from GradescopeBase import AutograderTest, Max, Test

@Test("Test 1: First test", 2, timeout=1)
def Test1_fn(ag, test: AutograderTest):
    test.print("This is the first test! It will always pass :)")
    import time
    time.sleep(10)   
    return Max()