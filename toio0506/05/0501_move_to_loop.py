# 0501_move_to_loop.py: 目標地点への移動とログ表示
import sys # sys モジュール(sys.exit()使用に必要)
from logging import * # logging モジュール（ログ表示に必要）
# toio.simple モジュールから SimpleCube を取り込み
from toio.simple import SimpleCube

# メイン関数
def main():
    with SimpleCube(name="m78", log_level=INFO) as cube: # 指定のキューブを探索，接続，ログ表示
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        targets = [(-50, -50), (-50, 50), (50, 50), (50, -50)] # 目標座標（タプルに格納）
        for i, target in enumerate(targets):
            print(i, target)
            target_x, target_y = target # 目標座標のタプルを展開
            success = cube.move_to(speed=30, x=target_x, y=target_y)
            print(success)
            if success is False:
                print("Position ID missed.")
            cube.sleep(0.5)
            cube.set_orientation(speed=15, degree=(90 * i) % 360)
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())