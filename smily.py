smily = "\U0001f600"

final = 10
for i in range(1,final):
	gap = int(final - i)
	content = ""
	if(gap > 0): 
		for o in range(gap):
			content += " "
	
	content += smily * i
	print(content)

# i = 0
# while i < 10:
# 	smilies = smily
# 	for j in range(0, i):
# 		smilies +=  smily
# 	print(smilies)
# 	i += 1