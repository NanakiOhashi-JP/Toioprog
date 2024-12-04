# 0601_cube_info.py: キューブの情報表示
import sys # sys モジュール(sys.exit()使用に必要)
import signal # singnalモジュール
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
def main():
    with SimpleCube(name="m78", log_level=NOTSET) as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        print("Battery Level: ", cube.get_battery_level()) # バッテリーレベル表示
        cube.sleep(1.0) 
        while LOOP:
            posture = cube.get_posture() # キューブの姿勢（上向きの面）検出
            roll, pitch, yaw = cube.get_3d_angle() # キューブの姿勢角（ロール，ピッチ，ヨー）検出
            button_state = cube.is_button_pressed() # ボタンの状態検出
            print(f"Posture: {posture}, 3D angle: {roll}, {pitch}, {yaw}, Button: {button_state}")
            cube.sleep(0.5)
    print("Disconnected.")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())