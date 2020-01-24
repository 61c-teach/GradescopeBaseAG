"""
/*
 * @Author: ThaumicMekanism [Stephan K.] 
 * @Date: 2020-01-23 21:04:39 
 * @Last Modified by:   ThaumicMekanism [Stephan K.] 
 * @Last Modified time: 2020-01-23 21:04:39 
 */
"""
from GradescopeBase import AutograderTest, Max

def Test2_fn(ag, test: AutograderTest):
    test.print("Second test!")
    test.print("It only gives half points.") 
    return test.max_score / 2

Test2 = AutograderTest(Test2_fn, "Test 2: Second Test - Partial", 2)