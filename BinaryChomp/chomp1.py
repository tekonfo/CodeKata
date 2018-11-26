from IPython import embed
#   今回は再帰
count = 0
# これが初期化できてない


def chop(search_number, array):
    global count
    if len(array) % 2 == 1:
        array_count = int(len(array) / 2)
    elif len(array) == 0:
        return return_count(-1)
    else:
        array_count = int(len(array) / 2 - 1)
    if array[array_count] == search_number:
        return return_count(array_count + count)
    elif array[array_count] < search_number:
        count += array_count + 1
        if array_count == 0:
            return chop(search_number, array[array_count+1:])
        return chop(search_number, array[array_count+1:])
    elif array[array_count] > search_number:
        return chop(search_number, array[:array_count])
    else:
        return - 1


def return_count(number):
    global count
    count = 0
    return number


# やってみて、添え字が１プラスされるものと、されないものとの統合性を取ることが難しかった。
