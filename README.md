### Team Blind Forum Scraper
## Web scraper to get around login requirement to view forums. This scraper gets all the comments that are hidden by the login prompt.
# When perusing the web about proprietary trading shops in the Chicagoland area I found a website called team blind used mostly by SWEs at tech/ trading firms. Upon trying to read a thread I was (annoyingly) prompted to sign up for their website and a curtain was put up to block me from reading the comments responding to the thread.

# I probably would have signed up if I didn't notice that team blind renders all the information I need before rendering the curtain. My first attempt was to throttle my network connection to 15 kbps a second to load just the forum and comments before the curtain was rendered, then cut my connection off to hopefully keep what I rendered and nothing more. This did not work because the page routed me to a network connection error page upon cutting my connection (duh). 

# I then looked through the client side HTML in my browser and discovered the text I wanted embeddded within a handful of div elements. However, I wouldn't need to seep through the divs to get to the text if I knew the class name associated with the elements containing comment text.

# Therefore, I used python requests to send a get request for the forum's HTML (with a modified user-agent to circumvent bot detection) and used the BeautifulSoup4 package to scrape the HTML response for <p> tags with the class="whitespace-pre-wrap break-words text-sm/5 text-gray-999 md:text-base/6". 

# Current state has basic functionality
# Output is sent to the terminal
# Further updates will organize commnets to clearly indicate what comments are replies to other comments along with dates posted and usernames.
