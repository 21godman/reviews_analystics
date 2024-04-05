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

# 老師寫法

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