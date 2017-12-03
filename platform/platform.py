import platform

print('Python version:', platform.python_version())
# 3.5.2

print('Platform machine:', platform.machine())
# amd64

print('Architecture:', platform.architecture())
# ('64bit', 'ELF')

print('Node:', platform.node())
# 'local'

print('Platform:', platform.platform())
# 'FreeBSD-10.3-STABLE-amd64-64bit-ELF'

print('System:', platform.system())
# 'FreeBSD'

print('Uname:', platform.uname())
# uname_result(system, node, release, version, machine, processor)