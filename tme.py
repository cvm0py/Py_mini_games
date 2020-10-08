import time
sec1 = int(time.strftime("%S",time.localtime()))
min1 = int(time.strftime("%M",time.localtime()))


print("{0}:{1}".format(min1, sec1))
time.sleep(35.7)
min2 = int(time.strftime("%M",time.localtime()))
sec2 = int(time.strftime("%S",time.localtime()))
print("{0}:{1}".format(min2, sec2))

if min1 != min2:
    sec1 = sec1 - 60
diff = sec2 - sec1
print(diff)
