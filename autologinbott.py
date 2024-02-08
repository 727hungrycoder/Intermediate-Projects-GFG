# Used to import the webdriver from selenium
from selenium import webdriver


# Get the path of chromedriver which you have install


def startBot(username, password, url):
    try:
        # path = r"C:\\Users\\Raj\\Downloads\\chromedriver_win32\\chromedriver.exe"

        # giving the path of chromedriver to selenium webdriver
        driver = webdriver.Chrome()

        # opening the website in chrome.
        driver.get(url)

        # find the id or name or class of
        # username by inspecting on username input
        # Find the username and password fields by their IDs
        username_field = driver.find_element("id", "session_key")
        password_field = driver.find_element("id", "session_password")

        # Enter the username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click on the submit button
        submit_button = driver.find_element(
            "xpath", '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button'
        )
        submit_button.click()
        print("Login Successful")

    except Exception as e:
        print(e)
        # Close the WebDriver session
        # driver.quit()


# Enter below your login credentials
username = "727.ankita@gmail.com"
password = "ankita22@"

# URL of the login page of site<button class="btn-md btn-primary flex-shrink-0 cursor-pointer
url = "https://www.linkedin.com/"

# Call the function
startBot(username, password, url)
