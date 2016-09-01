# roomscraper

Scapes all real estate listing photos for Houston, TX from Realtor.com. Because you never know when you might need five thousand photos of empty rooms.

To run your own crawl:
``` bash
git clone https://github.com/mouse-reeve/roomscraper.git
cd roomscraper
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
scrapy crawl realtor -o test.json
```
