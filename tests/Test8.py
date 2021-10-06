"""
/*
 * @Author: ThaumicMekanism [Stephan K.] 
 * @Date: 2020-01-23 21:04:29 
 * @Last Modified by: ThaumicMekanism [Stephan K.]
 * @Last Modified time: 2020-01-30 13:38:43
 */
"""
from GradescopeBase import AutograderTest, Max, Test

@Test("Test 8: Assert Fail", 2, timeout=1)
def Test8_fn(ag, test: AutograderTest):
    test.print("This test will fail due to an assertion error.")
    assert False, "I always fail"
    return Max()