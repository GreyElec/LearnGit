def question_one(num_list):
    res, temp_list = list(), list()
    for num in num_list:
        if not temp_list:
            temp_list.append(num)
        else:
            if temp_list[-1] + 1 == num:
                temp_list.append(num)
            else:
                if len(temp_list) > 1:
                    res.append('->'.join([str(min(temp_list)), str(max(temp_list))]))
                temp_list = [num]
    if len(temp_list) > 1:
        res.append('->'.join([str(min(temp_list)), str(max(temp_list))]))
    return res


def minimize_price_route():
    source_city,destination_city = input().split(',')
    route_table = dict()
    while True:
        try:
            from_city, to_city, price = input().split(',')
            if not from_city in route_table:
                route_table[from_city] = [[to_city,int()]]
        except expression as identifier:
            pass
