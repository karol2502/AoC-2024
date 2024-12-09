with open('input.txt','r') as file:
    prob = 0

    left_list = []
    right_dict = {}

    for line in file:
        left, right = line.strip().split("   ")
        left_list.append(left)

        if right in right_dict:
            right_dict[right] += 1
        else :
            right_dict[right] = 1

    for left in left_list:
        if left in right_dict:
            prob += int(left) * int(right_dict[left])

    print(prob)