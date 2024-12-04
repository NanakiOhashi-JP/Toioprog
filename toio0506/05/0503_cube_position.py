# 0503_cube_position.py: キューブの位置検出
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
    with SimpleCube(name="ABC") as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        while LOOP:
            position = cube.get_current_position() # 現在位置取得
            grid = cube.get_grid() # 現在のマス目取得
            orientation = cube.get_orientation() # 方向取得
            if position is not None and grid is not None:
                print(f"x: {position[0]}, y:{position[1]}, cell_x: {grid[0]}, cell_y: {grid[1]}, orientation: {orientation}")
            else:
                print(f"position: {position}, grid: {grid}, orientation: {orientation}")
    print("Disconnected.")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())