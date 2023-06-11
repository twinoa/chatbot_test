import pandas as pd

class SimpleChatBot:

    # load_data 함수를 통해 questions, answers 항목들을 불러서 변수에 저장하는
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    # 지정된 csv 파일을 불러와 질문열, 답변열을 파이썬 리스트로 저장하여 리턴
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()  # 질문열만 뽑아 파이썬 리스트로 저장
        answers = data['A'].tolist()   # 답변열만 뽑아 파이썬 리스트로 저장
        return questions, answers

    # 레벤슈타인 거리를 이용해 최적의 답을 찾아내기
    def find_best_answer_lev(self, input_sentence):
        input_len = len(input_sentence) # 입력된 문장의 길이를 저장
        distances = [] # 유사도를 저장할 빈 배열 선언

        if input_len == 0 : return '입력을 해주세요!' # 입력된 문장이 없으면 입력해달라고 출력

        # questions 배열의 항목 한개씩 꺼내서 반복
        for i in self.questions : 

            # 입력 문자, 질문 길이만큼 배열 초기화
            matrix = [[] for j in range(input_len+1)] 
            for j in range(input_len+1): 
                matrix[j] = [0 for k in range(len(i)+1)] 

            # 0일때 초기값 설정
            for j in range(input_len+1):
                matrix[j][0] = j
            for k in range(len(i)+1):
                matrix[0][k] = k

            # 표 채우기
            for j in range(1, input_len+1):
                ac = input_sentence[j-1]

                for k in range(1, len(i)+1):
                    bc = i[k-1] 

                    cost = 0 if (ac == bc) else 1  
                    matrix[j][k] = min([
                        matrix[j-1][k] + 1,     # 문자 제거 : 위쪽에서 + 1
                        matrix[j][k-1] + 1,     # 문자 삽입 : 왼쪽에서 + 1 
                        matrix[j-1][k-1] + cost # 문자 변경 : 대각선에서 +1, 문자가 동일하면 대각선 숫자 복사
                    ])
            
            # 입력 문자와 질문 배열 사이의 레벤슈타인 거리 저장
            distances.append(matrix[input_len][len(i)])

        # 레벤슈타인 거리가 가장 짤은 질문의 인덱스를 저장하고 답변을 리턴
        best_match_index = distances.index(min(distances))
        return self.answers[best_match_index]
        

# CSV 파일 경로를 지정하세요.
filepath = 'ChatbotData.csv'

# 간단한 챗봇 인스턴스를 생성합니다.
chatbot = SimpleChatBot(filepath)

# '종료'라는 단어가 입력될 때까지 챗봇과의 대화를 반복합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_best_answer_lev(input_sentence)
    print('Chatbot:', response)
    
