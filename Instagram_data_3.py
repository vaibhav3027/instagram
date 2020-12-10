import os, time, datetime, math, instaloader
import pandas as pd
from dotenv import load_dotenv


load_dotenv()
print("Start")
time.sleep(3)
timer = 100

influencer_file = pd.read_excel("Influencer List/Part3_101Influencers.xlsx")

start_id,end_id = 272,280

print(influencer_file['Account name'][start_id-200])
time.sleep(5)
start_date = "datetime(2017,1,1)"
end_date = "datetime(2018,3,31)"#--------------------------------------CHECK THE DATE
#start_date = "datetime(2017,1,1)"
# end_date = "datetime(2017,12,10)"


for profile_id in range(start_id-200,end_id-200):
    profile_name = influencer_file['Account name'][profile_id][1:]
            
    
    print(profile_id,"\t",profile_name)
    
    folder_id = str(int(math.floor(profile_id / 10.0)) * 10+200)+"_"+ str(int(math.floor(profile_id / 10.0)) * 10+10+200)
    folder_name = f"Instagram_Data_{folder_id}/{profile_name}"
    print(folder_name)
    if not os.path.exists(folder_name.split("/")[0]):os.mkdir(folder_name.split("/")[0])

    command = f'instaloader --post-filter="date_utc >= {start_date} and date_utc <= {end_date}" {profile_name} --no-metadata-json --no-profile-pic --no-video-thumbnails --dirname-pattern={folder_name} --login {os.getenv("INSTAGRAM_USER")} --password {os.getenv("INSTAGRAM_PASSWORD")}'
    os.system(f'cmd /c {command}')              #to close 
    
    time.sleep(timer)
