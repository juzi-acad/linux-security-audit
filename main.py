import platform
import os
from datetime import datetime

print("=" * 45)
print("       Linux Security Audit")
print("       Linux 系统安全检查工具")
print("=" * 45)

# 获取系统基本信息
system_name = platform.system()
system_version = platform.release()
python_version = platform.python_version()
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("\n[1] 系统基本信息")
print("操作系统：", system_name)
print("系统版本：", system_version)
print("Python版本：", python_version)
print("检查时间：", current_time)

# 检查当前登录用户
print("\n[2] 当前用户信息")
print("当前用户名：", os.getenv("USER"))
print("\n[3] linux 用户账号检查")

with open("/etc/passwd","r") as file:
     users = file.readlines()   
print("系统账户总数",len(users))
print("\n检查完成！")
print("=" * 45)
