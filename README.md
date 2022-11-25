Capture images from yotube cameras according to the schedule
============================================================
Installation
----------------
- download the code from github
    > git clone git@github.com:igormayachenkov/image-capturer.git
- install python modules
    > apt install python3-pip  
    apt install python3-opencv 
    pip install pafy
    sudo pip install --upgrade youtube_dl
- fix the pafy bug https://github.com/mps-youtube/pafy/issues/287
    > nano /home/igor/.local/lib/python3.10/site-packages/pafy/backend_youtube_dl.py   
    comment like_count, dislike_count
- copy the configuration file to `/etc` dir and correct it according to you tasks
    > cd image-capturer   
    cp image-capturer-config.json /etc   
    nano /etc/image-capturer-config.json
- start under PM2 management
    > pm2 start main.py --name capturer --interpreter python3

Configuration file format
--------------------------
| Parameter                 | Description                                                   |
| :---------------          |:-----------------------------------------------------------   |
| `schedule`                | periodic work settings.                                       |
|   `.periodicity`          | "daily" or "hourly"                                           |
|   `.times`                | times during the loop ("hh:mm" for daily, "mm:ss" for hourly) |
| `sources`                 | list of sources {url, dir}                                    |
| `destination`             | the output dir                                                |
