import pyautogui, random, time
#base coordinate settings
x = 500  
y = 300  

# How long the script will run before a break (randomly taken between minimum and max) and maximum run time.
running_interval_min = 15 * 60    #15 minutes
running_interval_max = 45 * 60   #45 minutes
max_run_time = 60 * 60          #1 hour

#How long does the script break for taken randomly between min and max.
break_min = 3 * 60             
break_max = 7 * 60   

time.sleep(5) #how long the script waits before starting - currently 5 seconds.                  
start_time = time.time()
next_break_time = start_time + random.uniform(running_interval_min, running_interval_max)

try:
    while True:
        if time.time() - start_time >= max_run_time: # Check max run time, if reached program ends.
            break

        offset_x = random.randint(-3, 3)                # Random offset for each click x/horizontal
        offset_y = random.randint(-3, 3)                # Random offset for each click y/vertical
        delay = random.uniform(0.2, 0.6)                # Random delay between clicks (0.2s - 0.6s)
        pyautogui.click(x + offset_x, y + offset_y)     # Perform click
        time.sleep(delay)                               # Wait before next click
        if time.time() >= next_break_time:              # Check if it's time for a break
            break_length = random.uniform(break_min, break_max)
            time.sleep(break_length)

            next_break_time = time.time() + random.uniform(running_interval_min, running_interval_max)# Schedule next break

except KeyboardInterrupt:
    print("\nStopped by user.")
