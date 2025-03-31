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
follow = "followers"
f = "following"
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
        for i in range(number_of_follower):
            follower = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"//span[@class='_ap3a _aaco _aacw _aacx _aad7 _aade']")))
            print(follower.text)
            
        following = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/{}/following/')]".format(username)))
        )
        driver.execute_script("arguments[0].scrollIntoView();", following)
        time.sleep(1)  # Small delay before clicking
        driver.execute_script("arguments[0].click();", following)
        print("Following list opened!")
# "x1rg5ohu
    except Exception as e:
        print(e)

except Exception as e:
    print("Wrong username or password!")
    driver.close()
#    <div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1"><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"><div class="x1rg5ohu"><span class="xjp7ctv"><div><a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd" href="/krishita27_/?next=%2F" role="link" tabindex="0"><div class="x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1"><span class="_ap3a _aaco _aacw _aacx _aad7 _aade" dir="auto">krishita27_</span></div></div></a></div></span></div></div><span class="x1lliihq x1plvlek xryxfnj x1n2onr6 x1ji0vk5 x18bv5gf x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x1roi4f4 x10wh9bi x1wdrske x8viiok x18hxmgj" style="----base-line-clamp-line-height: 18px; --lineHeight: 18px;" dir="auto"><span class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft">Krishita</span></span></div>