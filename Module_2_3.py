my_list = [45, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
var = 0
while var < len(my_list):  # 0 < 12
    if my_list[var] >= 0:
        if my_list[var] != 0:
            print(my_list[var])
        var = var + 1
        continue
    else:
        break