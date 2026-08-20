import psutil
import platform
import os
import shutil
import ctypes

def get_volume_label(drive_letter):

    drive = f"{drive_letter.strip().upper()[0]}:\\"
    
    volume_name_buffer = ctypes.create_unicode_buffer(1024)
    
    success = ctypes.windll.kernel32.GetVolumeInformationW(
        ctypes.c_wchar_p(drive),
        volume_name_buffer,
        ctypes.sizeof(volume_name_buffer),
        None, None, None, None, 0
    )
    
    if success:
        return volume_name_buffer.value
    else:
        raise ctypes.WinError()

def find_pico_drive():
    for part in psutil.disk_partitions(all=False):
        try:
            if platform.system() == "Windows":
                volume_label = os.path.basename(part.mountpoint.rstrip("\\/"))
                try:
                    print("H",get_volume_label(part.device))
                    print("j",   part.mountpoint)
                except:pass
                try:
                    if "RPI-RP2" in get_volume_label(part.mountpoint) or "CIRCUITPY" in get_volume_label(part.mountpoint):
                        return part.device, part.mountpoint
                except:pass
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
                    os.remove(file)
    else:
        print("Pico not found.")
    print(f"file")

