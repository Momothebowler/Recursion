#in cmd do
#cd Desktop
#python
#from Deal import per
import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('HelloThere').sheet1
list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)

q=1
t=1
v=0
writes = 1
sleep = 0
number = 1000000
p = time.time()

def per(n,z,r):
    global q
    global t
    global number
    p = time.time()

    number = n
    
    if len(str(n))==1:
        print (n)
        return "DONE"
    while number == n and n!=z:
        pert(number,r)
        n-=1
    if number == n and n==z:
        t = time.time() - p
        print("DONE, Took: ", t, "seconds")

def pert(n,r):
    global writes
    global v
    global number
    global sleep
    if len(str(n))==1:
        if v>=r:
            print("#",number)
            print ("Times: ", v, "done", "Writes ", writes)
            if(writes<99):
                writes += 1
            sheet.append_row([str(number),str(v)])
        v = 0
        number -= 1
        return
    
    digits = [int(i) for i in str(n)]

    results = 1
        
    for j in digits:
        results *= j

    v+=1

    if(writes >= 99):
        while sleep<=101:
            time.sleep(1)
            sleep+=1
            print(sleep,end="\r")
        if sleep>100:
            writes = 1
            sleep = 0
    pert(results,r)
