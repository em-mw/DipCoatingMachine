import psutil
import platform
import os
import shutil

def find_pico_drive():
    for part in psutil.disk_partitions(all=False):
        try:
            if platform.system() == "Windows":
                volume_label = os.path.basename(part.mountpoint.rstrip("\\/"))
            else:
                # On Linux, check mount path directly
                volume_label = os.path.basename(part.mountpoint)
            
            if "RPI-RP2" in volume_label or "CIRCUITPY" in volume_label:
                return part.device, part.mountpoint
        except Exception:
            continue
    return None, None
def transfer():
    device, mountpoint = find_pico_drive()
    if mountpoint:
        print(f"Pico detected at: {mountpoint} ({device})")

        for file in os.listdir(os.getcwd()):
            print(os.listdir(os.getcwd()))
            print(f"{file.find('p')} {file[-3:]}")
            if file.find('p') == 0 and file[-3:]==".py":  #make sure to add number recognition to this
                try: int(file[1])
                except:pass
                else:
                    shutil.copy(file, mountpoint)
                    print(file)
    else:
        print("Pico not found.")
    print(f"file")

