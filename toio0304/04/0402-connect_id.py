import sys
from toio.simple import SimpleCube

"""Here, Write down Addtional Modules, Global Variables, Functions."""

# Main functions
def main():
    with SimpleCube() as cube:
        """Write down a code here (connectiong, control, etc,,,)"""
        
        # display the cube name.
        print("Cube name: ", cube.get_cube_name())
        
        cube.sleep(0.5)
        cube.spin(30, 2)
        cube.sleep(0.5)

        return 0

# Excute main(), when Python runs this file direcctly
if __name__ == "__main__":
    sys.exit(main())