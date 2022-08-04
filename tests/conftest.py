import pathlib
import sys

HOMEDIR = pathlib.Path(__file__).parent.parent.absolute().as_posix()
sys.path.append(HOMEDIR)
