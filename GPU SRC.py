import GPUtil
import time,os

os.system("title GPU Monitoring")
os.system("color 3")
os.system("cls")

class GpuInfo:
    def __init__(self, name="", temperature=""):
        self.Name = name
        self.Temperature = temperature

def get_gpu_info():
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]
            return GpuInfo(name=gpu.name, temperature=gpu.temperature)
    except Exception as e:
        print(f"Error retrieving GPU info: {e}")

    return GpuInfo()

def main():
    interval = 5
    while True:
        try:
            gpu_info = get_gpu_info()


            print("-----------------------------------")
            print(f"GPU Name: {gpu_info.Name}")
            print(f"Temperature: {gpu_info.Temperature}°C")
            print("-----------------------------------\n")
            time.sleep(interval)
        except KeyboardInterrupt:
            print("Exiting GPU Monitor.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("GPU Monitor started. Press Ctrl+C to exit.")
    main()
