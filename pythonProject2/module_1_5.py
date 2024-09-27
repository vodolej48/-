immutable_var = tuple([1,3,5,'string', False,[1,3,5]])
print(immutable_var)
print(type(immutable_var))
mutable_list = [1,3,5,'string', False,[1,3,5]]
print(mutable_list)
print(type(mutable_list))
mutable_list[2] = 8
print(mutable_list)
immutable_var[2] = 8