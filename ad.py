import re

data = input()
if re.match(r'^\d{2}\.\d{2}\.\d{4}$', data):
    if re.match(r'\d{2}\.[0][1-9]\.\d{4}|\d{2}\.[1][0-2]\.\d{4}', data):
        if re.match(r'[0][1-9]\.\d{2}\.\d{4}|[1][0-9]\.\d{2}\.\d{4}|[2][0-9]\.\d{2}\.\d{4}|[3][0]\.04\.\d{4}|[3][0]\.06\.\d{4}|[3][0]\.09\.\d{4}|[3][0]\.11\.\d{4}|[3][0-1]\.01\.\d{4}|[3][0-1]\.03\.\d{4}|[3][0-1]\.05\.\d{4}|[3][0-1]\.07\.\d{4}|[3][0-1]\.08\.\d{4}|[3][0-1]\.10\.\d{4}|[3][0-1]\.12\.\d{4}', data):
            if re.match(r'\d{2}\.02\.d{4}', data):
                if int(data[0:2]) <= 28 and (int(data[-4:]) % 4 != 0 or int(data[-4:0]) % 100 == 0 and int(data[-4:0]) % 400 != 0):
                    print("verno")
                elif int(data[0:2]) <= 29 and (int(data[-4:]) % 4 == 0 and int(data[-4:0]) % 100 != 0 or int(data[-4:0]) % 400 == 0):
                    print("verno")
                else:
                    print("neverno")
            else:
                print("verno")
        else:
            print("neverno")
    else:
        print("neverno")
