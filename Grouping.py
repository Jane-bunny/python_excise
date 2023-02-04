# Grouping and capturing
import re

# Define subexpression or group
print(re.search('(bar)', 'foo bar baz')) # Same re.search('bar', 'foo bar baz')

# Treating a Group as a Unit
print(re.search('(bar)+', 'foo bar baz'))
print(re.search('(bar)+', 'foo barbar baz'))
print(re.search('(bar)+', 'foo barbarbarbar baz'))

# Compare with bar+
print(re.search('bar+', 'foo bar baz'))
print(re.search('bar+', 'foo barbar baz'))
print(re.search('bar+', 'foo barbarbarbar baz'))

# Groupped search
print(re.search('(ba[rzs]){2,4}(qux)?', 'bazbarbazbasqux'))

# Compare
print(re.search('(ba[rzs]){2,4}(qux)?', 'bazbaybasbaybaybayqux')) # noticed that the group need to be squenced and the number need to matched

# Nested group
print(re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar'))

# Comparision
print(re.search('foo(bar)?', 'foofoobar123'))
print(re.search('(foo(bar)?)+(\d\d\d)?', 'foofoobar123'))

# Capture group
m = re.search('(\w+),(\w+),(\w+)', 'foo,quux,baz')
print(m)

print(m.groups())

print(m.group(1))

print(m.group(1, 2)) # Notice that a tuple is created

# Backreference
m = r'(\w+),\1'
n = re.search(m, 'foo,foo')

print(n.group(1))

n =re.search(m, 'foo,qux') # Notice the two words are not the same
print(n)

regex = r'^(###)?foo(?(1)bar|baz)'
print(re.search(regex, '###foobar'))
print(re.search(regex, '###foobaz'))
print(re.search(regex, 'foobar'))
print(re.search(regex, 'foobaz'))

regex = r'^(?P<ch>\W)?foo(?(ch)(?P=ch)|)$' # Notice the ch  need to be the same
print(re.search(regex, 'foo'))
print(re.search(regex, '#foo#'))
print(re.search(regex, '@foo@'))
print(re.search(regex, '#foo'))
print(re.search(regex, 'foo@'))
print(re.search(regex, '#foo@'))
print(re.search(regex, '@foo#'))

# Positive lookahead (?=<lookahead_regex>)
print(re.search('foo(?=[a-z])', 'foobar'))
print(re.search('foo(?=[a-z])(?P<ch>.)', 'foobar'))
print(re.search('foo([a-z])(?P<ch>.)', 'foobar'))
# Negative lookahead (?!<lookahead_regex>)
print(re.search('foo(?![a-z])', 'foobar'))
# Positive lookbehind: (?<=<lookbehind_regex>)
print(re.search('(?<=foo)bar', 'foobar'))
# Negative lookbehind (?<!<lookbehind_regex>)
print(re.search('(?<!qux)bar', 'foobar'))