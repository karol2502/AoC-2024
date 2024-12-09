with open('input.txt','r') as file:
    dist = 0

    left_list = []
    right_list = []

    for line in file:
        left, right = line.split("   ")
        left_list.append(left.strip())
        right_list.append(right.strip())

    left_list.sort()
    right_list.sort()

    for i in range(0, len(left_list)):
        dist += abs(int(left_list[i]) - int(right_list[i]))

    print(dist)