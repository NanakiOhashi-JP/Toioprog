"""
 3. ボタンを押すか，キューブの向きを変えるか，キューブを振ると音を鳴らすプログラムを作成しなさい．
    音程や音長を変更してもよい．
"""
import sys # sys モジュール(sys.exit()使用に必要)
import signal # singnalモジュール
# toio.simple モジュールから SimpleCube を取り込み
from toio.simple import SimpleCube, Note, MotionDetectionData # Note: 音程の名称

LOOP = True # 繰り返し継続フラグ（グローバル変数）

# シグナル割り込みハンドラ（端末上で Ctrl-C を押すと繰り返し終了）
def ctrl_c_handler(_signum, _frame):
    global LOOP
    print("Ctrl-C")
    LOOP = False

signal.signal(signal.SIGINT, ctrl_c_handler) # Add signal handler

# モーションデータ取得関数
def get_motion(self) -> MotionDetectionData | None:
    if self._async._motion is None:
        return None
    else:
        return self._async._motion

# クラス SimpleCube にメソッド get_motion() を追加
SimpleCube.get_motion = get_motion

# 音を鳴らすfunction
def play_sound(cube, melody):
    for sound in melody:
        cube.play_sound(note=sound[0], duration=sound[1]+0.15, wait_to_complete=False) # 発音後に待機しない
    cube.sleep(sound[1]) # 発音時間分，スリープ

# メイン関数
def main():
    with SimpleCube(name="m78") as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        print("Battery Level: ", cube.get_battery_level()) # バッテリーレベル表示
        cube.sleep(1.0) 

        melody = ((Note.C4, 0.5), (Note.D4, 0.5), (Note.E4, 0.5),
            (Note.F4, 0.5), (Note.G4, 1.0)) # 音程と音長をタプルでまとめる 
           
        last_orientation = cube.get_orientation()  # 最初の向きを保存

        while LOOP:
            # in state
            motion = cube.get_motion() # キューブのモーションデータ取得
            button_state = cube.is_button_pressed() # ボタンの状態

            # ボタンが押された場合
            if button_state == 128:
                print(f"Button pressed! {button_state}")
                play_sound(cube, melody)    

            # キューブの向きが変わった場合
            orientation = cube.get_orientation()
            if orientation != last_orientation:
                print(f"Orientation changed to {orientation}")
                play_sound(cube, melody)
                last_orientation = orientation

            # キューブが振られた場合
            if motion.shake > 0:
                print("Cube shaken!")
                play_sound(cube, melody)            
            cube.sleep(0.5)

    print("Disconnected.")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())