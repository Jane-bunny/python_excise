import re

# Matching example, can also use if statement
s = "janebunny123go"

x = re.search('123', s)
print(x)

# Regex Metacharacters and pattern match
x = re.search('[0-9][0-9][0-9]', s)
print(x)

x = re.search('[0-9][0-9][0-9]', '12janebunny3go')
print(x)

x = re.search('1.3', s)
print(x)

x = re.search('13', s)
print(x)

x = re.search('[^0-9]', '12345foo') # Complement a character class. Only when '^' at the beginning of the to be searched character class
print(x)

x = re.search('foo.bar', 'fooxbar') # Dot (.), represent any single character except a newline
print(x)  

# As a regex, foo.bar essentially means the characters 'foo', then any character except newline, then the characters 'bar'

# \w alphanumeric
x = re.search('\w', '#(.a$@&') # Same as re.search('[a-zA-Z0-9_]', '#(.a$@&')
print(x)

# \W non-word character
x = re.search('\W', 'a_1*3Qb')
print(x)

# \d decimal. \D is not decimal
x = re.search('\d', 'abc4def')
print(x)

x = re.search('\D', '234Q678')
print(x)

# \s whitespace, \S is not whitespace, a newline \n is a whitespace
x = re.search('\s', 'foo bar baz')
print(x)

x = re.search('\S', 'foo bar baz')
print(x)

s = r'foo\bar'
x = re.search('\\\\', s)
print(x)

x = re.search(r"\\", s) # Raw string
print(x)

# ^ and \A begining of the string
x = re. search('^foo', 'foobar')
print (x)
print(re.search('^foo', 'barfoo'))

# $ and \Z the same principle, end of the string
x = re.search('bar$', 'foobar')
print(x)

# \b same as \w, but asserts the regex parser's current position must be at the beginning or end of a word. 
x = re.search('\\bbar', 'foo bar')
print(x)

x = re.search(r'\bbar', 'foo.bar')
print(x)

print(re.search(r'\bbar', 'foobar'))  # None
# Notice here r for raw string must be used, otherwise two \\b should be used
# Because \b is an escape sequence for both string literals and regexes 

# \B current position must not be at the start or end of a word
print(re.search(r'\Bfoo\B', 'foo'))

print(re.search(r'\Bfoo\B', '.foo.'))

x = re.search(r'\Bfoo\B', 'barfoobaz')
print(x)

for i in range(1, 6):
    s = f"x{'-' * i}x"
    print(f'{i}  {s:10}', re.search('x-{2,4}x', s))

x =  'I wish you 1 nice weekend, meet 3 friends, drink 2 beers.'
x1 = re.findall('\S', x)
print(x1)

x2 = re.findall('\W', x)
print(x2)

x3 = re.findall('\D', x)
print(x3)

x4 = re.findall('[AEIOUaeiou]', x)
print(x4)

x5 = re.findall('[^AEIOUaeiou]', x)
print(x5)

x6 = re.findall('[^AEIOUaeiou\s\d\.]', x)
print(x6)