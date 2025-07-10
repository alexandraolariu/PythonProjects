# ------SIMPLE SYSTEM MONITOR------
import psutil
import datetime

MONITOR_INTERVAL_SECONDS = 5
DISK_PARTITION = 'C:/'

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory_usage=psutil.virtual_memory()
    return memory_usage.percent

def get_disk_usage():
    disk = psutil.disk_usage(DISK_PARTITION)
    return disk.percent

def display_logs(cpu_usage,memory_usage,disk_usage):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("System status at " + now)
    print("CPU usage: " + str(cpu_usage) + "%")
    print("Memory usage: " + str(memory_usage) + "%")
    print("Disk usage: " + str(disk_usage) + "%")

def main():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    display_logs(cpu_usage,memory_usage,disk_usage)

if __name__ == "__main__":
    main()