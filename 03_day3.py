import itertools
RESULT = {'[0, 0]': 1}

def change_direction(current_direction):
     if current_direction == [ 1, 0 ]:
         return [ 0, 1 ]
     elif current_direction == [ 0, 1 ]:
         return [ -1, 0 ]
     elif current_direction == [ -1, 0 ]:
         return [ 0, -1 ]
     elif current_direction == [ 0, -1]:
         return [ 1, 0 ]


def one_iteration(val, input_data, steps, direction, position):
     i = 0
     while i < 2:  #  Each step value is relevant only twice (each traversal of the side of the sq)
         i += 1
         s = steps
         while steps != 0:
             position = [x + y for x, y in zip(position, direction)]  # Calculate the new position for the new value
             val += 1
             if val == input_data:
                 return True, val, direction, position
             steps -= 1
         direction = change_direction(direction)  # change direction by 90 degrees
         steps = s
     steps = steps + 1  # Increment steps and then recursively call the function
     return(one_iteration(val, input_data, steps,  direction, position))


# PART 2

def get_neighbor_positions(position):
    x_axis = [1, -1, 0]
    y_axis = [1, -1, 0]
    for possible_position in itertools.product(x_axis, y_axis):
        if possible_position != (0, 0):
            neighbor_position = [x + y for x, y in zip(
                position, list(possible_position))]
            yield neighbor_position


def find_closest_value(input_data, steps, direction, position):
    i = 0
    global RESULT
    while i < 2:
        i += 1
        s = steps
        while steps != 0:
            val = 0
            position = [x + y for x, y in zip(position, direction)]
            for neighbor_position in get_neighbor_positions(position):
                if RESULT.get(str(neighbor_position)):
                    val = val + RESULT.get(str(neighbor_position))
            RESULT[str(position)] = val
            if val > input_data:
                return val
            steps -= 1
        direction = change_direction(direction)
        steps = s
    steps += 1
    return(find_closest_value(input_data, steps, direction, position))

if __name__ == "__main__":
    input_data = 277678
    val = 1  # Initial value
    # Steps define how many times to move in a particular direction
    steps = 1 # Initial steps = 1, for each iteration steps increment
    direction = [1, 0]  # Initial direction, x,y
    position = [0, 0]  # Initial position/origin
    result_position = one_iteration(val, input_data, steps, direction, position)[-1]
    distance = sum((abs(i) for i in result_position))
    print(distance)  # Expected 475
    # PART 2
    input_data = 277678
    steps = 1
    direction = [1, 0]
    position = [0, 0]
    closest_number = find_closest_value(input_data, steps, direction, position)
    print(closest_number)  # Expected 279138
