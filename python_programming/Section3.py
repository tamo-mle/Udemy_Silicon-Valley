# セクション3 「Pythonの基本」
# Lesson08
num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# Lesson09
print('Hi', 'Mike')
print('Hi', 'Mike', sep=',')
print('Hi', 'Mike', sep=',', end='\n')
print('Hi', 'Mike', sep=',', end='.\n')

# Lesson10
import math
result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

# Lesson11
print('Hello')
print("Hello")
print("I don't know")
print('I don\'t know')
print('Say "I don\'t know"')
print("Say \"I don't know\"")

print('Hello. \nHow are you?')
print(r'C:/name/name')
print('#############')
print("""\
Line1
Line2
Line3\
""")
print('#############')

print('Hi.' * 3)
print('Hi.' * 3 + 'Mike')
print('Py''thon')

prefix = 'py'
print(prefix + 'thon')

s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbb')

print(s)

# Lesson12
word = 'Python'
print(word[0])
print(word[-1])
print(word[0:2])
print(word[:2])
print(word[2:])

word = 'J' + word[1:]
print(word)
n = len(word)
print(n)

# Lesson13
s = 'My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('My')
print(is_start)

is_start = s.startswith('X')
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

# Lesson14/15
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Taro'
family = 'Yamada'
print(f'My name is {name} {family}. 私は {family} {name} です')