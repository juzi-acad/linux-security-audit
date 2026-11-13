
import platform
from datetime import datetime

print("=" * 40)
print("       Linux Security Audit")
print("       系统信息检查模块")
print("=" * 40)

system_name = platform.system()
system_version = platform.release()
python_version = platform.python_version()
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("操作系统：", system_name)
print("系统版本：", system_version)
print("Python版本：", python_version)
print("检查时间：", current_time)

print("=" * 40)

if system_name == "Linux":
    print("检测到 Linux 系统，可以进行安全检查。")
elif system_name == "Windows":
    print("当前是 Windows 系统，暂不执行 Linux 安全检查。")
else:
    print("当前系统暂不支持安全检查。")
