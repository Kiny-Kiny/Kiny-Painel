from os import execl;from sys import executable
def run(): execl(executable, executable, *argv)
