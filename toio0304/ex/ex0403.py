import sys  # sys モジュール(sys.exit()使用に必要)
# toio.simple モジュールから SimpleCube を取り込み
from toio.simple import SimpleCube

# メイン関数
def main():
    with SimpleCube("m78") as cube:  # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name())  # キューブ名表示

        # 正三角形の各頂点の座標を指定
        cube.move_to(30, -43, -25)      # 頂点1
        cube.set_orientation(15, 30)  # 向きを設定

        cube.move_to(30, 0, 50)  # 頂点2
        cube.set_orientation(15, 120)

        cube.move_to(30, 43, -25)   # 頂点3
        cube.set_orientation(15, 270)

        cube.move_to(30, -50, 50)      # 頂点1

    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())
