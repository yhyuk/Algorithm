# 문자열 입력 받은 후 가장 많이 사용된 알파벳?
# 가장 많이 사용된 알파벳 개수가 1개를 넘거나 아닌경우 '?' 출력

# n = input().upper() #문자열 입력, 대소문자 구분 X
# ans = list(set(n)) #중복요소 제거

# cnt_list = []
# for i in ans:
#     cnt = n.count(i)
#     cnt_list.append(cnt)
# if cnt_list.count(max(cnt_list)) > 1:
#     print('?')
# else :
#     max_index = cnt_list.index(max(cnt_list))
#     print(ans[max_index]) 
# word = input().upper()
# word_list = list(set(word))
# word_count = []

# for i in word_list:
#     count = word.count(i)
#     word_count.append(count)
# if(word_count.count(max(word_count))>=2): print("?")
# else: 
#     print(word_list[word_count.index(max(word_count))])

# c = ord(input())
# t = ord('a')
# while t<=c :
#   print(chr(t), end=' ')
#   t += 1