#Library for natural language processing of Japanese
#©2019 Mamoru Itoi

import MeCab
import re

#形態素解析
def tokenizer(text):
	t = MeCab.Tagger("")
	t.parse("")
	m = t.parseToNode(text)
	tokens = []
	while m:
		tokenData = m.feature.split(",")
		token = [m.surface]
		for data in tokenData:
			token.append(data)
		tokens.append(token)
		m = m.next
	tokens.pop(0)
	tokens.pop(-1)
	for i , token in enumerate(tokens):
		if i != len(tokens) - 1:
			token[0] = token[0].replace(tokens[i + 1][0], "")
	for token in tokens:
		if token[2] == "数":
			token += ["*", "*"]
	return tokens

#文節分け
def phrasesSepaleter(text):
	#形態素解析
	tokens = tokenizer(text)
	#文節リスト
	phrases = []
	#一つの文節のトークンリスト
	phrase = []
	#特別処理中フラグ
	isSpecialAnalyzing = False
	#付属語登場フラグ
	didAttachedWordApper = None
	#自立語リスト
	independentParts = ["名詞", "動詞", "形容詞", "副詞", "連体詞", "感動詞", "接続詞", "接頭詞"]
	#トークンごとの処理
	for i, token in enumerate(tokens):
		#見出し
		surface = token[0]
		#品詞
		part = token[1]
		#品詞細分類1
		typeOfPart = token[2]
		#もしpartが自立語で、はじめの文節でなく、didAttachedWordApperがTrueならば
		if part in independentParts and i != 0:
			isSpecialAnalyzing = False
			if i + 1 != len(tokens) and part == "名詞" and didAttachedWordApper == None:
				didAttachedWordApper = False
			if phrase != []:
				didAttachedWordApper = None
				phrases.append(phrase)
			phrase = []
		#もしpartが付属語なら
		else:
			didAttachedWordApper = True
		#もしtokenが漢語サ変動詞なら
		if i != 0 and token[5] == "サ変・スル" or typeOfPart == ("非自立" or "接尾") or tokens[i - 1][1] == "接頭詞" or didAttachedWordApper == False:
			isSpecialAnalyzing = True
		if isSpecialAnalyzing:
			phrases[-1].append(token)
		else:
			phrase.append(token)
	if phrase != []:
		phrases.append(phrase)
	for phrase in phrases:
		print(phrase)

#活用がある単語を入力すると、その単語の活用を返す
def inflections(word):
	#形態素解析
	tokens = tokenizer(word)
	#抜き出し
	token = tokens[0]
	#見出し
	surface = token[0]
	#品詞
	part = token[1]
	#品詞細分類1
	typeOfPart = token[2]
	#活用型
	utilization = token[5]
	#基本形
	normal = token[7]
	#読み
	read = token[8]
	#活用リスト
	inflectionsList = []
	#語幹を抽出
	#動詞
	if part == "動詞":
		#五段動詞
		if re.search("五段", utilization):
			#五段動詞・カ行
			if re.search("カ行", utilization):
				stem = normal.replace("く", "")
				#五段動詞・カ行イ音便
				if re.search("イ音便", utilization):
					inflectionsList = [[stem + "か", stem + "こ"], [stem + "き", stem + "い"], stem + "く", stem + "く", stem + "け", stem + "け"]
				#五段動詞・カ行促音便
				elif re.search("促音便", utilization):
					inflectionsList = [[stem + "か", stem + "こ"], [stem + "き", stem + "っ"], stem + "く", stem + "く", stem + "け", stem + "け"]
				#五段動詞・カ行ユク
				else:
					inflectionsList = [["ゆか", "ゆこ"], ["ゆき", ""], "ゆく", "ゆく", "ゆけ", "ゆけ"]
			#五段動詞・ガ行
			elif re.search("ガ行", utilization):
				stem = normal.replace("ぐ", "")
				inflectionsList = [[stem + "が", stem + "ご"], [stem + "ぎ", stem + "い"], stem + "ぐ", stem + "ぐ", stem + "げ", stem + "げ"]
			#五段動詞・サ行
			elif re.search("サ行", utilization):
				stem = normal.replace("す", "")
				inflectionsList = [[stem + "さ", stem + "そ"], [stem + "し", stem + "し"], stem + "す", stem + "す", stem + "せ", stem + "せ"]
			#五段動詞・タ行
			elif re.search("タ行", utilization):
				stem = normal.replace("つ", "")
				inflectionsList = [[stem + "た", stem + "と"], [stem + "ち", stem + "っ"], stem + "つ", stem + "つ", stem + "て", stem + "て"]
			#五段動詞・ナ行
			elif re.search("ナ行", utilization):
				stem = normal.replace("ぬ", "")
				inflectionsList = [[stem + "な", stem + "の"], [stem + "に", stem + "ん"], stem + "ぬ", stem + "ぬ", stem + "ね", stem + "ね"]
			#五段動詞・バ行
			elif re.search("バ行", utilization):
				stem = normal.replace("ぶ", "")
				inflectionsList = [[stem + "ば", stem + "ぼ"], [stem + "び", stem + "ん"], stem + "ぶ", stem + "ぶ", stem + "べ", stem + "べ"]
			#五段動詞・マ行
			elif re.search("マ行", utilization):
				stem = normal.replace("む", "")
				inflectionsList = [[stem + "ま", stem + "も"], [stem + "み", stem + "ん"], stem + "む", stem + "む", stem + "め", stem + "め"]
			#五段動詞・ラ行
			elif re.search("ラ行", utilization):
				stem = normal.replace("る", "")
				#五段動詞・ラ行特殊
				if re.search("特殊", utilization):
					inflectionsList = [[stem + "ら", stem + "ろ"], [stem + "い", stem + "っ"], stem + "る", stem + "る", stem + "れ", stem + "い"]
				#五段動詞・ラ行
				else:
					inflectionsList = [[stem + "ら", stem + "ろ"], [stem + "り", stem + "っ"], stem + "る", stem + "る", stem + "れ", stem + "れ"]
			#五段動詞・ワ行
			elif re.search("ワ行", utilization):
				stem = normal.replace("う", "")
				inflectionsList = [[stem + "わ", stem + "お"], [stem + "い", stem + "っ"], stem + "う", stem + "う", stem + "え", stem + "え"]
		#一段動詞
		elif utilization == "一段":
			#一段動詞・2モーラ
			if len(read) == 2:
				stem = normal[0]
			#一段動詞・3モーラ
			else:
				stem = normal .replace("る", "")
			inflectionsList = [stem, stem, stem + "る", stem + "る", stem + "れ", stem + "ろ"]
		#カ変動詞
		elif re.search("カ変", utilization):
			if normal == "来る":
				inflectionsList = ["来", "来", "来る", "来る", "来れ", "来い"]
			elif normal == "くる":
				inflectionsList = ["こ", "き", "くる", "くる", "くれ", "こい"]
			#カタカナで送信するようなやつは知らん
		#サ変動詞
		elif re.search("サ変", utilization):
			#サ変動詞・スル
			if normal == "する":
				inflectionsList = [["し", "せ", "さ"], "し", "する", "する", "すれ", ["しろ", "せよ"]]
			#サ変動詞・-スル
			elif re.search("スル", read):
				stem = normal.replace("する", "")
				inflectionsList = [[stem + "し", stem + "せ", stem + "せ"], stem + "し", stem + "する", stem + "する", stem + "すれ", stem + "しろ"]
			#サ変動詞・-ズル
			elif re.search("ズル", read):
				stem = normal.replace("ずる", "")
				inflectionsList = [[stem + "じ", stem + "ぜ", stem + "ぜ"], stem + "じ", stem + "ずる", stem + "ずる", stem + "ずれ", stem + "じろ"]
	#形容詞
	elif part == "形容詞":
		stem = normal.replace("い", "")
		inflectionsList = [stem + "かろ", [stem + "く", stem + "かっ"], stem + "い", stem + "い", stem + "けれ", ""]
	return inflectionsList

#助動詞をつける
def auxiliaryVerb(word, mode):
	#形態素解析
	tokens = tokenizer(word)
	#抜き出し
	token = tokens[0]
	#見出し
	surface = token[0]
	#品詞
	part = token[1]
	#品詞細分類1
	typeOfPart = token[2]
	#活用型
	utilization = token[5]
	#基本形
	normal = token[7]
	#読み
	read = token[8]
	#活用を取得
	inflectionsList = inflections(word)
	#助動詞
	auxiliaryVerb = ""
	#使役
	if mode == "causatire":
		if re.search("五段", utilization):
			auxiliaryVerb = inflectionsList[0][0] + "せる"
		elif re.search("一段|カ変", utilization):
			auxiliaryVerb = inflectionslist[0] + "させる"
		elif re.search("サ変", utilization):
			auxiliaryVerb = inflectionsList[0][2] + "せる"
	#受け身・自発・尊敬
	elif mode == "passive":
		if re.search("五段", utilization):
			auxiliaryVerb = inflectionsList[0][0] + "れる"
		elif re.search("一段|カ変", utilization):
			auxiliaryVerb = inflections[0] + "られる"
		elif re.search("サ変", utilization):
			auxiliaryVerb = inflectionsList[0][2] + "れる"
	#打ち消し
	elif mode == "cancellation":
		if re.search("五段", utilization):
			auxiliaryVerb = inflectionsList[0][0] + "ない"
		elif re.search("一段|カ変", utilization):
			auxiliaryVerb = inflectionsList[0] + "ない"
		elif re.search("サ変", utilization):	
			auxiliaryVerb = inflectionsList[0][0] + "ない"
	#希望
	elif mode == "hope":
		if re.search("五段", utilization):
			auxiliaryVerb = inflectionsList[1][0] + "たい"
		if re.search("一段|カ変|サ変", utilization):
			auxiliaryVerb = inflectionsList[1] + "たい"
	#推定
	elif mode == "estimate":
		auxiliaryVerb = inflectionsList[2] + "らしい"
	#断定
	elif mode == "assertion":
		pass
	#伝聞
	elif mode == "hearsay":
		auxiliaryVerb = inflectionsList[2] + "そうだ"
	#様態
	elif mode == "condition":
		if re.search("五段", utilization):
			auxiliaryVerb = inflectionsList[1][0] + "そうだ"
		if re.search("一段|カ変|サ変", utilization):
			auxiliaryVerb = inflectionsList[1] + "そうだ"
	#比況
	elif mode == "proportion":
		auxiliaryVerb = inflectionsList[3] + "ようだ"
	#過去
	elif mode == "past":
		if re.search("五段", utilization):
			if re.search("ガ|ナ|バ|マ", utilization):
				auxiliaryVerb = inflectionsList[1][1] + "だ"
			else:
				auxiliaryVerb = inflectionsList[1][1] + "た"
		if re.search("一段|カ変|サ変", utilization):
			auxiliaryVerb = inflectionsList[1] + "た"
	#丁寧な断定
	elif mode == "politeAssertion":
		pass
	#丁寧
	elif mode == "polite":
		if re.search("五段", utilization):
			auxiliaryVerb = inflectionsList[1][0] + "ます"
		if re.search("一段|カ変|サ変", utilization):
			auxiliaryVerb = inflectionsList[1] + "ます"
	#意志・勧誘
	elif mode == "solicitation":
		if re.search("五段", utilization):
			auxiliaryVerb = inflectionsList[0][1] + "う"
		if re.search("一段|カ変", utilization):
			auxiliaryVerb = inflectionsList[0] + "よう"
		if re.search("サ変", utilization):
			auxiliaryVerb = inflectionsList[0][0] + "よう"
	return auxiliaryVerb
