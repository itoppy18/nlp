# README of nlp
## 概要
本ソフトは、日本語の自然言語処理用のライブラリです。
## 構成
### tokenizer(text)
textを形態素解析します。  

```python3:
#例:「ぼんやりとした花曇りの白い空。百人が乗った車輌、千人を運ぶ列車、その千本が流れる街。」

[
["ぼんやり", "名詞", "サ変接続", "*", "*", "*", "*", "ぼんやり", "ボンヤリ", "ボンヤリ"], 
["と", "助詞", "格助詞", "一般", "*", "*", "*", "と", "ト", "ト"], 
["し", "動詞", "自立", "*", "*", "サ変・スル", "連用形", "する", "シ", "シ"], 
["た", "助動詞", "*", "*", "*", "特殊・タ", "基本形", "た", "タ", "タ"], 
["花曇り", "名詞", "一般", "*", "*", "*", "*", "花曇り", "ハナグモリ", "ハナグモリ"], 
["の", "助詞", "格助詞", "一般", "*", "*", "*", "の", "ノ", "ノ"], 
["白い", "形容詞", "自立", "*", "*", "形容詞・アウオ段", "基本形", "白い", "シロイ", "シロイ"], 
["空", "名詞", "一般", "*", "*", "*", "*", "空", "ソラ", "ソラ"], 
["。", "記号", "句点", "*", "*", "*", "*", "。", "。", "。"], 
["百", "名詞", "数", "*", "*", "*", "*", "百", "ヒャク", "ヒャク"], 
["人", "名詞", "接尾", "助数詞", "*", "*", "*", "人", "ニン", "ニン"], 
["が", "助詞", "格助詞", "一般", "*", "*", "*", "が", "ガ", "ガ"], 
["乗っ", "動詞", "自立", "*", "*", "五段・ラ行", "連用タ接続", "乗る", "ノッ", "ノッ"], 
["た", "助動詞", "*", "*", "*", "特殊・タ", "基本形", "た", "タ", "タ"], 
["車輛", "名詞", "一般", "*", "*", "*", "*", "車輛", "シャリョウ", "シャリョー"], 
["、", "記号", "読点", "*", "*", "*", "*", "、", "、", "、"], 
["千", "名詞", "数", "*", "*", "*", "*", "千", "セン", "セン"], 
["人", "名詞", "接尾", "助数詞", "*", "*", "*", "人", "ニン", "ニン"], 
["を", "助詞", "格助詞", "一般", "*", "*", "*", "を", "ヲ", "ヲ"], 
["運ぶ", "動詞", "自立", "*", "*", "五段・バ行", "基本形", "運ぶ", "ハコブ", "ハコブ"], 
["列車", "名詞", "一般", "*", "*", "*", "*", "列車", "レッシャ", "レッシャ"], 
["、", "記号", "読点", "*", "*", "*", "*", "、", "、", "、"], 
["その", "連体詞", "*", "*", "*", "*", "*", "その", "ソノ", "ソノ"], 
["千", "名詞", "数", "*", "*", "*", "*", "千", "セン", "セン"], 
["本", "名詞", "接尾", "助数詞", "*", "*", "*", "本", "ホン", "ホン"], 
["が", "助詞", "格助詞", "一般", "*", "*", "*", "が", "ガ", "ガ"], 
["流れる", "動詞", "自立", "*", "*", "一段", "基本形", "流れる", "ナガレル", "ナガレル"], 
["街", "名詞", "一般", "*", "*", "*", "*", "街", "マチ", "マチ"], 
["。", "記号", "句点", "*", "*", "*", "*", "。", "。", "。"], 
]
```
### phrasesSepaleter(text)
textを文節に分けます。  

```python3:
#例:「これは、僕と彼女だけが知っている、世界の秘密についての物語。」
[
[['これ', '名詞', '代名詞', '一般', '*', '*', '*', 'これ', 'コレ', 'コレ'], ['は', '助詞', '係助詞', '*', '*', '*', '*', 'は', 'ハ', 'ワ'], ['、', '記号', '読点', '*', '*', '*', '*', '、', '、', '、']]
[['僕', '名詞', '代名詞', '一般', '*', '*', '*', '僕', 'ボク', 'ボク'], ['と', '助詞', '格助詞', '一般', '*', '*', '*', 'と', 'ト', 'ト']]
[['彼女', '名詞', '代名詞', '一般', '*', '*', '*', '彼女', 'カノジョ', 'カノジョ'], ['だけ', '助詞', '副助詞', '*', '*', '*', '*', 'だけ', 'ダケ', 'ダケ'], ['が', '助詞', '格助詞', '一般', '*', '*', '*', 'が', 'ガ', 'ガ']]
[['知っ', '動詞', '自立', '*', '*', '五段・ラ行', '連用タ接続', '知る', 'シッ', 'シッ'], ['て', '助詞', '接続助詞', '*', '*', '*', '*', 'て', 'テ', 'テ'], ['いる', '動詞', '非自立', '*', '*', '一段', '基本形', 'いる', 'イル', 'イル'], ['、', '記号', '読点', '*', '*', '*', '*', '、', '、', '、']]
[['世界', '名詞', '一般', '*', '*', '*', '*', '世界', 'セカイ', 'セカイ'], ['の', '助詞', '連体化', '*', '*', '*', '*', 'の', 'ノ', 'ノ']]
[['秘密', '名詞', '一般', '*', '*', '*', '*', '秘密', 'ヒミツ', 'ヒミツ'], ['について', '助詞', '格助詞', '連語', '*', '*', '*', 'について', 'ニツイテ', 'ニツイテ'], ['の', '助詞', '連体化', '*', '*', '*', '*', 'の', 'ノ', 'ノ']]
[['物語', '名詞', '一般', '*', '*', '*', '*', '物語', 'モノガタリ', 'モノガタリ'], ['。', '記号', '句点', '*', '*', '*', '*', '。', '。', '。']]
]
```
### inflections(word)
wordの活用を取得します。動詞と形容詞に対応しています。 

```python3:
#例:「輝く」
[["輝か", "輝こ"], ["輝き", "輝い"], "輝く", "輝く", "輝け", "輝け"]
```
### auxiliaryVerb(word, mode)
wordの助動詞活用を取得します。

```python3:
#例:「輝く」の希望形
"輝きたい"
```
