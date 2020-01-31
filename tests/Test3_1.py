"""
/*
 * @Author: ThaumicMekanism [Stephan K.]
 * @Date: 2020-01-30 11:06:30
 * @Last Modified by: ThaumicMekanism [Stephan K.]
 * @Last Modified time: 2020-01-30 15:24:50
 */
"""
from GradescopeBase import Autograder, AutograderTest, Max, SubTest, SubTestRunner

Test3 = AutograderTest(SubTestRunner(pass_fail_ratio=3/4), "Test 3.1: Subtests", 2)

@SubTest(Test3, "Passes and empty print!")
def st1(ag: Autograder, test: AutograderTest):
    return True

@SubTest(Test3, "Passes with printing!")
def st2(ag: Autograder, test: AutograderTest):
    test.print("IM SOME MESSAGE")
    test.print("IM ON NEW LINE")
    return True

@SubTest(Test3, "I FAIL!")
def st3(ag: Autograder, test: AutograderTest):
    test.print("you shall not pass")
    return False

@SubTest(Test3, "Passes and empty print!")
def st4(ag: Autograder, test: AutograderTest):
    return True
