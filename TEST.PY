# Used to import the webdriver from selenium
from selenium import webdriver


# Get the path of chromedriver which you have install


def startBot(username, password, url):
    try:
        # path = "C:\\Users\\hp\\Downloads\\chromedriver"

        # giving the path of chromedriver to selenium webdriver
        driver = webdriver.Chrome()

        # opening the website  in chrome.
        driver.get(url)

        # find the id or name or class of
        # username by inspecting on username input
        username_field = driver.find_element("id", "session_key")

        # find the password by inspecting on password input
        password_field = driver.find_element("id", "session_password")

        username_field.send_keys(username)
        password_field.send_keys(password)

        # click on submit
        submit_button = driver.find_element(
            "xpath", '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button'
        )
        submit_button.click()
    except Exception as e:
        print(e)


# Driver Code
# Enter below your login credentials
username = "Enter your username"
password = "Enter your password"

# URL of the login page of site
# which you want to automate login.
url = "Enter the URL of login page of website"

# Call the function
startBot(username, password, url)
