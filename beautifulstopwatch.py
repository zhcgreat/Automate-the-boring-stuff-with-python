#! python
# stopwatch.py - A simple stopwatch program.

import time, pyperclip

# Display the program's instructions.
print ('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch, press Ctrl-C to quit')
input() # Press enter to start
print ('Started.')
starttime = time.time()
lasttime=starttime
lapNum = 1
# Start tracking the lap time.
results = []
try:
    while True:
        input()
        laptime = round(time.time()-lasttime, 2)
        totaltime = round(time.time() - starttime, 2)
        result = 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2),str(totaltime).rjust(5),str(laptime).rjust(5))
        print (result, end='')
        lapNum+=1
        lasttime = time.time() #reset the last lap time.
        results.append(result)
except KeyboardInterrupt:
    # Handle the ctrl-c exception to keep its error message from displaying.
    print ('\nDone.')
    text = '\n'.join(results)
    pyperclip.copy(text)
