import requests
from bs4 import BeautifulSoup
###
# TO ADD
# Information indicating who said what (username with comment...etc)
# Indicate what comments are replies to other comments (can be found in contents list of parent comment)
# Add more information (date posted, how many likes, etc.)
###

# Url to get soup from
url = "https://www.teamblind.com/post/Should-I-tell-girlfriend-my-TC-PuhbYY02"
# Headers with mozilla user agent to convince website I am not a bot
my_headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    # Add more headers as needed
}

session = requests.Session()
response = session.get(url, headers=my_headers)
print("Successful response!" if response.status_code == 200 else "NOT SUCCESSFUL\nError code: %d" % response.status_code)

# Create soup object
soup = BeautifulSoup(response.text, 'html.parser')
comment_group = soup.find_all("p", class_="whitespace-pre-wrap break-words text-sm/5 text-gray-999 md:text-base/6")

comment_count = 0
for comment in comment_group:
    print("Comment: %d" % comment_count)
    print(comment.text)
    print()
    comment_count += 1

# comment_group = soup.find_all('div', class_ = "flex flex-col gap-4") #An "_" is used after class because class is a keyword in python
# comment_list = comment_group[2].contents
# print(len(comment_list))

# for i in range(len(comment_list)):
#     comment = comment_list[i]
#     print(comment.contents[0].contents[1].contents[0].contents[1].contents)