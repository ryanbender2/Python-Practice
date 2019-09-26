"""
Nathan, Ryan, Jon
Liberty University
Python team ACM Competition
"""


def check_distance(point1, point2):
    dist_x = abs(point1[0] - point2[0])
    dist_y = abs(point1[1] - point2[1])
    distance_total = dist_x + dist_y
    return(distance_total)


def get_distance_from_points(point, input_list):
    distance = 0
    for p in input_list:
        distance += check_distance(point, p)
    return(distance)


def find_shortest_distance(input_list, grid):
    previous_distance = grid[0]*grid[1]
    meeting_point = (grid[0], grid[1])
    for x in range(1, grid[0] + 1):
        for y in range(1, grid[1] + 1):
            point = (x, y)
            distance = get_distance_from_points(point, input_list)
            if ((previous_distance > distance) or
               (previous_distance == distance) and
               ((meeting_point[0] > point[0] and meeting_point[1] > point[1]) or
               (meeting_point[0] == point[0] and meeting_point[1] > point[1]) or
               (meeting_point[0] > point[0] and meeting_point[1] == point[1]))):
                previous_distance = distance
                meeting_point = point
    return(meeting_point)


with open('test_case.txt') as test_case:
    all_cases = [i.split() for i in test_case.read().split('\n')]

current_line = 1
for _ in range(int(all_cases[0][0])):
    num_of_avenues = int(all_cases[current_line][1])
    num_of_streets = int(all_cases[current_line][0])
    num_of_friends = int(all_cases[current_line][2])
    grid = (num_of_avenues, num_of_streets)
    friends_list = []

    for f in range(num_of_friends):
        current_line += 1
        friend = (int(all_cases[current_line][1]), int(all_cases[current_line][0]))
        friends_list.append(friend)

    meeting_point = find_shortest_distance(friends_list, grid)
    print("(Street: {}, Avenue: {})".format(meeting_point[0], meeting_point[1]))
    current_line += 1





