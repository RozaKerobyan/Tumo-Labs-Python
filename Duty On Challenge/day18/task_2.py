def time_converter(t):
    period = t[-2:]
    hour, minute, second = map(int, t[:-3].split(':'))

    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0
    
    s_res = f"{hour:02}:{minute:02}:{second:02}"
    print(s_res)

if __name__ == '__main__':
    time = input("Enter time in 12-hour format (hh:mm:ss AM/PM): ")
    time_converter(time)

