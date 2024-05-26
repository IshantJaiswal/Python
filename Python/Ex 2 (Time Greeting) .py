import time
timestamp = time.strftime('%H,%M,%S')
print(timestamp) 
timestamp = time.strftime('%H')
print(timestamp) 
timestamp = time.strftime('%M')
print(timestamp) 
timestamp = time.strftime('%S')
print("time",time)

if(time>6 & time<12):
    print("Good Morning sir")

elif(time<13 & time>16):
    print("Good Afternoon sir")
    
else:
    time('18-24')
    print("Good night")