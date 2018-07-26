#browser bomb by Jack
import webbrowser
import time

main_logo = '''===========[python3 edition]=========
   ___         ___            _      
  | _ )  ___  | _ ) ___ _ __ | |__   
  | _ \ |___| | _ \/ _ \ '  \| '_ \  
  |___/       |___/\___/_|_|_|_.__/  
                                     
        Browser Bomb By Jack
               [V1.0.7]              
        [github.com/jackthebaptist]      
====================================='''

print(main_logo)


website = input("[?] What site do you want to use?:")
while True:
    try:
        num = int(input("[?]How many times should your site open?: "))
    except ValueError:
        print("[-] Sorry, I didn't understand that.")
        continue
    else:
        break
time.sleep(2)
for _ in range(num):
        webbrowser.open('http://{}'.format(website))
        time.sleep(0.4)

