import sys # sys モジュール(sys.exit()使用に必要)
# toio.simple モジュールから SimpleCube を取り込み
from toio.simple import SimpleCube

# (1) ここに追加モジュール，グローバル変数，関数などを定義

# メイン関数
def main():
    with SimpleCube() as cube: # キューブを探索，接続

    # (2) ここにキューブの接続，制御，切断の処理を記述

    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())