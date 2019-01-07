#!/usr/bin/env python3
# This script reads from STDIN and greets the name it receives
import sys
name = sys.stdin.read()
print("Hello " + name + "!")