import math

def spark(numbers):
    """Generate a text based sparkline graph from a list of numbers (ints or
    floats).

    Based on:
      https://github.com/holman/spark
    and:
      http://www.datadrivenconsulting.com/2010/06/twitter-sparkline-generator/
    """

    out = []

    min_value = min(numbers)
    max_value = max(numbers)
    value_scale = max_value - min_value

    for number in numbers:
        if (number - min_value) != 0 and value_scale != 0:
            scaled_value = (number - min_value) / value_scale
        else:
            scaled_value = 0
        num = math.floor(min([6, (scaled_value * 7)]))

        # Hack because 9604 and 9608 aren't vertically aligned the same as
        # other block elements
        if num == 3:
            if (scaled_value * 7) < 3.5:
                num = 2
            else:
                num = 4
        elif num == 7:
            num = 6

        out.append(unichr(int(9601 + num)))

    return ''.join(out)
