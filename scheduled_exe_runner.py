import subprocess
import os
import time
from datetime import datetime, timedelta
import threading

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

def run_exe(exe_path, directory, exe_args):
    try:
        # 切换到指定目录
        os.chdir(directory)
        log_message(f"已切换到目录 {directory}")
        # 构建带参数的命令
        full_command = f'{exe_path} {" ".join(exe_args)}'
        # 使用 runas 命令以管理员权限运行带参数的 exe 文件
        # runas_command = f'runas /user:Administrator "{full_command}"'
        # log_message(f"执行命令: {runas_command}")
        result = subprocess.run(full_command, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            log_message(f"执行成功，输出：{result.stdout}")
        else:
            log_message(f"执行失败，错误信息：{result.stderr}")
    except Exception as e:
        log_message(f"发生未知错误：{e}")

def run_daily_task(exe_path, directory, daily_exe_args):
    log_message(f"开始执行每日任务，传递参数 {daily_exe_args}...")
    run_exe(exe_path, directory, daily_exe_args)
    log_message("exe 程序已退出，每日执行完成。")

def run_weekly_task(exe_path, directory, weekly_exe_args, last_weekly_run_date):
    log_message(f"开始执行每周任务，传递参数 {weekly_exe_args}...")
    run_exe(exe_path, directory, weekly_exe_args)
    log_message("exe 程序已退出，每周执行完成。")
    return datetime.now().date()

def run_exe_at_scheduled_time(exe_path, directory, daily_scheduled_time, daily_exe_args, weekly_scheduled_time, weekly_exe_args):
    last_weekly_run_date = None
    log_message(f"程序启动，等待每日执行时间 {daily_scheduled_time} 和每周执行时间 {weekly_scheduled_time}...")
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_date = now.date()

        # 处理每日任务
        if current_time == daily_scheduled_time:
            daily_thread = threading.Thread(target=run_daily_task, args=(exe_path, directory, daily_exe_args))
            daily_thread.start()

        # 处理每周任务
        if current_time == weekly_scheduled_time:
            if last_weekly_run_date is None or (current_date - last_weekly_run_date).days >= 7:
                weekly_thread = threading.Thread(target=run_weekly_task, args=(exe_path, directory, weekly_exe_args, last_weekly_run_date))
                weekly_thread.start()
                last_weekly_run_date = current_date

        remaining_daily_time = (datetime.strptime(daily_scheduled_time, "%H:%M") - datetime.strptime(current_time, "%H:%M")).total_seconds()
        if remaining_daily_time < 0:
            remaining_daily_time += 24 * 60 * 60
        remaining_weekly_time = (datetime.strptime(weekly_scheduled_time, "%H:%M") - datetime.strptime(current_time, "%H:%M")).total_seconds()
        if remaining_weekly_time < 0:
            remaining_weekly_time += 24 * 60 * 60
        log_message(f"当前时间 {current_time}，距离每日执行时间还剩 {remaining_daily_time // 60} 分钟，距离每周执行时间还剩 {remaining_weekly_time // 60} 分钟，继续等待...")
        # 等待 1 分钟后再次检查
        time.sleep(60)

if __name__ == "__main__":
    # 指定 exe 文件的路径
    exe_path = "ok-ww.exe"
    # 指定目录
    directory = "E:\Documents\code\ok-wuthering-waves"
    # 指定每天运行的时间，格式为 "HH:MM"
    daily_scheduled_time = "05:00"
    # 指定 exe 程序需要的参数，以列表形式提供
    daily_exe_args = ["-t 1", "-e"]
    # 指定每周运行的时间，格式为 "HH:MM"
    weekly_scheduled_time = "06:00"
    # 指定每周 exe 程序需要的参数，以列表形式提供
    weekly_exe_args = ["-t 5", "-e"]
    run_exe_at_scheduled_time(exe_path, directory, daily_scheduled_time, daily_exe_args, weekly_scheduled_time, weekly_exe_args)
    