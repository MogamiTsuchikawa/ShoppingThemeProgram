# テストケースの生成方法及びテスターの使用法

## 要約
- 入力は1000行
- 最初はadd,最後二つはcheckout->exit
- add,show,checkoutがそれぞれおおよそ1割、buyがおおよそ7割
- show,checkoutはそれぞれで連続はしない(show->checkout及びその逆はありうる)
- 入出力に使用される文字は英数字のみ
- テストケース生成してからテスターを使用すること
- 出力の行頭が#の時はコメントとして無視する
- 出力の形式は以下に記載

## 出力の形式
出力が必要な命令はshowとcheckoutのみである。
行頭に#を入れるとデバッグ用のメッセージとして扱われその行は無視される。
### show
```
形式:
{id}:{name} {value}yen

例:
0:apple 500yen
1:banana 300yen
2:cucumber 200yen
:
:
```

- id: addされた順番(0から)
- name: 商品の名前
- value: 価格

nameとvalueの間にスペースを入れ、商品ごとに改行するのを忘れずに。

### checkout
```
形式:
{id}:{name} {value}yen*{count}
:
:
total:{total}yen

例:
0:apple 500yen*0
1:banana 300yen*1
2:cucumber 200yen*2
:
:
total:123456yen
```

- id: addされた順番(0から)
- name: 商品の名前
- value: 価格
- total: 合計金額

showに加え、各商品の現在購入している数を出力していき、最後にその合計金額を出力する。


## コマンドの種類と生成方法
- add
- buy
- show
- checkout

1から10の乱数を生成し、1の場合add,2の場合show,3の場合checkout,4以上の場合buyを生成する。
ただし、show,checkoutについては前の行と同じ場合それ以外が選択されるまで再抽選される。同様に998行目でcheckoutが選択された際も再抽選される。
また1行目は必ずaddが生成される。