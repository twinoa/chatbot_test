# ������Ÿ�� �Ÿ� ���ϱ�
def calc_distance(a, b):
    ''' ������Ÿ�� �Ÿ� ����ϱ� '''
    if a == b: return 0 # ������ 0�� ��ȯ
    a_len = len(a) # a ����
    b_len = len(b) # b ����
    if a == "": return b_len
    if b == "": return a_len
    # 2���� ǥ (a_len+1, b_len+1) �غ��ϱ� --- (��1)
    # matrix �ʱ�ȭ�� �� : [[0, 1, 2, 3], [1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [3, 0, 0, 0, 0], [4, 0, 0, 0, 0]]
    # [0, 1, 2, 3]
    # [1, 0, 0, 0]
    # [2, 0, 0, 0]
    # [3, 0, 0, 0] 
    matrix = [[] for i in range(a_len+1)] # ����Ʈ ����������� ����Ͽ� 1���� �ʱ�ȭ
    for i in range(a_len+1): # 0���� �ʱ�ȭ
        matrix[i] = [0 for j in range(b_len+1)]  # ����Ʈ ����������� ����Ͽ� 2���� �ʱ�ȭ
    # 0�� �� �ʱ갪�� ����
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[0][j] = j
    # ǥ ä��� --- (��2)
    # print(matrix,'----------')
    for i in range(1, a_len+1):
        ac = a[i-1]
        # print(ac,'=============')
        for j in range(1, b_len+1):
            bc = b[j-1] 
            # print(bc)
            cost = 0 if (ac == bc) else 1  #  ���̽� ���� ǥ���� ��:) result = value1 if condition else value2
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     # ���� ����: ���ʿ��� +1
                matrix[i][j-1] + 1,     # ���� ����: ���� ������ +1   
                matrix[i-1][j-1] + cost # ���� ����: �밢������ +1, ���ڰ� �����ϸ� �밢�� ���� ����
            ])
            # print(matrix)
        # print(matrix,'----------��')
    return matrix[a_len][b_len]
# "�󸶳� �м��� �ɱ��"�� "���絵�� �м� �ұ��"�� �Ÿ� --- (��3)
print(calc_distance("�󸶳� �м��� �ɱ��","���絵�� �м� �ұ��"))
# ���� ��
samples = ["���̿�","��õ��","��õ��","�Ź�","���"]
base = samples[0]
r = sorted(samples, key = lambda n: calc_distance(base, n))  # samples ����Ʈ�� �� ��ҿ� ���� calc_distance(base, n) �Լ��� ȣ���Ͽ� ������Ÿ�� �Ÿ��� ����ϰ�, �̸� �������� ����Ʈ�� ����
for n in r:
    print(calc_distance(base, n), n)