def clock(hr,m):
    if hr == 12:
        hr = 0
    if m ==60:
        m = 0
    hour_angle = 0.5 *(hr*60 +m)
    minute_angle = 8 * m

    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle,angle)

    return(angle)



def main():
    hr = int(input("Please enter the hour: "))
    minute = int(input("Please enter the minute: "))
    print(clock(hr,minute))

main()
