"""
 You multiply each digit in a number
 317 = 3*1*7 = 21
 21 = 2 * 1 = 2
 So steps taken is 2 for 317
"""

import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Connect To Google Sheet
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('HelloThere').sheet1
list_of_hashes = sheet.get_all_records()

timer = 1
v = 0  # TODO: Remove
writes = 1
sleep = 0
number = 1000000  # TODO: remove this too?


def Recurse(n, z, r):  # Starting Number: Ending Number: Steps to check
    global timer
    start_time = time.time()  # time when program starts

    global number
    number = n  # Used to check when finished

    if len(str(n)) == 1:  # if only 1 digit is present (0-9)
        print(n)
        return "DONE"

    while number == n and n != z: #While not <10 keep running
        Algo(number, z)
        n -= 1

    if number == n and n == z:
        timer = time.time() - start_time
        print("DONE, Took: ", t, "seconds")


def Algo(n, z):
    global writes
    global v
    global number
    global sleep
    if len(str(n)) == 1:
        if v >= z:
            print("#", number)
            print("Times: ", v, "done", "Writes ", writes)
            if (writes < 99):
                writes += 1
            sheet.append_row([str(number), str(v)])
        v = 0
        number -= 1
        return

    digits = [int(i) for i in str(n)]

    results = 1

    for j in digits:
        results *= j

    v += 1

    if (writes >= 99):
        while sleep <= 101:
            time.sleep(1)
            sleep += 1
            print(sleep, end="\r")
        if sleep > 100:
            writes = 1
            sleep = 0
    Algo(results, z)
