from p03_tuple import first

a = (0,1,2,3,4,5,6,7,8,9)
b = range(10)
print(a)
print(b)

for i in a :
    print(i , end= ' ')
print("//")
d1 = {
    "hello" : 10, "world" : 20.5
}
print(d1["hello"])

keys = [ "hello", "are_you_there", "world" ]
for key in keys:
  print('-- Key:', key)

  value = d1[key] if key in d1 else '없는데요'
  print("value:",value)

  words = [
      "flagrant",
      "lawmaker",
      "allow",
      "alumina",
      "foxglove",
      "fiche",
      "concern",
      "kiosk",
      "clean",
      "especially",
      "wanton",
      "addle",
      "agitate",
      "whinchat",
  ]

  from collections import defaultdict
  counts = defaultdict(int)
  for word in words:
      first_ch = word[0]
      counts[first_ch] += 1

for ch in  counts.keys():
    print(ch,counts[ch])

for ch in sorted(counts.keys()):
    print(ch,counts[ch])

t1 = 1,2,'hello',3.5
t2 = (10,20)
print(t1,t2)
print()
num,index,name,score = t1
print(index,score)

arr = [100,200]
first,last = arr
print(first,last)

xy1 = 123,456
print(xy1[0],xy1[1])

xy2 = [234,567]
print(xy2[0],xy2[1])
xy2[1] += 10
print(xy2[0],xy2[1])


def func():
    print('This is a function')
func()
func()

class Hello:
    def func_print(self):
        print('asdasdsa')
    pass
h = Hello()

def func():
    return 'This is a string'
flags = [True, False, True]
for flag in flags:
    todo = Hello if flag else func
    obj = todo()
    print('flag값은 : ', flag, '이번에 얻은 것은 : ', obj)
h1 = Hello()
h2 = Hello()
h1.name = 'David'
h2.age = 20

students = [
    ('David',22,(4.3+4.0+3.3)/3),
    ('John Abdul', 25, (2.3 + 2.3 + 3.3) / 3),
    ('Chuck Norris', 124, (1.3 + 1.0 + 3.0) / 3),
    ('Karl Marx', 21, (3.3 + 2.0 + 4.3) / 3),
]

for st in students:
    name, age, score = st
    print(f'{name:^15}:{age:4}:{score:05.2f}')

david = {'name':'David','age':22,'score':3.866666}
print('%(name)-15s:%(age)4s : %(score)05.2f' % david)

class Student : pass

student = Student()
student.name = 'David'
student.age = 22
student.score = 3.866666

print('{p.name:^15s} : {p.age:4} : {p.score:.2f}'.format(p=student))
print(f'{student.name:^15s} : {student.age :4} : {student.score:.2f}')