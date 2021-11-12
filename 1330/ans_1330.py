# 문제 - 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

def compare():
    num1,num2 = map(int,input().split(" ")) # int 및 split 방법
    
    if (num1 >= -10000) and (num2 <= 10000):
        if num1 > num2:
            print(">")
        elif num1 < num2:
            print("<")
        else:
            print("==")
    else:
        print("out of bound")


if __name__ == "__main__":
    compare()