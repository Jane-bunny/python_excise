# Rewrite coding examples

# Example 1a: Assignment operation for string
portugal_island = 'Madeira'

# Example 1b: Assignment operator for integer & tuple
uni_liverpool_age = 142
liverpool_teaching_areas = 114
uni_liverpool_age += 1

print(uni_liverpool_age)

#Example 1c: Assignment operator list
breakfast_list = ['coffee', 'apple', 'butter bread', 'tea', 'banana', 'cheese', 'grapes']

# Example 2a: Relational (comparison) operator
tweet = 'Let us go travel!'
if tweet == 'Let us go travel!':
    print('Juhu')
else:
    print('It is such a nice weather, right?')

# Example 2b: Relational (comparison) operator
iq_score = 100
if iq_score >= 160:
    print('super smart')
else:
    print('average')

# Example 3a: Membership operator not in
mylist = ['machine learning', 'nlp', 'deep learning', 'multi_system agent']
if 'data science' not in mylist:
    print('nonsense')

# Example 3b: Membership operator in 
customer_data = ['i would like to have a cup of tea']
if '€' in customer_data:
    print('payment')
elif '0123456789' in customer_data:
    print('card number')
else:
    print('Please insert the correct payment amount')

# Example 4: Arithmetic operators
a = 8 + 9
b = 89 - 5
c = 85 / 5
d = 25 // 4
e = 78 % 8
f = 2 ** 5

print(a, b, c, d, e, f, sep='\n')