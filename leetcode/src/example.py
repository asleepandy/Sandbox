# -*- coding: utf-8 -*-


def example1(n):
    """寫一個函數計算當參數為 n(n很大) 時的值 1-2+3-4+5-6+7……+n"""
    result = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            result -= i
        else:
            result += i

    print result


def example2(m, n):
    """ 寫一個函數實作輾轉相除法(輸入兩整數求最大公因數 """
    while m % n != 0:
        t = n
        n = m % n
        m = t
    print n
