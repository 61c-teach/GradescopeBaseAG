"""
/*
 * @Author: ThaumicMekanism [Stephan K.]
 * @Date: 2020-01-30 11:06:30
 * @Last Modified by: ThaumicMekanism [Stephan K.]
 * @Last Modified time: 2020-01-30 13:59:43
 */
"""
from GradescopeBase import Autograder, AutograderTest, Max, SubTest, SubTestRunner

class CustomSubTestRunner(SubTestRunner):
    def post_test_run(self, ag: Autograder, test: AutograderTest, data: dict):
        if data["passed"]:
            test.print("You have passed this test, here is a secret message: :)")
Test4 = AutograderTest(CustomSubTestRunner(), "Test 4: Subtests Complex", 2)

@SubTest(Test4, "Passes and empty print!")
def st1(ag: Autograder, test: AutograderTest):
    return True

@SubTest(Test4, "Passes with printing!")
def st2(ag: Autograder, test: AutograderTest):
    test.print("IM SOME MESSAGE")
    test.print("IM ON NEW LINE")
    return True
