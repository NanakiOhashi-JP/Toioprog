import sys # sys モジュール(sys.exit()使用に必要)
# toio.simple モジュールから SimpleCube, Direction を取り込み
from toio.simple import SimpleCube, Direction

# メイン関数
def main():
    with SimpleCube("m78") as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        for i in range(4):
            cube.move_steps(Direction.Forward, 30, 50)
            cube.turn(15, 90)
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())