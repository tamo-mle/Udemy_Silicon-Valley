# Section4
# Lesson18
r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3, 3))

print(r.count(3))

if 5 in r:
    print('exist')

if 100 in r:
    print('exist')

r.sort()
print(r)

r.reverse()
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)


# Lesson19
i = [1 ,2, 3, 4, 5, 6, 7, 8, 9 ,10]
j = i
j[0] = 100
print(i)
print(j)

x = [1 ,2 ,3, 4, 5, 6, 7, 8, 9, 10]
y = x.copy()

y[0] = 100

print(x)
print(y)

X = 20
Y = X
Y = 5

print(id(X))
print(id(Y))

print(X)
print(Y)

XX = [1 , 2]
YY = XX
YY[0] = 9

print(id(XX))
print(id(YY))

print(XX)
print(YY)


# Lesson22
num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

min, max = 0, 100
print(min, max)

i = 10
j = 20

tmp = i
i = j
j = tmp

print(i, j)

a = 100
b = 200
print(a, b)

a, b = b, a
print(a,b)


# Lesson23
chose_from_two = ('a', 'b', 'c')
answer = []
answer.append('a')
answer.append('c')

print(chose_from_two)
print(answer)


#Lesson26
x = {'a': 1}
y = x
y['a'] = 1000

print(x)
print(y)

x = {'a': 1}
y = x.copy()

y['a'] = 2000
print(x)
print(y)

# Lesson27
fruits = {
    'apple': 100,
    'banana': 150,
    'orange': 200
    }

print(fruits['apple'])


# Lesson30
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}

print(my_friends & A_friends)


f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)