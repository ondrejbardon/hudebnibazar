# hudebnibazar.cz scraper

Script for scraping hudebnibazar.cz on regular basis in cronjob manner. Matches newly appeared gear based on the keywords, checks if given advertisement has already been processed and pushes notification through Spontit.

## How to use

 - Setup SPONTIT_USERNAME and SPONTIT_SECRET_KEY based on your user
 - Install requirements `pip3 install -r requirements.txt`
 - Run manually `/usr/local/bin/python3 hudebnibazar.py`
 - Configure regular job `*/1 * * * * cd /Users/john.doe/repositories/hudebnibazar && /usr/local/bin/python3 hudebnibazar.py >/tmp/stdout.log 2>/tmp/stderr.log`

## TODO

 - configure as AWS lambda cron function
 - exchange spontit with other push provider