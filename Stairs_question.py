# 爬樓梯方法問題
# 計算排列組合套件
from scipy.special import comb


def ways_cal(stairs):
    # 方式總數 (預設為 1，最少有 1 種方法：每次走一階走完)
    ways = 1
    # 計算方法數量迴圈
    # i 從 1 到 stairs (i 代表走兩階的次數)
    for i in range(1, stairs + 1):
        # i == 1 時，代表走兩階 1 次，方法數等於 stairs - 1
        if i == 1:
            ways = ways + comb(stairs - 1, 1)
        # 從 i == 2 開始，只要 2*i 不大於 stairs，都不會超過總階數
        elif stairs - (2*i) > 0:
            # C 的 n 會等於總階數 - i (走兩階的次數)；m 等於 i (走兩階的次數)
            n = stairs - i
            ways = ways + comb(n, i)
        # 如 stairs == 2*i，代表從頭到尾只走兩階 (只有一種方法，ways + 1)
        elif stairs - (2*i) == 0:
            ways += 1
        # 代表 2*i 大於 stairs 的情況，此時走得階數超出總階梯數，無法成立，中止迴圈
        else:
            break

    # 將計算結果轉換為整數 (comb 用浮點數計算)
    ways = int(ways)

    return ways


if __name__ == '__main__':
    answer = ways_cal(41)
    print("共 {} 種不同的上樓方式".format(answer))
