while True:
    tp = int(input('1.hour to seconds\n2.seconds to hour\n1 or 2: '))
    if tp == 1:
        hr = int(input('hours: '))
        min = int(input('minutes: '))
        sec = int(input('seconds: '))
        secs = (hr * 3600) + (min * 60) + sec
        print(secs, 'seconds')
        break
    elif tp == 2:
        secs = int(input('seconds: '))
        hr = int(secs / 3600)
        min = int((secs - (hr * 3600)) / 60)
        sec = int(((secs - (hr * 3600) - min * 60) / 60) * 60)
        print(hr,':', min,':', sec)
        break
    else:
        print('you have to Enter "1" or "2"')
        continue
