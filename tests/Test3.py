"""
/*
 * @Author: ThaumicMekanism [Stephan K.]
 * @Date: 2020-01-30 11:06:30
 * @Last Modified by: ThaumicMekanism [Stephan K.]
 * @Last Modified time: 2020-01-30 13:42:03
 */
"""
from GradescopeBase import Autograder, AutograderTest, Max, SubTest

Test3 = AutograderTest(None, "Test 3: Subtests", 2)

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
