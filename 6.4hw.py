dic = {
	"word1": "meaning1",
	"word4": "meaning2",
	"word3": "meaning5",
	"word2": "meaning4",
	"word5": "meaning3",
	}
for word, meaning in sorted(dic.items()):
	print(word +": " +meaning)