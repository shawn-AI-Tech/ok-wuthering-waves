import json
import os
import sys

# 定义记录文件路径
RECORD_FILE = "execution_records.json"

def load_records():
    """
    加载执行记录
    """
    if os.path.exists(RECORD_FILE):
        with open(RECORD_FILE, 'r') as f:
            return json.load(f)
    return {'daily': 0, 'weekly': 0}

def save_records(records):
    """
    保存执行记录
    """
    with open(RECORD_FILE, 'w') as f:
        json.dump(records, f)

def main(task_type):
    # 加载记录
    records = load_records()

    # 更新执行次数
    if task_type == 'daily':
        records['daily'] += 1
    elif task_type == 'weekly':
        records['weekly'] += 1

    # 保存记录
    save_records(records)

    # 显示执行次数
    print(f"Daily execution count: {records['daily']}")
    print(f"Weekly execution count: {records['weekly']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python record_execution.py [daily|weekly]")
        sys.exit(1)
    task_type = sys.argv[1].lower()
    if task_type not in ['daily', 'weekly']:
        print("Invalid task type. Please use 'daily' or 'weekly'.")
        sys.exit(1)
    main(task_type)