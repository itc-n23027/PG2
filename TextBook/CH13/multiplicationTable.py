
import sys
from openpyxl import Workbook

def create_multiplication_table(n):
    # Workbookオブジェクトの生成
    wb = Workbook()
    ws = wb.active
    ws.title = "Multiplication Table"

    # 掛け算表の作成
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ws.cell(row=i, column=j, value=i * j)

    # ファイルの保存
    filename = f"multiplication_table_{n}x{n}.xlsx"
    wb.save(filename)
    print(f"{filename} を作成しました。")

if __name__ == "__main__":
    # コマンドライン引数のチェック
    if len(sys.argv) != 2:
        print("使い方: python multiplicationTable.py <N>")
        sys.exit(1)
    
    # コマンドライン引数を整数に変換
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Nは整数でなければなりません。")
        sys.exit(1)
    
    # 掛け算表の作成
    create_multiplication_table(n)
