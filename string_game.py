import operator

def bar_chart(results):
    order_results = sorted(results.items(), key=operator.itemgetter(1), reverse=True)
    figures = {"Q1": "", "Q2": "", "Q3": "", "Q4": ""}

    for key in results:
        num = results[key] / 50
        hashes = ''
        for i in range(int(num)):
            hashes += '#'
        figures.update({key: hashes})

    first_pos = [order_results[0][0], figures[str(order_results[0][0])], order_results[0][1]]
    second_pos = [order_results[1][0], figures[str(order_results[1][0])], order_results[1][1]]
    third_pos = [order_results[2][0], figures[str(order_results[2][0])], ' ' + str(order_results[2][1])]
    fourth_pos = [order_results[3][0], figures[str(order_results[3][0])], ' ' + str(order_results[3][1])]

    if third_pos[2] == ' 0':
        third_pos[1] = '0'
        third_pos[2] = ''
    if fourth_pos[2] == ' 0':
        fourth_pos[1] = '0'
        fourth_pos[2] = ''

    newstring =  "{}|{} {}\n{}|{} {}\n{}|{}{}\n{}|{}{}"\
        .format(first_pos[0], first_pos[1], first_pos[2],
                second_pos[0], second_pos[1], second_pos[2],
                third_pos[0], third_pos[1], third_pos[2],
                fourth_pos[0], fourth_pos[1], fourth_pos[2])

    return newstring
""" just need to figure out how to make the Q's come out in order if both 0 """


print(bar_chart({'Q4': 0, 'Q3': 100, 'Q2': 0, 'Q1': 600}))