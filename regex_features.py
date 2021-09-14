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

# re.finditer - Iterator
# Faster than re.findall
print('*' * 20)

pattern = r"\d+"
text = 'Ny Postal Codes are 10001, 10002, 10003, 10004'

print('Pattern', pattern)
match_iter = re.finditer(pattern, text)

print('Matches')
for match in match_iter:
    print('\t', match.group(0), 'at index:', match.start())

# groups - find sub matches
print('*' * 20)
pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})"
text = 'Start Date: 20200920'

match = re.search(pattern, text)
if match:
    print(match.group(0), 'at index:', match.start())
    print('\t', match.groupdict())
else:
    print("no match")

# re.sub - find and replace
print('*' * 20)
pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})"
text = "Start Date: 20200920, End Date: 20210920"
replacement_pattern = r"\g<month>-\g<day>-\g<year>"

new_text = re.sub(pattern, replacement_pattern, text)
print('new text\t', new_text)

import datetime


def format_date(match):
    in_date = match.groupdict()

    year = int(in_date['year'])
    month = int(in_date['month'])
    day = int(in_date['day'])

    return datetime.date(year, month, day).strftime('%b-%d-%Y')


pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})"
text = "Start Date: 20200920, End Date: 20210920"
print('original text\t', text)
print()

new_text = re.sub(pattern, format_date, text)
print('new text\t', new_text)

# re.split - split text based on specified pattern
print('*' * 20)

pattern = r","
text = "a-c,x,y,1"

print(re.split(pattern, text))
