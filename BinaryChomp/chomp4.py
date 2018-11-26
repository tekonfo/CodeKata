from IPython import embed
#   今回はスライスしないパターンの再帰


def chop(search_number, array):
    if len(array) == 0:
        return -1
    return search(search_number, array, 0, len(array) - 1)


# 配列の番号を返す。再帰の為に使用する。
def search(search_number, array, start, end):
    point = int((start + end)/2)
    if array[point] == search_number:
        return point
    elif array[point] < search_number:
        if start == end:
            return -1
        return search(search_number, array, point + 1, end)
    else:
        if start == end:
            return -1
        return search(search_number, array, start, point)


# 今回は一回でパス。めっちゃ成長してるwww
# 長さを−１するとか、pointを＋１するとか面倒なところを切り出せているのでミスなくいけた気がする。
