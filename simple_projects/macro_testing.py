from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def monitor_youtube_and_redirect():
    # Initialize the WebDriver (Replace with the path to your ChromeDriver)
    driver = webdriver.Chrome()

    try:
        # Open YouTube
        driver.get("https://www.youtube.com")
        print("YouTube opened.")

        # Wait for the page to load
        time.sleep(5)

        # Find all video links on the page
        video_links = driver.find_elements(By.CSS_SELECTOR, "a#video-title")

        # Add a click interceptor
        for video in video_links:
            ActionChains(driver).move_to_element(video).pause(0.5).perform()
            video.click()
            print("Redirecting to Google...")
            driver.get("https://www.google.com")
            break  # Stop after the first click

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()

# Run the macro
if __name__ == "__main__":
    monitor_youtube_and_redirect()




