from IPython import embed
#   今回は配列の総数を１と見なして、回数を重ねるごとに分母を二倍していく。


def chop(search_number, array):
    # 配列の総数を検索。2^nのnを判別する。
    n = 0
    array_count = len(array)
    if array_count == 0:
        return -1
    while array_count != 0:
        array_count = int(array_count/2)
        n += 1
    # n の回数分検索する

    # @point 現在指している配列の場所 [0 ~ 1]
    # @flg 次右左どちらに進むのかを決める 右にいく時true
    point = 0.0
    flg = True
    for now_n in range(n):
        # 1/2**now_nを取得
        flo = float(1/(2 ** (now_n + 1)))
        if flg:
            point += flo
        else:
            point -= flo
        number = decide_number(point, array)
        if array[number] == search_number:
            return number
        elif array[number] < search_number:
            flg = True
        else:
            flg = False
    return -1


# [0~1]の範囲の引数を渡せば現在の配列でマッチしている範囲の場所を渡してくれる関数
def decide_number(flo, array):
    count = 0
    for in_array in array:
        count += 1
        if float(count/len(array)) >= flo:
            return count - 1

# 今までで一番うまくいった。やばそうな箇所が初めからわかっていたので(decide_number)そこを切り出してエラーが出ても対策可能な状態にした。
