# 0502_move_to_infty.py: 無限ループとシグナル割り込みハンドラ
import sys # sys モジュール(sys.exit()使用に必要)
import signal # singnalモジュール
from logging import INFO # logging モジュール（ログ表示に必要）
# toio.simple モジュールから SimpleCube を取り込み
from toio.simple import SimpleCube

LOOP = True # 繰り返し継続フラグ（グローバル変数）

# シグナル割り込みハンドラ（端末上で Ctrl-C を押すと繰り返し終了）
def ctrl_c_handler(_signum, _frame):
    global LOOP
    print("Ctrl-C")
    LOOP = False

signal.signal(signal.SIGINT, ctrl_c_handler) # Add signal handler

# メイン関数
def main():
    with SimpleCube(name="m78", log_level=INFO) as cube: # 指定のキューブを探索，接続，ログ表示
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        targets = ((-50, -50), (-50, 50), (50, 50), (50, -50)) # 目標座標（タプルに格納）
        while LOOP:
            for i, target in enumerate(targets):
                print(i, target)
                target_x, target_y = target # 目標座標のタプルを展開
                success = cube.move_to(speed=30, x=target_x, y=target_y)
                print(success)
                if not success:
                    print("move_to: Failed.")
                cube.sleep(0.5)
                success = cube.set_orientation(speed=15, degree=(90 * i) % 360)
                print(success)
                if not success:
                    print("orentation: Failed.")
    print("Disconnected.")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())