import sys  # sys モジュール(sys.exit()使用に必要)
import signal  # signalモジュール
from toio.simple import SimpleCube  # toio.simple モジュールから SimpleCube を取り込み

LOOP = True  # 繰り返し継続フラグ（グローバル変数）

# シグナル割り込みハンドラ（端末上で Ctrl-C を押すと繰り返し終了）
def ctrl_c_handler(_signum, _frame):
    global LOOP
    print("Ctrl-C")
    LOOP = False

signal.signal(signal.SIGINT, ctrl_c_handler)  # シグナルハンドラ設定

# 端っこの座標を取得する関数
def get_edge_position(cube, degree):
    global LOOP
    LOOP = True
    cube.set_orientation(speed=15, degree=degree)  # 指定した方向に設定
    cube.move(speed=-15, duration=0)  # 後退（動き続ける）
    while LOOP:
        position = cube.get_current_position()  # 現在位置取得
        if position is None:  # マットから飛び出したとき
            cube.stop_motor()
            cube.move(speed=15, duration=0.5)  # マット内に戻る
            position = cube.get_current_position()  # ボーダー付近の位置を再取得
            return position


def main():
    directions = ["下", "左", "上", "右"]
    degrees = [0, 90, 180, 270]
    edge_positions = []

    with SimpleCube(name="m78") as cube:  # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name())  # キューブ名表示
        for direction, degree in zip(directions, degrees):
            print(f"{direction}側を計測中...")
            position = get_edge_position(cube, degree)
            print(f"{direction}側の座標: {position}")
            edge_positions.append((direction, position))
    return 0


# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())
