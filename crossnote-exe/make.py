debug_mode = 0

import os

dir_path = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
ddir_path = os.path.dirname(dir_path)

def test(cmd):
    print("测试命令：", cmd)
    os.system(cmd)
    print("")

if not debug_mode:
    # https://www.cnblogs.com/sandeepin/p/gcc-win-gui-no-cmd.html
    os.system("windres resource.rc -O coff -o resource.res")
    os.system(f"gcc -mwindows crossnote.c resource.res -o {ddir_path}/crossnote.exe")
    exit(0)

print("开始编译")
if os.system(f"gcc crossnote.c -o {ddir_path}/crossnote.exe"):
    print("编译失败")
    exit(1)

print("开始测试")
test(f"{ddir_path}/crossnote.exe {ddir_path}/testCase/离散数学复习重点.md")
