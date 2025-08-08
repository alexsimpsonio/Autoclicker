
# Autoclicker
A customisable AutoClicker with randomness of timing, breaks and click position.
If you choose to use this to cheat at videogames, do this at your own risk ;).


Getting the right co-ordinates:
Run the co-ordinates script.
It waits 5 seconds before printing out the mouse co-ordinates wherever you are running it.
use this to find your base X and Y for the below.


There are some variables to change:

1) Set your base x and y co-ordinates. This is where you want this clicker to click.

2) You can change:

   Code: running_interval_min = 15 * 60, running_interval_max = 45 * 60, max_run_time = 60 * 60    

   Exp:  max_run_time is a counter, once reached the AutoClicker stops. EG if you want to run it for two hours change max_run_time to 120 * 60.
   The intervals determine how long it will run without breaks. The above means that it will run somehwere between 15 and 45 minutes before taking a break.
   It takes a break then continues to run until max time is reached.

   Code: break_min = 3 * 60 , break_max = 7 * 60 , time.sleep(5)

   Exp: These determine the random break length discussed above, the min and max are the thresholds for how long a break is taken during the run time.
   The sleep gives you some time before the script runs.

   Code: offset_x = random.randint(-3, 3), offset_y = random.randint(-3, 3), delay = random.uniform(0.2, 0.6)

   Exp: offsets determine how much the x and y co-ordinate is changed each click intended to mimic human inconsistencies. Adjust to your needs, sometimes they might be too large.
   delay decides how long between each click, the click is randomly selected to be between every 0.2 seconds and 0.6 seconds. Adjust to your needs, but keep a range.
   

                 
   
   
