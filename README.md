# README of nlp
## 概要
本ソフトは、日本語の自然言語処理用のライブラリです。
## 構成
### tokenizer(text)
textを形態素解析します。  「ぼんやりとした花曇りの白い空。百人が乗った車輛、千人を運ぶ列車、その千本が流れる街。」

```python3:
[
["", "BOS/EOS", "*", "*", "*", "*", "*", "*", "*", "*"], 
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
["", "BOS/EOS", "*", "*", "*", "*", "*", "*", "*", "*"]
]
```
### dependencyAnalyzer(text)
textを係り受け解析します。  「新しいご馳走の発見は、新しい星の発見よりも人々を幸せにする。」

```python3:
[
["新しい", "ご馳走の"], 
["ご馳走の", "発見は、"], 
["発見は、", "幸せにする。"], 
["新しい", "星の"], 
["星の", "発見よりも"], 
["発見よりも", "幸せにする。"], 
["人々を", "幸せにする。"]
]
```
### inflections(word)
wordの活用を取得します。動詞と形容詞に対応しています。  「輝く」

```python3:
[["輝か", "輝こ"], ["輝き", "輝い"], "輝く", "輝く", "輝け", "輝け"]
```
### auxiliaryVerb(word, mode)
wordの助動詞活用を取得します。  「輝く」 mode="hope"

```python3:
"輝きたい"
```
