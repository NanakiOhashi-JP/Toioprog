
import sys # sys モジュール(sys.exit()使用に必要)
import signal # singnalモジュール
import random # 乱数モジュール
# toio.simple モジュールから SimpleCube を取り込み
from toio.simple import SimpleCube, MotionDetectionData

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

# 色をランダムに変更し、変更したカラーを表示
def change_color(cube):
    red = random.randint(0, 255) # 0-255 の範囲の乱数
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    cube.turn_on_cube_lamp(r=red, b=blue, g=green, duration=0.5) # 0.5秒点灯
    print(f"Lamp color (R,G,B) = ({red}, {green}, {blue})")

# メイン関数
def main():
    with SimpleCube(name="m78") as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        last_orientation = cube.get_orientation()
        cube.sleep(1.0) 
        while LOOP:
            # in state
            motion = cube.get_motion() # キューブのモーションデータ取得
            button_state = cube.is_button_pressed() # ボタンの状態

            # ボタンが押された場合
            if button_state == 128:
                print(f"Button pressed! {button_state}")
                change_color(cube)
            
            # キューブの向きが変わった場合
            orientation = cube.get_orientation()
            if orientation != last_orientation:
                print(f"Orientation changed to {orientation}")
                change_color(cube)
                last_orientation = orientation

            # キューブが振られた場合
            if motion.shake > 0:
                print("Cube shaken!")
                change_color(cube)
            

    print("Disconnected.")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())