import speedtest

d_speed = speedtest.Speedtest()

print(f'{d_speed.download()/8000000:.2f}mb')
Output:
213.78mb
