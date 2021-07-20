
"# copyForm" 
A python tool for copying forms beetwen two pages with different versions of Centreon

Usage:
br = browser("YOUR_URL",page_number=0,item_offset=0) #You can choose the page and item (host or service) where it starts copying
data = br.get_Services_Information()
br.create_Services(data)
br.next_service_page()


Any error will be displayed on terminal waiting for user confirmation for solving it and continuing

Configuration:

The delay for waiting pages until they are ready can be modified in browser.py if your connection is slow

Todo:

Optimize Service creation by checking what have been previously created