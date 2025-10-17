import psutil
import time

def monitor_cpu(threshold):
    """
    Continuously monitor CPU usage.
    Displays an alert if CPU usage exceeds the given threshold.

    Parameters:
        threshold (int): CPU usage percentage to trigger alert.
    """
    print("Monitoring CPU usage... (Press Ctrl+C to stop)")

    try:
        while True:
            # Get CPU usage for all cores (averaged over 1 second)
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU usage: {cpu_usage}%")

            # Print alert if usage exceeds threshold
            if cpu_usage > threshold:
                print(f"⚠️ Alert! CPU usage exceeds threshold: {cpu_usage}%")

            # Sleep for a short period before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n✅ Monitoring stopped by user.")
    except Exception as e:
        print(f"❌ Error occurred: {e}")


if __name__ == "__main__":
    # Start monitoring with default threshold = 80%
    monitor_cpu(80)
