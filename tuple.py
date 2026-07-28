tp=(11,22,33,44,55,66)
print(type(tp))
print(tp)
print(tp.index(22))
print(tp.count(33))
ls=list(tp)
print(ls)
ls.append(123)
print(ls)
tp=tuple(ls)
print(tp)

# member operator in python - it always return a boolean value
#types - 1. in  2. not in

# x="1234"
# y="2" in x
# print(y)

# x="1234"
# y="2" not in x
# print(y)

x=[1,2,3,4]
y=2 not in x
print(y)