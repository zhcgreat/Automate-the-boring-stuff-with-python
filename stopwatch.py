#! python
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print ('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch, press Ctrl-C to quit')
input() # Press enter to start
print ('Started.')
starttime = time.time()
lasttime=starttime
lapNum = 1
# Start tracking the lap time.
try:
    while True:
        input()
        laptime = round(time.time()-lasttime, 2)
        totaltime = round(time.time() - starttime, 2)
        print('Lap #%s: %s (%s)' % (lapNum,totaltime,laptime),end = '')
        lapNum+=1
        lasttime = time.time() #reset the last lap time.
except KeyboardInterrupt:
    # Handle the ctrl-c exception to keep its error message from displaying.
    print ('\nDone.')
