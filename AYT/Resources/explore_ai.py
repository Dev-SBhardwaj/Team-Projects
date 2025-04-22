from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Set the path to your chromedriver executable
chromedriver_path = 'path/to/chromedriver'

# Set the topic you want to search for
topic = "tech topic"

# Start the Selenium WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# Navigate to the ExploreAI website
driver.get("https://exploreai.vercel.app/")

# Find the search input element and enter the topic
search_input = driver.find_element(By.XPATH, "//input[@name='search']")
search_input.send_keys(topic)
search_input.send_keys(Keys.ENTER)

# Wait for the results to load
driver.implicitly_wait(10)

# Find the generated video element and get the video URL
video_element = driver.find_element(By.XPATH, "//video[@class='video-js']")
video_url = video_element.get_attribute("src")

# Print the video URL
print("Generated video URL:", video_url)

# Close the browser
driver.quit()
