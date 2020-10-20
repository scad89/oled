def find_double_ints(ls):

    ls.sort()
    num = 0
    for i in ls:
        if i != num:
            num = i
        elif i == num:
            print(f'Double int {i}')
            break


ls = []
for i in range(int(input('How many items does the list contain: '))):
    num = int(input())
    ls.append(num)

find_double_ints(ls)
