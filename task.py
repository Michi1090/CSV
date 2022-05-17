# ライブラリのインポート
import csv

# 元データの読み込み
with open('sample.csv', 'r', newline='', encoding='cp932') as file:
    reader = csv.reader(file)
    result = []

    # CSVから1行ずつデータを取得
    for row in reader:
        # 見出し行の抽出
        if reader.line_num == 1:
            result.append(row)
        # 大阪府のデータを抽出
        elif row[1] == '大阪府':
            result.append(row)

# 新規CSVファイルの作成
with open('result.csv', 'w', newline='', encoding='cp932') as file:
    writer = csv.writer(file)
    writer.writerows(result)
