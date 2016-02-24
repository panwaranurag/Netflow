
import csv
import numpy as np
import os

users = []
userid_file = raw_input("Please enter user id file:")
with open(userid_file, 'rt') as file:
    reader = csv.reader(file, delimiter='|', skipinitialspace=True)
    for line in reader:
        users.append([line[0][5:],line[3].strip()]) #Ignoring first 5 chararcter of username which is user-
        #contains users and ipaddresses
users = np.array(users)
unique_user = set(users[:,0])    #Set is used to get unique users
unique_user = list(unique_user) #unique_user contains list of unique users

dict_user = {}
#for item in unique_user: #this is the only time you are actually looping through the list
    #open('%s.txt'%(item,), 'w')
#users contains usera and ip address as numpy array
#creating a dictionary with userid and ip address
for item in unique_user:
    lst = []
    for i in range(0,len(users)):
        if item == users[i,0]:
            lst.append(users[i,1])
    dict_user[item] = lst

#Condition check which row contain userid ip address
for item in unique_user:
    for file in os.listdir("."):
        if file.endswith(".ascii"):
            print file
            reader = csv.reader(open(file, 'rt'), delimiter='\t', skipinitialspace=True)
            writer = csv.writer(open('%s.txt'%(item,), "ab"), delimiter='\t', skipinitialspace=True)
            writer.writerow(["#:unix_secs","unix_nsecs", "sysuptime", "exaddr", "dpkts","doctets","first","last","engine_type",
                         "engine_id",	"srcaddr","dstaddr","nexthop","input","output","srcport","dstport","prot","tos",
                         "tcp_flags","src_mask","dst_mask","src_as","dst_as","router_sc"])
            for line in reader:
                if line[11] in dict_user[item]:
                    writer.writerow(line)
