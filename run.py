import subprocess
import os
import subprocess
import time
from datetime import datetime

def log_message(message):
    """
    记录日志到文件并打印到控制台
    :param message: 日志信息
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp}: {message}"
    print(log_entry)
    with open("execution_log.txt", "a") as log_file:
        log_file.write(log_entry + "\n")

def run_exe_at_scheduled_time(exe_path, directory, scheduled_time, exe_args):
    log_message(f"程序启动，等待执行时间 {scheduled_time}...")
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if current_time == scheduled_time:
            log_message(f"到达执行时间，开始执行 {exe_path} 并传递参数 {exe_args}...")
            try:
                # 切换到指定目录
                os.chdir(directory)
                log_message(f"已切换到目录 {directory}")
                # 构建带参数的命令
                full_command = f'{exe_path} {" ".join(exe_args)}'
                # 使用 runas 命令以管理员权限运行带参数的 exe 文件
                # runas_command = f'runas /user:Administrator "{full_command}"'
                log_message(f"执行命令: {full_command}")
                result = subprocess.run(full_command, capture_output=True, text=True, shell=True)
                if result.returncode == 0:
                    log_message(f"执行成功，输出：{result.stdout}")
                else:
                    log_message(f"执行失败，错误信息：{result.stderr}")
            except Exception as e:
                log_message(f"发生未知错误：{e}")

            log_message("执行完成，等待下一天执行时间...")
            # 等待一天，避免在同一分钟内再次执行
            time.sleep(24 * 60 * 60)
        else:
            remaining_time = (datetime.strptime(scheduled_time, "%H:%M") - datetime.strptime(current_time, "%H:%M")).total_seconds()
            if remaining_time < 0:
                remaining_time += 24 * 60 * 60
            log_message(f"当前时间 {current_time}，距离执行时间还剩 {remaining_time // 60} 分钟，继续等待...")
            # 等待 1 分钟后再次检查
            time.sleep(60)

if __name__ == "__main__":
    # 指定 exe 文件的路径
    exe_path = "ok-ww.exe"
    # 指定目录
    directory = "E:\Documents\code\ok-wuthering-waves"
    # 指定每天运行的时间，格式为 "HH:MM"
    scheduled_time = "09:55"
    # 指定 exe 程序需要的参数，以列表形式提供
    exe_args = ["-t 1", "-e"]
    run_exe_at_scheduled_time(exe_path, directory, scheduled_time, exe_args)
    