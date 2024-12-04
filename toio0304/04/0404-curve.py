import sys
from toio.simple import SimpleCube

"""Here, Write down Addtional Modules, Global Variables, Functions."""

# Main functions
def main():
    with SimpleCube() as cube:
        """Write down a code here (connectiong, control, etc,,,)"""

        cube.run_motor(30, 10, 0)
        cube.sleep(3)
        cube.run_motor(10, 30, 0)
        cube.sleep(3)
        cube.stop_motor()

        return 0

# Excute main(), when Python runs this file direcctly
if __name__ == "__main__":
    sys.exit(main())