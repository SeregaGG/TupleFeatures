def get_square_pairs(*args) -> list:
    square_list = []
    for pair in args:
        for item in pair:
            square_list.append((item, item ** item))

    return square_list


def uniq_square(square_list: list) -> list:
    square_values = [x[1] for x in square_list]
    uniq_value = square_values[0]
    uniq_list = [uniq_value]
    for i in range(1, len(square_values)):
        if square_values[i] == uniq_value:
            continue
        else:
            uniq_value = square_values[i]
            uniq_list.append(uniq_value)
    return uniq_list
