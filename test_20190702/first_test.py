# -*- coding:utf-8 -*-
import regex as re
"""
# 概要
ユーザーによって string と sub_stringが入力されます
sub_string が stringの中で何回発生しているかを出力してください

- 注意: 文字はケースセンシティブです
- 入力フォーマット: 最初が string。 次に来るのが sub_stringとなります
- 文字の長さ: 1 <= len(string) <= 200、1<= len(sub_string) <= 200、 len(string) > len(sub_string)
- 出力: int

# 例

## インプット
ABCDCDC
CDC

## アウトプット
2

## 解説
ABCDCDCに対してCDCが2回登場するため、出力は2となる。
"""


def count_substring(string, sub_string):
    # ここに書いてください
    return len(re.findall(sub_string, string, overlapped=True))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
