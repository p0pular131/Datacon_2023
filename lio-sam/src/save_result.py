#!/usr/bin/env python3

import rospy
import csv
import pandas as pd
from nav_msgs.msg import Odometry

data_list = []
file_name = 'result.csv'

class make_result :
    def __init__(self) :
        rospy.init_node('result_node', anonymous=False)
        rospy.Subscriber('lio_sam/mapping/odometry', Odometry, self.odom_cb)
        

        self.secs = 1658814741
        self.cnt = 0

        self.E = 208794.0599
        self.N = 534534.5496

        self.x, self.y = 0,0



    def odom_cb(self, data) :
        # 위치추정을 위해 전 값을 저장
        if data.header.stamp.secs == 1658814740 :
            self.x = data.pose.pose.position.x
            self.y = data.pose.pose.position.y

        # 데이터를 저장해야하는 경우
        if self.secs == data.header.stamp.secs :
            # 데이터 계산
            odom_x = data.pose.pose.position.x
            odom_y = data.pose.pose.position.y
            self.E += -(odom_y - self.y)
            self.N += odom_x - self.x

            # 데이터 저장
            # data_list.append([data.header.stamp.secs, self.E, self.N])
            print(data.header.stamp.secs)
            csv_writer.writerow([data.header.stamp.secs, self.E, self.N])

            # 변수값 갱신
            self.secs += 1 
            self.cnt += 1 
            self.x, self.y = odom_x, odom_y

                

if __name__ == "__main__" :
    with open(file_name, 'w', newline='' ) as csvfile :
        csv_writer = csv.writer(csvfile)
        make_result()
        rospy.spin()


    