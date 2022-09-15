from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF"


browser = webdriver.Edge()
browser.get(URL)

# Returns the title of the Page
print(browser.title)

# Prints the current URL
print(browser.current_url)


# Closes the browser
browser.close()
