#!/usr/bin/env python3

import os
import subprocess
import time


bag_files = [
    'bagfile1.bag',
    'bagfile2.bag',
    'bagfile3.bag'
]
cnt = 0

for bag_file in bag_files:
    play_command = f'rosbag play --clock {bag_file}'
    
    subprocess.Popen(play_command, shell=True)
    
    if cnt == 0 :
        play_time = 508.102483
    elif cnt == 1 :
        play_time = 490.719804
    elif cnt == 2 :
        play_time = 37.660221

    time.sleep(play_time)  

    # 현재 재생 중인 프로세스 종료
    os.system("pkill -f 'rosbag play'")
    cnt+=1

# print("All bag files have been played.")