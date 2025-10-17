######## Monitoring CPU usage ########
import psutil
import time

def monitor_cpu(threshold):
    print("Monitoring CPU usage...")
    
    try:
        while True:
             
            cpu_usage = psutil.cpu_percent(interval=1)      #Get current CPU usage as a percentage at interval of 1 second
            print(f"Current CPU usage: {cpu_usage}%")
            
            if cpu_usage > threshold:                       #Check if the CPU usage exceeds the threshold
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

    except KeyboardInterrupt:
        print("Monitoring stopped by user.")

    except Exception as e:
        print(f"An error occurred during CPU monitoring: {e}")

if __name__ == "__main__":
    monitor_cpu(threshold=80)                               #You can modify the threshold here if needed
######## Monitoring CPU usage ########
import psutil
import time

def monitor_cpu(threshold):
    print("Monitoring CPU usage...")
    
    try:
        while True:
             
            cpu_usage = psutil.cpu_percent(interval=1)      #Get current CPU usage as a percentage at interval of 1 second
            print(f"Current CPU usage: {cpu_usage}%")
            
            if cpu_usage > threshold:                       #Check if the CPU usage exceeds the threshold
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

    except KeyboardInterrupt:
        print("Monitoring stopped by user.")

    except Exception as e:
        print(f"An error occurred during CPU monitoring: {e}")

if __name__ == "__main__":
    monitor_cpu(threshold=80)                               #You can modify the threshold here if needed