# ���� ������ �Է¹޾� 90 ~ 100���� A, 80 ~ 89���� B, 70 ~ 79���� C, 
# 60 ~ 69���� D, ������ ������ F�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.

# �Է� -ù ° �ٿ� ���� ������ �־�����. 
# ���� ������ 0���� ũ�ų� ����, 100���� �۰ų� ���� �����̴�.

def report():
    # (1) �Է�
    score_report = int(input())

    # (2) ���� �Ǵ� �� ���
    if (score_report < 0) or (score_report > 100):
        print("not correct score")
    elif 90 <= score_report <= 100:
        print("A")
    elif 80 <= score_report < 90:
        print("B")
    elif 70 <= score_report < 80:
        print("C")
    elif 60 <= score_report < 70:
        print("D")
    else:
        print("F")
    
if __name__ == "__main__":
    report()