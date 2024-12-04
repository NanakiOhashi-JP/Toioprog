# 0602_lamp_color.py: ランプの色変更と点灯，消灯
import sys # sys モジュール(sys.exit()使用に必要)
import signal # singnalモジュール
import random # 乱数モジュール
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
    with SimpleCube(name="m78") as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        print("Battery Level: ", cube.get_battery_level()) # バッテリーレベル表示
        cube.sleep(1.0) 
        while LOOP:
            red = random.randint(0, 255) # 0-255 の範囲の乱数
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            cube.turn_on_cube_lamp(r=red, b=blue, g=green, duration=0.5) # 0.5秒点灯
            print(f"Lamp color (R,G,B) = ({red}, {green}, {blue})")
            cube.turn_off_cube_lamp()
            cube.sleep(0.5)
    print("Disconnected.")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())