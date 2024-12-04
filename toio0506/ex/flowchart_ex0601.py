# ライブラリの読み込み
from pyflowchart import Flowchart

# フローチャートを作成するPythonプログラムを指定する
with open('ex0602.py', encoding='utf-8') as f:  # UTF-8で読み込む
    code = f.read()

# フローチャート作成時のオプションを指定する
fc = Flowchart.from_code(code, field='', inner=False, simplify=False)

# 作成したフローチャートを保存する
with open('ex0602.md', mode='w', encoding='utf-8') as f:  # UTF-8で保存する
    f.write('```flow\n')        # flowchart.jsの始まり
    f.write(fc.flowchart())     # フローチャートの中身
    f.write('```')              # flowchart.jsの終わり

print("フローチャートをex0602.mdに保存しました")
