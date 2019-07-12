import random
import pprint
import requests
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"

# 1. 요청
# jsom -> 
# 파이썬의 dictionary와 list로 변환하여 조작할 수 있다.
# 응답 (HTML, XML, JSON)
response = requests.get(url).json()
pprint.pprint(response)
print(type(response))

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
for i in range(100000):
    my_lotto = random.sample(range(1,46),6)
    n=0
    count = 0
   # print(f'내 번호 : {my_lotto}')
    for n in range(6):
        n += 1
        if response[f'drwtNo{n}'] in my_lotto:
            count += 1
    
    if count == 6:
        print('1등 당첨입니다.')
        c1 += 1
    elif count == 5:
        if response['bnusNo'] in my_lotto:
           print('2등 당첨입니다.')
           c2 += 1
        else:
            print('3등 당첨입니다.')
            c3 += 1
    elif count == 4:
        print('4등 당첨입니다.')
        c4 += 1
    elif count == 3:
        print('5등 당첨입니다.')
        c5 += 1
    else:
        print('낙첨입니다.')
        c6 += 1
    
print(f'1등 {c1}번, 2등 {c2}번, 3등 {c3}번, 4등 {c4}번, 5등 {c5}번, 낙첨 {c6}번', end='\r')
print('끝')

### 풀이
# 당첨번호 6개 + 보너스 번호
# win_lotto = []
# bonus = response['bnusNo']
# for i in range(1, 7):
#     win_lotto.append(response[f'drwtNo{i}'])

# result = [0, 0, 0, 0, 0]
# for i in range(10000000):
#     # 내가 뽑은 로또 번호
#     my_lotto = random.sample(range(1, 46), 6)

#     # 몇개 맞았는지 확인
#     # matched = 0
#     # for num in my_lotto:
#     #     if num in win_lotto:
#     #         matched += 1
#     matched = len(set(win_lotto) & set(my_lotto))

#     # 몇개 맞았는지를 바탕으로 출력
#     if matched == 6:
#         result[0] += 1
#     elif matched == 5 and bonus in my_lotto:
#         result[1] += 1
#     elif matched == 5:
#         result[2] += 1
#     elif matched == 4:
#         result[3] += 1
#     elif matched == 3:
#         result[4] += 1
#     print(result, end='\r')
# print('끝')
# print(result)