num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
if num_1 == num_2 and num_3 == num_2 and num_3 == num_1:
    print(3)
elif num_1 == num_2 or num_3 == num_2 or num_3 == num_1:
    print(2)
else:
    print(0)