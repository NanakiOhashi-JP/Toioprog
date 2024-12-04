import sys # sys モジュール(sys.exit()使用に必要)
# toio.simple モジュールから SimpleCube を取り込み
from toio.simple import SimpleCube

# メイン関数
def main():
    with SimpleCube("m78") as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        cube.move_to_the_grid_cell(30, -1, -1)
        cube.set_orientation(15, 0)
        cube.move_to_the_grid_cell(30, -1, 1)
        cube.set_orientation(15, 90)
        cube.move_to_the_grid_cell(30, 1, 1)
        cube.set_orientation(15, 180)
        cube.move_to_the_grid_cell(30, 1, -1)
        cube.set_orientation(15, 270)
        cube.move_to_the_grid_cell(30, -1, -1)
        cube.set_orientation(15, 0)
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())