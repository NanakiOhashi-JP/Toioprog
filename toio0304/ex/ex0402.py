import sys
from toio.simple import SimpleCube

"""Here, Write down Addtional Modules, Global Variables, Functions."""

# Main functions
def main():
    with SimpleCube() as cube:
        """Write down a code here (connectiong, control, etc,,,)"""

        for i in range(4):
            cube.move(30, 1)
            cube.spin(15, 0.5)

        return 0

# Excute main(), when Python runs this file direcctly
if __name__ == "__main__":
    sys.exit(main())