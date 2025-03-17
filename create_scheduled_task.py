import subprocess
import sys

def create_scheduled_task(task_name, command, schedule_type, days=None, time="03:00"):
    """
    创建 Windows 计划任务
    :param task_name: 任务名称
    :param command: 要执行的命令（含完整路径）
    :param schedule_type: 计划类型（DAILY/WEEKLY）
    :param days: 每周执行的星期几（WEEKLY 时使用）
    :param time: 执行时间（HH:MM 格式）
    """
    try:
        # 先删除已存在的同名任务
        try:
            subprocess.run(["schtasks", "/delete", "/tn", task_name, "/f"], check=True)
        except subprocess.CalledProcessError as e:
            if e.returncode == 1:  # 任务不存在的错误码
                pass
            else:
                raise

        # 创建新任务
        args = [
            "schtasks", "/create", "/tn", task_name,
            "/tr", command,
            "/sc", schedule_type,
            "/st", time
        ]

        if schedule_type == "WEEKLY":
            args.extend(["/d", days])

        subprocess.run(args, check=True)
        print(f"任务 '{task_name}' 创建成功")

    except subprocess.CalledProcessError as e:
        print(f"创建任务失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 请根据实际情况修改以下参数
    A_EXE_PATH = r"E:\Documents\code\ok-wuthering-waves\ok-ww.exe"  # 替换为 a.exe 的实际路径
    DAILY_TIME = "05:00"  # 每天执行时间
    WEEKLY_TIME = "06:00"  # 每周执行时间
    WEEKLY_DAY = "MON"  # 每周执行的星期几（MON/TUE/WED/THU/FRI/SAT/SUN）
    RECORD_SCRIPT_PATH = r"E:\Documents\code\ok-wuthering-waves\record_execution.py"  # 替换为记录执行次数脚本的实际路径

    # 每天执行的任务
    daily_command = f'python "{RECORD_SCRIPT_PATH}" daily && "{A_EXE_PATH}" -t 1 -e'
    create_scheduled_task(
        task_name="DailyAExeTask",
        command=daily_command,
        schedule_type="DAILY",
        time=DAILY_TIME
    )

    # 每周执行的任务
    weekly_command = f'python "{RECORD_SCRIPT_PATH}" weekly && "{A_EXE_PATH}" -t 4 -e'
    create_scheduled_task(
        task_name="WeeklyAExeTask",
        command=weekly_command,
        schedule_type="WEEKLY",
        days=WEEKLY_DAY,
        time=WEEKLY_TIME
    )

    print("所有任务创建完成")