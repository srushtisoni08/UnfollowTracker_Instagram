from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import getpass
import time

print("You can only use this if you enter your instagram username. If you try to login with email then this will fail for now. Sorry!!!")
username = input("Enter your instagram username: ")
password= getpass.getpass("Enter your password: ")
driver = webdriver.Firefox()
driver.implicitly_wait(5)

try:
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    user = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    user.send_keys(username)

    User_password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    User_password.send_keys(password)
    User_password.send_keys(Keys.RETURN)

    print("Login attempt successful!")
    
    try:
        profile_icon = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//img[contains(@alt, \"{}'s profile picture\")]".format(username)))
)

        profile_icon.click()
        print("Profile page opened!")

        followers = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/{}/following/')]".format(username)))
)
        print("we found the follower list")

        following = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/{}/following/')]".format(username)))
        )
        print("Following list opened!")

    except Exception as e:
        print(e)
        driver.close()

except Exception as e:
    print("Wrong username or password!")
    driver.close()