testCases = [
    {
        "name": "Only letters allowed",
        "valid": ["abc", "def"],
        "invalid": ["123", "456"],
        "expected_regex": r"^\D+$",
    },
    {
        "name": "Starts with a",
        "valid": ["aaa", "abb", "acc"],
        "invalid": ["bbb", "bcc", "bca"],
        "expected_regex": r"^a.+$",
    },
    {
        "name": "Ends with 1",
        "valid": ["abc1", "bbb1", "ccc1"],
        "invalid": ["abc", "bbb", "ccc"],
        "expected_regex": r"^.+1$",
    },
    {
        "name": "Has - before 2",
        "valid": ["abc-1", "bbb-1", "cde-1"],
        "invalid": ["abc1", "bbb1", "cde1"],
        "expected_regex": r"^.+-.+$",
    },
    {
        "name": "Simple email",
        "valid": ["foo@abc.com", "bar@def.net"],
        "invalid": ["baz@abc", "qux.com"],
        "expected_regex": r"^\D+@\w+\.\w+$",
    },
    {
        "name": "Starts digit, ends letter",
        "valid": ["1abc", "2def", "3ghi"],
        "invalid": ["abc1", "def2", "ghi3"],
    },
    {
        "name": "Case-sensitive letters",
        "valid": ["Abc", "Aef"],
        "invalid": ["abc", "aef"],
    },
    {
        "name": "3 lowercase, 1 digit",
        "valid": ["abc1", "def2", "ghi3"],
        "invalid": ["abc", "def", "ghi", "1234"],
    },
    {
        "name": "Must start with 'K9-'",
        "valid": ["K9-ab", "K9-zz", "K9-12"],
        "invalid": ["k9-ab", "A9-zz", "K9ab"],
    },
    {
        "name": "Ends with .txt",
        "valid": ["file.txt", "dile.txt", "bile.txt"],
        "invalid": ["file.doc", "filetxt", "txt.file"],
    },
]


def getTestCases():
    return testCases
