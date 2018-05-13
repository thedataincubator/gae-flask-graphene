import os
import sys
directory = os.getcwd()
sys.path.append(directory)
sys.path.append(os.path.join(directory, "vendor"))
from starwars import initialize

if __name__ == "__main__":
  initialize()
