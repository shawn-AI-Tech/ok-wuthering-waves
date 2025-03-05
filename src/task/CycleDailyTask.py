import re

from ok import Logger
from src.task.BaseWWTask import number_re
from src.task.DailyTask import DailyTask

logger = Logger.get_logger(__name__)

import time
import psutil
import win32api
import win32con
import win32process

# 配置应用程序路径（修改为你的目标程序）
APP_PATH = "F:\\Wuthering Waves\\Wuthering Waves Game\\Client\\Binaries\\Win64\\Client-Win64-Shipping.exe"
APP_NAME = "Client-Win64-Shipping.exe"

def is_program_running(program_name):
    """检查程序是否正在运行"""
    for proc in psutil.process_iter(attrs=['name']):
        if proc.info['name'].lower() == program_name.lower():
            return proc.pid  # 返回进程 ID
    return None  # 未运行

def start_program():
    """启动程序"""
    print(f"启动 {APP_NAME}...")
    si = win32process.STARTUPINFO()
    pi = win32process.CreateProcess(APP_PATH, "", None, None, False, win32con.NORMAL_PRIORITY_CLASS, None, None, si)
    return pi[2]  # 返回进程 ID

def close_program(pid):
    """关闭程序"""
    try:
        handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, False, pid)
        win32api.TerminateProcess(handle, 0)
        win32api.CloseHandle(handle)
        print(f"{APP_NAME} 已关闭 (PID: {pid})")
    except Exception as e:
        print(f"关闭 {APP_NAME} 失败: {e}")

class CycleDailyTask(DailyTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.description = "Login, claim monthly card, farm echo, and claim daily reward"
        self.name = "Cycle Daily Task"
        self.first_time = True
        self.scheduled_interval = 60*60*24
        self.task_complete_count = 0
        
    def run(self):
        
        while True:

            self.ensure_main(time_out=180)
            self.farm_tacet()
            self.claim_daily()
            self.claim_mail()
            self.claim_millage()
            self.task_complete_count += 1
            self.log_info('Task completed times: {}'.format(self.task_complete_count), notify=True)
                
            self.ensure_main(time_out=180)
                
            time.sleep(self.scheduled_interval)

    # def run(self):
        
    #     while True:
    #         if self.first_time:
    #             self.ensure_main(time_out=180)
    #             # self.farm_tacet()
    #             # self.claim_daily()
    #             # self.claim_mail()
    #             # self.claim_millage()
    #             pid = is_program_running(APP_NAME)
    #             self.log_info(f"{APP_NAME} 正在运行 (PID: {pid})，执行任务中...")
    #             # 模拟执行任务（等待 10 秒）
    #             time.sleep(10)
                
    #             self.log_info('Task completed', notify=True)
    #             self.first_time = False
                
                
    #             close_program(pid)
    #             time.sleep(self.scheduled_interval)
    #         else:
                
    #             pid = is_program_running(APP_NAME)
    #             # 如果未运行，则启动程序
    #             if pid is None:
    #                 pid = start_program()
    #                 time.sleep(60)  # 等待 20 秒，确保程序启动完成
                    
    #             self.ensure_main(time_out=180)
                
    #             self.log_info(f"{APP_NAME} 正在运行 (PID: {pid})，执行任务中...")
    #             # 模拟执行任务（等待 10 秒）
    #             time.sleep(10)

    #             close_program(pid)
    #             time.sleep(self.scheduled_interval)



echo_color = {
    'r': (200, 255),  # Red range
    'g': (150, 220),  # Green range
    'b': (130, 170)  # Blue range
}
