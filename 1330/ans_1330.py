# ���� - �� ���� A�� B�� �־����� ��, A�� B�� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

def compare():
    num1,num2 = map(int,input().split(" ")) # int �� split ���
    
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