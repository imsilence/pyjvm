#encoding: utf-8

import sys
import logging

from cmd import Cmd
from jvm import JVM


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    cmd = Cmd.parse(sys.argv[1:])
    if cmd.version_flag:
        cmd.version()
    elif cmd.help_flag  or '' == cmd.clazz:
        cmd.help()
    else:
        JVM(cmd).start()

