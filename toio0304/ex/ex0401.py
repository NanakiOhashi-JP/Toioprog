import sys # sys モジュール(sys.exit()使用に必要)
# toio.simple モジュールから SimpleCube を取り込み
from toio.simple import SimpleCube

import matplotlib.pyplot as plt

# メイン関数
def main():
    with SimpleCube("m78") as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        
        n = 5  # 速度の種類数
        m = 3  # 各速度での計測回数
        speed = [24, 37, 59, 69, 77]
        length = [[] for _ in range(n)]
        avg_length = []

        # 各速度で複数回計測
        for i in range(n):
            print(f"Measuring for speed {speed[i]}...")
            for j in range(m):
                cube.move(speed[i], 1)
                cube.sleep(1)
                tmp = float(input(f"Length for speed {speed[i]} (Trial {j + 1}): "))
                length[i].append(tmp)

            avg = sum(length[i]) / m
            avg_length.append(avg)
            print(f"Average length for speed {speed[i]}: {avg}")


    # グラフを描画
    plt.figure(figsize=(8, 6))
    plt.plot(speed, avg_length, marker='o', linestyle='-', color='b', label='Speed vs Avg Length')
    plt.title('Speed vs Average Length')
    plt.xlabel('Speed')
    plt.ylabel('Average Length')
    plt.grid(True)
    plt.legend()
    plt.show()

    save_path = "speed_length.png"
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Graph saved as {save_path}")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())