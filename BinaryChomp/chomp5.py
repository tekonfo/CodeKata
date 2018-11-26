from IPython import embed
#  クロージャー使って実装する。


def chop(search_number, array):
    if len(array) == 0:
        return -1
    end = len(array) - 1
    start = 0

    def search(search_number, array):
        nonlocal start
        nonlocal end
        point = int((start + end)/2)
        if array[point] == search_number:
            return point
        elif array[point] < search_number:
            if start == end:
                return -1
            start = point + 1
            return search(search_number, array)
        else:
            if start == end:
                return -1
            end = point
            return search(search_number, array)
    return search(search_number, array)


# 実装内容自体は変わっていない。クロージャーを使うと変数を上に保存することができて引数で指定する必要がない。
