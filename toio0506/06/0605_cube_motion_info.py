# 0605_cube_motion_info.py: キューブの情報表示（モーションデータ取得）
import sys # sys モジュール(sys.exit()使用に必要)
import signal # singnalモジュール
from logging import * # logging モジュール（ログ表示に必要）
# toio.simple モジュールから SimpleCube, MotionDetectionData を取り込み
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

# メイン関数
def main():
    with SimpleCube(name="m78", log_level=INFO) as cube: # 指定のキューブを探索，接続
        print("Cube name: ", cube.get_cube_name()) # キューブ名表示
        print("Battery Level: ", cube.get_battery_level()) # バッテリーレベル表示
        cube.sleep(1.0) 
        while LOOP:
            posture = cube.get_posture() # キューブの姿勢（上向きの面）検出
            roll, pitch, yaw = cube.get_3d_angle() # キューブの姿勢角（ロール，ピッチ，ヨー）検出
            button_state = cube.is_button_pressed() # ボタンの状態検出
            motion = cube.get_motion() # キューブのモーションデータ取得
            print(f"Posture: {posture}, 3D angle: {roll}, {pitch}, {yaw}, Button: {button_state}")
            print(f"collision: {motion.collision}, double_tap: {motion.double_tap}, horizontal: {motion.horizontal}, shake: {motion.shake}")
            cube.sleep(0.5)
    print("Disconnected.")
    return 0

# このファイルがPythonから直接起動されたとき，main() を実行
if __name__ == "__main__":
    sys.exit(main())