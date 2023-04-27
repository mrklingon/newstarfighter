def shoSky(crn: number):
    for index in range(5):
        for index2 in range(5):
            led.plot_brightness(index2, index, 12 * cosmos[crn + (index2 + 100 * 0)])
def findDir():
    global dir2
    dir2 = 0
    if input.acceleration(Dimension.X) < -300:
        dir2 = 4
    else:
        if input.acceleration(Dimension.Y) > 300:
            dir2 = 3
        if input.acceleration(Dimension.Y) < -500:
            dir2 = 1
    if input.acceleration(Dimension.X) > 300:
        dir2 = 2
    return dir2
d = 0
dir2 = 0
cosmos: List[number] = []
alt = 2
for index3 in range(5 * 100):
    if 40 < randint(0, 100):
        cosmos.append(randint(2, 6))
    else:
        cosmos.append(0)
corner = 0

def on_forever():
    global d, alt
    led.plot(2, alt)
    basic.pause(100)
    led.unplot(2, alt)
    shoSky(corner)
    d = findDir()
    if d == 1:
        alt += -1
        if alt < 0:
            alt = 0
    if d == 3:
        alt += 1
        if alt > 4:
            alt = 4
basic.forever(on_forever)
