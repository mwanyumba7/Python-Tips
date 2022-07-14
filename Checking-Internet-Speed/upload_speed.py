import speedtest

up_speed = speedtest.Speedtest()

print(f'{up_speed.upload()/8000000:.2f}mb')
Output:
85.31mb