import os
import sys
from pathlib import Path

if __name__ == "__main__":
    print("-" * 80)
    print(f"__file__       - {os.path.abspath(__file__)}")
    print(f"sys.argv[0]    - {os.path.abspath(sys.argv[0])}")
    print(f"sys.path[0]    - {os.path.abspath(sys.path[0])}")
    print(f"sys.path[1]    - {os.path.abspath(sys.path[1])}")
    print(f"Path.cwd()     - {os.path.abspath(Path.cwd())}")
    print(f"os.getcwd()    - {os.path.abspath(os.getcwd())}")
    print(f"sys.executable - {os.path.abspath(sys.executable)}")
    print("-" * 80)
