#문제의 핵심은 최소값으로 정렬한 배열의 원소의 index가 정답에 들어가면 된다.

input()                                 #갯수는 중요하지 않으므로 흘려준다
li = list(map(int,input().split()))    #두번째 입력에서 얻은 숫자를 list로 만든다
setli = list(set(li))                    #입력받은 list에서 중복을 제거한 뒤 정렬해준다
setli.sort()

result = {}
for i in range(len(setli)) :            #set된 list길이만큼 순회하면서 result[입력 배열의 값] = index
    result[setli[i]] = i                #로 result dict를 완성한다
for j in li :                            #입력받은 배열을 돌면서 해당 값을 키로 가지는 result의 값을 출력한다
    print(result[j],end=' ')