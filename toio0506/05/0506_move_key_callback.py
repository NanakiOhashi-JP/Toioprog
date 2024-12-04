# 0506_move_key_callback.py: キー検出によるキューブ移動（コールバック関数使用）
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

lsp = rsp = 0 # 左右のモーター速度（グローバル変数）

# キー検知コールバック関数
def key_motor(key):
    global lsp, rsp, LOOP
    if key.event_type == keyboard.KEY_DOWN:
        print("press: ", key.name)
        if key.name == "up": # カーソルキーの入力検出
            lsp = rsp = 30
        elif key.name =="down":
            lsp = rsp = -30
        elif key.name == "left":
            lsp = -15; rsp = 15
        elif key.name == "right":
            lsp = 15; rsp = -15
        elif key.name == "q":
            print("quit")
            LOOP = False
        else:
            lsp = rsp = 0
    else:
        print("release: ", key.name)
        lsp = rsp = 0

keyboard.hook(callback = key_motor) # キー検知コールバック関数の登録

# メイン関数
def main ():
    with SimpleCube(name="m78", log_level=NOTSET) as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        print("push cursor key:")
        while LOOP:
            cube.run_motor(left_speed = lsp, right_speed = rsp, duration = 0)
            cube.sleep(0.1)
    print("Disconnected.")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())