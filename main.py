



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

# 判断操作系统类型
if system_name == "Linux":
    print("\n检测到 Linux 系统，可以进行安全检查。")
elif system_name == "Windows":
    print("\n当前是 Windows 系统，暂不执行 Linux 安全检查。")
else:
    print("\n当前系统暂不支持安全检查。")

# 检查当前登录用户
print("\n[2] 当前用户信息")
current_user = os.getenv("USER") or os.getenv("USERNAME")
print("当前用户名：", current_user)

# Linux 用户账号检查
if system_name == "Linux":
    print("\n[3] Linux 用户账号检查")

    try:
        with open("/etc/passwd", "r") as file:
            users = file.readlines()

        print("系统账户总数：", len(users))

    except PermissionError:
        print("没有权限读取 /etc/passwd。")
    except OSError as error:
        print("读取账户文件时发生错误：", error)

print("\n检查完成！")
print("=" * 45)
