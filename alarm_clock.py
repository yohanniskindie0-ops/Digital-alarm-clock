import time

def digital_clock():
    print("Digital Alarm Clock")
    alarm = input("Set alarm time (HH:MM): ")
    
    while True:
        current = time.strftime("%H:%M")
        print(f"Current time: {current}", end="\r")
        
        if current == alarm:
            print("\n⏰ ALARM! Wake up!")
            break
        
        time.sleep(30)

digital_clock()
