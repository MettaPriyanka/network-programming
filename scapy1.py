from scapy.all import *
import psutil
from collections import defaultdict
import os
from threading import Thread
import pandas as pd
all_macs = {iface.mac for iface in ifaces.values()}
print(all_macs)
connection2pid = {}
pid2traffic = defaultdict(lambda: [0, 0])
print(pid2traffic)
global_df = None
is_program_running = True
def get_size(bytes):
    """
    returns size of bytes in a nice format"""
    for unit in ['','K','M','G','T','P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /=1024
        
while True:
 #sleep for Uodate delay seconds
    time.sleep(UPDATE_DELAY)
    io_2 = psutil.net_io_counters(pernic=True)
    data = []
    for iface, iface_io in io.times():
        upload_speed, download_speed = io_2[ifaces].byte_sent - iface_io.bytes_sent,io_2[iface].bytes_recv - iface_io.bytes_recv
        data.append({
        "iface": iface,"Download":get_size(io_2[iface].bytes_recv),
        "Upload": get_size(io_2[iface].bytes_sent),
        "Upload Speed":f"{get_size(upload_speed / UPDATE_DELAY )}/S"
        "Download Speed":f"{get_siz(download_speed / UPDATE_DELAY)}/S"
        })
    io = io_2
    df=pd.DataFrame(data)
    df_sort_values("Download",inplace=True,ascending=False)
    os.system("cls") if "nt" in os.name else os.system("clear")
    print(df.to_string())
    
    
    