from IPython import embed
#   今回は繰り返し


def chop(search_number, array):
    left_p = 0
    right_p = len(array) - 1
    if right_p == -1:
        return - 1
    while True:
        if left_p > (len(array) - 1) or right_p < 0 or left_p > right_p:
            return - 1
        # 真ん中を指定
        middle_p = int((left_p + right_p)/2)
        if array[middle_p] == search_number:
            return middle_p
        elif array[middle_p] > search_number:
            if right_p == left_p:
                return - 1
            right_p = middle_p - 1
        else:
            if right_p == left_p:
                return - 1
            left_p = middle_p + 1

# 着手する方法で難しさって変わるんだな、ループだと添え字番号とかは簡単だったけど、右が左寄り大きくなるエラーとかが出てきた。
