import time  # Importing the time module to use the sleep function for delays

# Defining the countdown function that takes time in seconds
def countdown(time_sec):
    # This loop runs until time_sec becomes 0
    while time_sec:
        # divmod divides time_sec by 60 and returns minutes and seconds
        mins, secs = divmod(time_sec, 60)

        # Formatting the time as MM:SS using string formatting
        # {:02d} ensures two digits with leading zeros if needed (e.g., 01, 02...)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        

        # Print the formatted time on the same line using carriage return '\r'
        # end='\r' ensures it doesn't move to the next line but rewrites the current line
        print(timeformat, end='\r')

        # Pause the program for 1 second
        time.sleep(1)

        # Decrease the time by 1 second
        time_sec -= 1

    # When the loop ends (i.e., countdown is over), print 'Stop'
    print("Stop")

# Calling the function with 10 seconds as input
countdown(10)
