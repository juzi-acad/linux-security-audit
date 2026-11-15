



import platform
import os
import stat
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
        bash_users = []
        nologin_users = []
        other_users = []

        for user in users:
            fields = user.strip().split(":")
            if len(fields) == 7:
                username = fields[0]
                shell = fields[6]

                if shell.endswith("nologin") or shell.endswith("false"):
                    nologin_users.append(username)
                elif shell.endswith(("bash", "sh", "zsh", "fish")):
                    bash_users.append(username)
                else:
                    other_users.append(username)

        print("\n账户分类结果：")
        print("可能可以交互式登录的账户：", bash_users)
        print("禁止交互式登录的账户：", nologin_users)
        print("使用其他 Shell 的账户：", other_users)
        root_users = []

        for user in users:
            fields = user.strip().split(":")
            uid = int(fields[2])

            if uid == 0:
                root_users.append(fields[0])

        print("\nUID 0 超级用户检查：")
        print("UID 为0的账户:", root_users)
        if root_users == ["root"]:
            print("检查结果：正常，未发现异常UID 0 账户。")

        elif len(root_users) == 0:
            print("安全警告：未检测到任何UID为0的账户！")

        else:
            print("安全警告：发现异常UID 0 账号，请进一步检查！")
    except PermissionError:
        print("没有权限读取 /etc/passwd。")
    except OSError as error:
        print("读取账户文件时发生错误：", error)

if system_name == "Linux":
    print("\n[4] Linux 密码文件安全检查")

    shadow_path = "/etc/shadow"

    try:
        shadow_info = os.stat(shadow_path)
        shadow_permissions = stat.S_IMODE(shadow_info.st_mode)

        print("shadow 文件权限：", oct(shadow_permissions))
        if (shadow_info.st_uid == 0
               and not (shadow_permissions & stat.S_IWGRP)
               and not (shadow_permissions & stat.S_IRWXO)):
            print("权限检查结果：符合基本安全要求。")
        else:
            print("安全警告：/etc/shadow 文件权限配置存在风险！")
    except PermissionError:
        print("没有权限检查shadow文件。")

    except OSError as error:
        print("检查shadow文件时发生错误：",error)
if system_name == "Linux":
    print("\n[5]linux 重要文件权限检查")
    important_files = {
        "/etc/passwd":0o644,
        "/etc/shadow":0o640,
        "/etc/group":0o644,
        "/etc/sudoers":0o440,
   }
    for file_path,expected_permission in important_files.items():
        try:
            file_info = os.stat(file_path)
            permissions = stat.S_IMODE(file_info.st_mode)

            print(f"\n文件：{file_path}")
            print("当前权限：", oct(permissions))

            if permissions == expected_permission:
                print("检查结果：正常")
            else:
                print("安全警告：文件权限与预期不符！")

        except OSError as error:
            print("检查失败：", error)
print("\n检查完成！")
print("=" * 45)
