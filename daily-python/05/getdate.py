'''
Date: 2022-05-29 15:00:11
LastEditors: r7000p
LastEditTime: 2022-05-29 15:17:32
FilePath: \Daily\daily-python\05\getdate.py
'''
import random
import time
import csv

def generate_random_str(len):
    str = ""
    for i in range(len):
        str += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    return str

# t = time.time()
# ts = int(t)
# tms = int(round(t * 1000))

with open("./daily-python/05/1bdate.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["imei", "request_id"])
    for i in range(1000000):
        imei = generate_random_str(12)
        t = int(time.time())
        writer.writerow([imei, imei + str(t)])

# for i in range(100000):
#     print("imei: ", generate_random_str(12), "\trequest_id: ", int(time.time()))