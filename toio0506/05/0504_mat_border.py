# 0504_mat_border.py: マットのボーダー位置検出
import sys # sys モジュール(sys.exit()使用に必要)
import signal # singnalモジュール
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
    global LOOP # main() 内でグローバル変数 LOOP に代入
    with SimpleCube(name="m78") as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        cube.set_orientation(speed=15, degree=0) # 上向き
        cube.move(speed=-15, duration=0) # 後退（動き続ける）
        while LOOP:
            position = cube.get_current_position() # 現在位置取得
            grid = cube.get_grid() # 現在のマス目取得
            orientation = cube.get_orientation() # 方向取得
            print(f"position: {position}, grid: {grid}, orientation: {orientation}")
            if position is None: # マットから飛び出したとき
                cube.stop_motor()
                cube.move(speed=15, duration=0.5) # マット内に戻る
                cube.spin(speed=15, duration=2.0) # 約1回転
                position = cube.get_current_position() # 現在位置取得
                print(f"position: {position}") # 位置表示（ボーダー付近）
                LOOP = False
    print("Disconnected.")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())