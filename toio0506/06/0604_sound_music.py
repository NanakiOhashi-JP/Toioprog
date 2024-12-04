# 0604_sound_music.py: 音を鳴らす（テンポと音符使用の例）
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

tempo4 = 120 # テンポ（1分あたりの4分音符の数）

# メイン関数
def main():
    with SimpleCube(name="ABC") as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        print("Battery Level: ", cube.get_battery_level()) # バッテリーレベル表示
        cube.sleep(1.0)
        melody = ((Note.C4, 4), (Note.D4, 4), (Note.E4, 4),
                  (Note.F4, 4), (Note.G4, 2)) # 音程と音符をタプルでまとめる
        for sound in melody:
            note_length =   60 * 4 / (tempo4 * sound[1]) # 音長
            print(sound[0], note_length)
            cube.play_sound(note=sound[0], duration=note_length*1.3,
                            wait_to_complete=False) # 発音後に待機しない
            cube.sleep(note_length) # 発音時間分，スリープ
        cube.sleep(0.5)
    print("Disconnected.")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())