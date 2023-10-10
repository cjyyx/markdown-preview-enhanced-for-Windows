import os

dir_path = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')

# print("在管理员终端输入以下命令")

# print("ASSOC .md=MarkDown")
# print(f"FTYPE MarkDown=node {dir_path}/crossnote.js %1")


cmd=f"""
set cmd_path=%0
set md_path=%1

node "{dir_path}/crossnote.js" %md_path%
"""


with open("crossnote.cmd", "w", encoding="utf-8") as f:
    f.write(cmd)

