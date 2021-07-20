
"# copyForm" 
A python tool for copying forms beetwen two pages with different versions of Centreon

Usage:
br = browser("YOU_URL",page_number=0,item_offset=0) You can choose the page and item (host or service) where it starts copying

Any error will be displayed on terminal waiting for user confirmation for solving it and continuing

Configuration:

The delay for waiting pages until they are ready can be modified in browser.py if your connection is slow

Todo:

Optimize Service creation by checking what have been previously created