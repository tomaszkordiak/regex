import re

# re. match - find first match

pattern = r"\d+"
text = "42 is my lucky number"
match = re.match(pattern, text)
if match:
    print(match.group(0), 'at index:', match.start())
else:
    print("no match")


# input validation
def is_integer(text):
    pattern = r"^\d+$"
    match = re.match(pattern, text)
    if match:
        return True
    else:
        return False


def test_is_integer():
    pass_list = ['123', '456', '900', '0991']
    fail_list = ['a123', '124a', '1 2 3', '1\t2', ' 12', "45 "]

    for text in pass_list:
        if not is_integer(text):
            print('\tFailed to detect an integer', text)

    for text in fail_list:
        if is_integer(text):
            print('\tIncorrectly classified as an integer', text)

    print('test complete')


test_is_integer()

# re.search - Find the first match anywhere

pattern = r"\d+"
text = " is my lucky number 42"
match = re.search(pattern, text)
if match:
    print(match.group(0), 'at index:', match.start())
else:
    print("no match")


# re.findall - Find all the matches
pattern = r"\d+"
text = 'Ny Postal Codes are 10001, 10002, 10003, 10004'

print('Pattern', pattern)
match = re.findall(pattern, text)
if match:
    print('Found', match)
else:
    print("no match")

