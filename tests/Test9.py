"""
/*
 * @Author: ThaumicMekanism [Stephan K.]
 * @Date: 2020-01-30 11:06:30
 * @Last Modified by: ThaumicMekanism [Stephan K.]
 * @Last Modified time: 2020-01-30 15:24:50
 */
"""
from GradescopeBase import Autograder, AutograderTest, Max, SubTest, SubTestRunner

Test9 = AutograderTest(SubTestRunner(is_pass_fail=False), "Test 9: Subtests with assertions", 4)

@SubTest(Test9, "Passes and empty print!", max_score=1)
def st1(ag: Autograder, test: AutograderTest):
    return True

@SubTest(Test9, "Asserts and fails!", max_score=1)
def st2(ag: Autograder, test: AutograderTest):
    test.print("IM SOME MESSAGE")
    test.print("IM ON NEW LINE")
    assert False, "I will always fail!"
    return True

@SubTest(Test9, "I FAIL!", max_score=1)
def st3(ag: Autograder, test: AutograderTest):
    test.print("you shall not pass")
    return False

@SubTest(Test9, "Passes and empty print!", max_score=1)
def st4(ag: Autograder, test: AutograderTest):
    return True
