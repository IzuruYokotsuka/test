# -*- coding:utf-8 -*-
import math
"""
# 概要
ユーザーによって n が入力されます
n が素数かどうかの判定器を作ってください。

注意: 数値のみが入力されます。
出力フォーマット: bool値を返してください
数値の長さ: 1 <= n <= 10000000

# 例：
## 例1
- インプット: 100
- アウトプット: False

## 例2
- インプット: 13
- アウトプット: True

## 解説
100は素数ではない。
13は素数。
"""


def is_prime_number(n):
    # ここに書いてください
    if n < 2:
        return False
    if n == 2:
        return True
    for p in range(2, math.floor(math.sqrt(n))):
        if n % p == 0:
            return False
    return True


if __name__ == '__main__':
    n = input().strip()
    print(is_prime_number(int(n)))
