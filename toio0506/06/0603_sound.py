# 0603_sound.py: 音を鳴らす
import sys # sys モジュール(sys.exit()使用に必要)
import signal # singnalモジュール
# toio.simple モジュールから SimpleCube を取り込み
from toio.simple import SimpleCube, Note # Note: 音程の名称

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
        melody = ((Note.C4, 0.5), (Note.D4, 0.5), (Note.E4, 0.5),
                  (Note.F4, 0.5), (Note.G4, 1.0)) # 音程と音長をタプルでまとめる
        for sound in melody:
            cube.play_sound(note=sound[0], duration=sound[1]+0.15,
                            wait_to_complete=False) # 発音後に待機しない
            cube.sleep(sound[1]) # 発音時間分，スリープ
        cube.sleep(0.5)
    print("Disconnected.")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())