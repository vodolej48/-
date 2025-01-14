
def get_pass(num):
    password=''
    for i in range(1, num):
        for j in range(2, num):
            if j <= i:
                continue
            if num % (i + j) == 0:
                password += str(i) + str(j)
    return password

n = int(input('Введите целое число от 3 до 20: '))

result = get_pass(n)
print('Пароль:', result)