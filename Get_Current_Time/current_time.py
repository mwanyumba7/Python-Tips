# First we import the module as below 
from datetime import datetime

# We then query for the time and use the strftime() method to format time to the desired output.
time_now = datetime.now().strftime('%H:%M:%S')

# Printing the time now 
print(f'The time now is {time_now}')

# Output
The time now is 18:33:29

    