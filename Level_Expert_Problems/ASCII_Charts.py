""" ASCII Charts (Part 2: Bar Chart)
  Given a dictionary containing quarterly sales values for a year,
  return a string representing a bar chart of the sales by quarter.
    - Quarter names (Q1, Q2, Q3, Q4) should appear on the left.
    - Quarters should be sorted in descending order by value.
    - Quarters with the same value should be shown in their yearly order (Q1 -> Q4).
    - Bars should begin with a "|".
    - Repeat the character "#" to fill the bar, with each
        character having a value of 50.
    - A single space comes after the bar, then the sales for that quarter.
    - If the value is 0, there should be no space after "|".
    - Use the newline character ("\n") to separate each bar in the chart.
"""
import operator


def bar_chart(results):
    order_results = sorted(results.items(),
                           key=operator.itemgetter(1),
                           reverse=True)
    figures = {"Q1": "", "Q2": "", "Q3": "", "Q4": ""}

    for key in results:
        num = results[key] / 50
        hashes = ''
        for _ in range(int(num)):
            hashes += '#'
        figures.update({key: hashes})

    first_pos = [order_results[0][0],
                 figures[str(order_results[0][0])],
                 order_results[0][1]]
    second_pos = [order_results[1][0],
                  figures[str(order_results[1][0])],
                  order_results[1][1]]
    third_pos = [order_results[2][0],
                 figures[str(order_results[2][0])],
                 ' ' + str(order_results[2][1])]
    fourth_pos = [order_results[3][0],
                  figures[str(order_results[3][0])],
                  ' ' + str(order_results[3][1])]

    """
        I'm so sorry about all these checks.
        there is a much, MUCH better way to do this, I'm just too lazy...
    """
    if third_pos[2] == ' 0':
        third_pos[1] = '0'
        third_pos[2] = ''
    if fourth_pos[2] == ' 0':
        fourth_pos[1] = '0'
        fourth_pos[2] = ''
    if first_pos[2] == second_pos[2]:
        if first_pos[0][1] > second_pos[0][1]:
            first_pos[0] = order_results[1][0]
            second_pos[0] = order_results[0][0]
    if (' ' + str(second_pos[2])) == third_pos[2]:
        if second_pos[0][1] > third_pos[0][1]:
            second_pos[0] = order_results[2][0]
            third_pos[0] = order_results[1][0]
    if third_pos[2] == fourth_pos[2]:
        if third_pos[0][1] > fourth_pos[0][1]:
            third_pos[0] = order_results[3][0]
            fourth_pos[0] = order_results[2][0]
            if third_pos[1] == '0' and fourth_pos[1] == '0':
                third_pos[0] = order_results[3][0]
                fourth_pos[0] = order_results[2][0]
    # ending of the death checks

    newstring = "{}|{} {}\n{}|{} {}\n{}|{}{}\n{}|{}{}"\
        .format(first_pos[0], first_pos[1], first_pos[2],
                second_pos[0], second_pos[1], second_pos[2],
                third_pos[0], third_pos[1], third_pos[2],
                fourth_pos[0], fourth_pos[1], fourth_pos[2])

    return newstring


print(bar_chart({'Q2': 550, 'Q3': 1000, 'Q4': 0, 'Q1': 600}))
