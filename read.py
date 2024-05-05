data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')


# 算留言平均長度

# 老師寫法

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))

# 我的寫法

# a = 0
# a = int(a)
# c = []
# while True:
# 	if a < len(data):
# 		c.append(len(data[a]))
# 		a += 1
# 	else:
# 		break
# print('留言的平均長度為', sum(c)/len(data)) 

# 清單篩選

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')


# list comprehension (清單快寫法)

# good = [d for d in data if 'good' in d]
# print(good)
# bad = ['bad' in d for d in data]
# print(bad)

# 清單   = [   運算          變數        清單         篩選條件     ] 
# output = [(number-1) for number in reference if number % 2 == 0]


# 文字計數

wc = {} # word_count 的字典
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典

for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

while True:
	word = input("請輸入一個單字：")
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔')
print('感謝使用本查詢功能')