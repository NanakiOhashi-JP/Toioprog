# 0505_move_key.py: キー検出によるキューブ移動
import sys # sys モジュール(sys.exit()使用に必要)
import signal # singnalモジュール
import keyboard # keyboardモジュール
from logging import * # logging モジュール（ログ表示に必要）
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
def main ():
    global LOOP # main() 内でグローバル変数 LOOP に代入
    with SimpleCube(name="m78", log_level=NOTSET) as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        print("push cursor key:")
        while LOOP:
            if keyboard.is_pressed("up"): # 矢印キーの入力検出
                print("up")
                lsp = rsp = 30 # 左右のモーター速度
            elif keyboard.is_pressed("down"):
                print("down")
                lsp = rsp = -30
            elif keyboard.is_pressed("left"):
                print("left")
                lsp = -15; rsp = 15
            elif keyboard.is_pressed("right"):
                print("right")
                lsp = 15; rsp = -15
            elif keyboard.is_pressed("q"):
                print("quit")
                LOOP = False
            else:
                lsp  = rsp = 0
            cube.run_motor(left_speed=lsp, right_speed=rsp, duration=0)
            cube.sleep(0.1)
    print("Disconnected.")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())