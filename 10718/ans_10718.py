# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


def solve():
    n = 2
    for i in range(n):
        print("����ģ�� ��������")
    return 0

if __name__ == "__main__":
    solve()