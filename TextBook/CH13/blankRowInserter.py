import sys
from openpyxl import load_workbook

def insert_blank_row(file_name, n, m):
    # Excelファイルを読み込み
    wb = load_workbook(filename=file_name)
    ws = wb.active

    # M行目から空行をN行挿入
    for _ in range(n):
        ws.insert_rows(m)

    # ファイルを保存
    wb.save(file_name)
    print(f"{file_name} に {n} 行の空行を {m} 行目から挿入しました。")

if __name__ == "__main__":
    # コマンドライン引数のチェック
    if len(sys.argv) != 4:
        print("使い方: python blankRowInserter.py <N> <M> <file_name>")
        sys.exit(1)
    
    # コマンドライン引数を取得
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        file_name = sys.argv[3]
    except ValueError:
        print("NとMは整数でなければなりません。")
        sys.exit(1)
    
    # 空行の挿入
    insert_blank_row(file_name, n, m)
