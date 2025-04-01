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

def get_follower(a_names, b_names):

    only_u_follow = list(set(b_names) - set(a_names))
    only_they_follow = list(set(a_names) - set(b_names))

    return only_u_follow, only_they_follow

def fetch_follower():
    return [user.text.strip() for user in driver.find_elements(By.XPATH, "//span[contains(@class, '_ap3a')]") if user.text.strip()]

def fetch_following_people():
    return [user.text.strip() for user in driver.find_elements(By.XPATH, "//span[contains(@class, '_ap3a _aaco _aacw _aacx _aad7 _aade')]") if user.text.strip()]

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
    EC.element_to_be_clickable((By.XPATH,"//a[contains(@href, '/{}/followers/')]".format(username) ))
)
        driver.execute_script("arguments[0].scrollIntoView();", followers)
        time.sleep(1)  # Small delay before clicking
        driver.execute_script("arguments[0].click();", followers)
        print("Followers list opened!")
        # Wait for the followers list to load
        number_of_follower = int(followers.text.replace("followers","").strip())
        print(f"number of followers:{ number_of_follower}")

        follower_list = []
        # Extract All Follower Names
        follower_list = fetch_follower()
        while len(follower_list) != (number_of_follower):
            follower_list = fetch_follower()
            print(f"fetching....{len(follower_list)}")
            time.sleep(5)
            if len(follower_list) == (number_of_follower) or len(follower_list) > (number_of_follower):
                break

        print("follower list is complete")
        time.sleep(1)

        close_button = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,"//div[@class = '_abm0']")))
        close_button.click()

        following = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/{}/following/')]".format(username)))
        )
        number_of_following = int(following.text.replace("following","").strip())
        driver.execute_script("arguments[0].scrollIntoView();", following)
        time.sleep(1)  # Small delay before clicking
        driver.execute_script("arguments[0].click();", following)
        print("Following list opened!")

        following_list = []
        print(f"number of following: {number_of_following}")
        following_list = fetch_following_people()
        
        while len(following_list) < number_of_following:
            following_list = fetch_following_people()
            print(f"fetching...{len(following_list)}")
            time.sleep(5)
            if len(following_list) > (number_of_following-10):
                break

        print("following list complete")
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_abm0']"))).click()
        u_follow , they_follow = get_follower(follower_list,following_list)

        print("Insta id only followed by you they do not follow back are: ")
        for i in u_follow:
            print(i)

        print("\nInsta id you do not follow back are: ")
        for j in they_follow:
            print(j)

    except Exception as e:
        print(e)

except Exception as e:
    print("Wrong username or password!")
    driver.close()