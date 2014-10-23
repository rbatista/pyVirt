#!/usr/bin/env python

import sys
from cli import Cli

def main():
    c = Cli()
    return c.parse(sys.argv)

if __name__ == '__main__':
    sys.exit(main())
