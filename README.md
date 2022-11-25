Capture images from yotube cameras according to the schedule
============================================================
Configuration file format
--------------------------
| Parameter                 | Description                                                   |
| :---------------          |:-----------------------------------------------------------   |
| `schedule`                | periodic work settings.                                       |
|   `.periodicity`          | "daily" or "hourly"                                           |
|   `.times`                | times during the loop ("hh:mm" for daily, "mm:ss" for hourly)|
