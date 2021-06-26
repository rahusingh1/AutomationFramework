import pendulum

x = pendulum.now()
x = pendulum.now().strftime("%d-%m-%Y::%H:%M:%S")
print(x)


currTime = pendulum.now().strftime("%d-%m-%Y::%H:%M:%S")
screenShotName = "screenshot_"+currTime
print(screenShotName)
