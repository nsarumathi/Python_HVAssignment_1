import msvcrt
import psutil

threshold = 80

def check_CPU_Usage():
 try:
    print("Monitoring CPU Usage:")
    count_seconds=0
    while True:
        if msvcrt.kbhit():  # user pressed any key
            print("Monitoring stopped by user.")
            break
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > threshold:
            count_seconds=0
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
        elif cpu_usage<10:
            count_seconds+=1
            print(f"CPU low:{cpu_usage}%")           
            if count_seconds >= 10:      # low for 10 continuous seconds
                raise Exception("CPU low for 10 seconds!")
 except KeyboardInterrupt:
   print(f"Monitoring stopped by user")
 except Exception as e:
   print(f"Custom exception occured: {e}")


# ---- MAIN SCRIPT ----
check_CPU_Usage()