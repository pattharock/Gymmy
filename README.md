# Gymmy

A selenium application to automate the slot-booking process for gyms @HKU.

## Running locally
Clone the repository, then add a config file `config.py` in the repo.

Add the following data

`EMAIL = "your google address"`

`UNIVERSITY_EMAIL = "your @hku.hk address"`

`NAME = "full name as on university ID"`

`UNO = "your universsity Number as on university ID"`

`GYM_CHOICE = "one of Campus/QRW/Stanley"`

Following this, head over to the terminal and run the command `crontab -e` to add the script to your cronjobs.
1. add the time-scheduler (see https://crontab.guru)
2. add the location of your python install (virtual environment)
3. add the location of scipt

You're all set. 
