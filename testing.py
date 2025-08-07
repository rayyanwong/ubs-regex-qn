from main import generate_gree_expression
from testcases import getTestCases


if __name__ == "__main__":
    testCases = getTestCases()
    for i, test in enumerate(testCases):
        print("Test index: ", i)
        print(generate_gree_expression(test["valid"], test["invalid"]))

    # print(
    #     satisfies_both(
    #         r"^\D+@\w+\.\w+$", testCases[4]["valid"], testCases[4]["invalid"]
    #     )
    # )
