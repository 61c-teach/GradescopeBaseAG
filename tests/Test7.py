"""
/*
 * @Author: ThaumicMekanism [Stephan K.]
 * @Date: 2020-01-30 11:06:30
 * @Last Modified by: ThaumicMekanism [Stephan K.]
 * @Last Modified time: 2020-01-30 16:20:10
 */
"""
from GradescopeBase import Autograder, AutograderTest, Max, SubTest, SubTestRunner

class CustomSubTestRunner(SubTestRunner):
    def post_test_run(self, ag: Autograder, test: AutograderTest, data: dict):
        if self.did_pass(data):
            test.print("\nYou have passed this test, here is a secret message: :)")
Test4 = AutograderTest(CustomSubTestRunner(is_pass_fail=False), "Test 7: Subtests Complex", 2)

@SubTest(Test4, "Passes and empty print!", max_score=1)
def st1(ag: Autograder, test: AutograderTest):
    return 0.5

@SubTest(Test4, "Passes with printing!", max_score=1)
def st2(ag: Autograder, test: AutograderTest):
    test.print("IM SOME MESSAGE")
    test.print("IM ON NEW LINE")
    # raise Exception()
    return True
