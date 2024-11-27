from toio.simple import SimpleCube
import random as rd

cube = SimpleCube(m78) # type: ignore
print("Connected")
cube.sleep(0.5)
cube.spin(30,5)
cube.sleep(0.5)
cube.disconnect()
print("Disconnected")
