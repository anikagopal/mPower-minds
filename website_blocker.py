from time import *  
from datetime import *  
  
host_path = r"C:\Windows\System32\drivers\etc\hosts" 
redirect = "127.0.0.1"  
websites = ["www.facebook.com", "https://www.facebook.com","www.instagram.com", "https://www.instagram.com", "https://www.youtube.com", "www.youtube.com", "https://www.tiktok.com", "www.tiktok.com", "https://www.twitter.com", "www.twitter.com", "https://www.pinterest.com", "www.pinterest.com"]  
  
while True:  
    if datetime(datetime.now().year,datetime.now().month,datetime.now().day,8)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,20):  
        with open(host_path,"r+") as fileptr:  
            content = fileptr.read()  
            for website in websites:  
                if website in content:  
                    pass  
                else:  
                    fileptr.write(redirect+"        "+website+"\n")  
    else:  
        with open(host_path,'r+') as file:  
            content = file.readlines();  
            file.seek(0)  
            for line in content:  
                if not any(website in line for website in websites):  
                    file.write(line)  
            file.truncate()  
    sleep(5)  
