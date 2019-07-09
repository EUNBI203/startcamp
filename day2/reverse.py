# number.txt를 읽어서
# 리스트 (readlines)
with open('number.txt','r') as f:
    numbers = f.readlines()
print(numbers)

# 리스트를 뒤집는다.
numbers.reverse()

# number_reverse.txt로 저장!
with open('number_reverse.txt','w') as f:
    for number in numbers:
        f.write(number)
