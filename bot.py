from selenium import webdriver
import os, time, random
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from selenium.webdriver.common.keys import Keys



def banner():
    banner_logo = r"""

    __  _______ ________  ____________     ___        ________  ________    ____     __________
   /  |/  / __ /_  __/ / / / ____/ __ \   ( _ )      / ____/ / / /  _/ /   / __ \   /  _/ ____/
  / /|_/ / / / // / / /_/ / __/ / /_/ /  / __ \/|   / /   / /_/ // // /   / / / /   / // / __
 / /  / / /_/ // / / __  / /___/ _, _/  / /_/  <   / /___/ __  _/ // /___/ /_/ /  _/ // /_/ /
/_/  /_/\____//_/ /_/ /_/_____/_/ |_|   \____/\/   \____/_/ /_/___/_____/_____/  /___/\____/

                        ____  __  __           __   ______
                       / __ )/ / / ____ ______/ /__/ ________  _  __
                      / __  / /_/ / __ `/ ___/ //_/ /_  / __ \| |/_/
                     / /_/ / __  / /_/ / /__/ ,< / __/ / /_/ _>  <
                    /_____/_/ /_/\__,_/\___/_/|_/_/    \____/_/|_|


"""
    print(banner_logo)

class Add_photo:

    def __init__(self, username, password):
        chrome_options = Options()
        mobile_emulation = {"deviceMetrics": { "width": 460, "height": 600, "pixelRatio": 3.0 },"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
        #chrome_options.add_experimental_option('androidPackage','com.android.chrome')
        #chrome_options.add_argument(f'Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36')
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.driver = webdriver.Chrome(options=chrome_options, executable_path=r'./chromedriver')

        self.username = username
        self.password = password

        self.driver.get("https://instagram.com")
        time.sleep(4)
        self.LogIn()


    def LogIn(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button').click()
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]').click()
        pyautogui.click(x=100,y=100)
        pyautogui.doubleClick(x=200,y=100)
        time.sleep(0.5)
        pyautogui.doubleClick(x=200,y=100)
        time.sleep(0.5)
        pyautogui.doubleClick(x=200,y=100)

        time.sleep(10)


class Create_Account:

    def __init__(self,email_ig,password_ig,user_ig):
        self.email_ig = email_ig
        self.password_ig = password_ig
        self.user_ig = user_ig
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get("https://www.instagram.com/accounts/emailsignup/")
        time.sleep(4)
        self.Signin()

    def Signin(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.email_ig)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input').send_keys(self.user_ig)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input').send_keys(self.user_ig)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input').send_keys(self.password_ig)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button').click()
        time.sleep(15)



class Comment_Account:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get("https://www.instagram.com/")
        time.sleep(4)
        self.LogIn()

    def LogIn(self):
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click()
        time.sleep(3)


class Send_Direct:
    def __init__(self,username,password,msg):
        self.username = username
        self.password = password
        self.msg = msg
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get("https://instagram.com/")
        time.sleep(4)
        self.LogIn()

    def LogIn(self):
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click()
        time.sleep(3)
        self.GetName()

    def GetName(self):
        username_checked = open("username_checked.txt").readlines()
        username_used = open("username_used.txt").readlines()
        usr_new = []
        for i in range(len(username_checked)):
            username_checked[i] = username_checked[i].strip()
            a = 0
            for k in range(len(username_used)):
                username_used[k] = username_used[k].strip()
                if username_checked[i] != username_used[k]:
                    a += 0
                else:
                    a += 1
            if a==0:
                usr_new.append(username_checked[i])
        usr_new = list(dict.fromkeys(usr_new))
        self.driver.get("https://instagram.com/direct/inbox/")
        time.sleep(4)
        self.driver.find_element_by_xpath('//button[text()="Not Now"]').click()
        for i in range(len(usr_new)):
            self.driver.get("https://www.instagram.com/p/CFMOHW8qbOa/")
            time.sleep(2)
            self.Collect_users(usr_new[i])
            with open("username_used.txt","a") as wr:
                wr.write(usr_new[i]+"\n")

    def Collect_users(self,user_msg):
        print(user_msg)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div[1]/div/div').click()
        k = self.driver.find_elements_by_name("queryBox")
        k[0].send_keys(user_msg)
        time.sleep(2)
        #self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]').click()
        time.sleep(1)

        self.driver.get("https://instagram.com/direct/inbox/")
        time.sleep(2)
        #self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(Keys.CONTROL,'v')
        self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]').click()
        time.sleep(1)



class Gain_Followers:
    def __init__(self,username,password,user):
        self.username = username
        self.password = password
        self.user = user
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get("https://instagram.com/")
        time.sleep(4)
        self.LogIn()

    def LogIn(self):
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]").click()
        time.sleep(3)
        self.User_Followes()

    def User_Followes(self):
        self.driver.get("https://instagram.com/"+self.user)
        followeslink = self.driver.find_element_by_css_selector('ul li a')
        followeslink.click()
        time.sleep(2)
        followesList = self.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersList = len(followesList.find_elements_by_css_selector('li'))

        followesList.click()
        action_chains = webdriver.ActionChains(self.driver)
        while (numberOfFollowersList < 300):
            action_chains.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersList = len(followesList.find_elements_by_css_selector('li'))
            print(numberOfFollowersList)

        followers = []
        for user_to_follow in followesList.find_elements_by_css_selector('li'):
            userlink = user_to_follow.find_element_by_css_selector('a').get_attribute('href')
            print(userlink[27:-1])
            followers.append(userlink)
            with open("username_checked.txt","a") as wr:
                wr.write(userlink[27:-1])


def choose_method():
    print("Choose Method to Use:")
    print("[1]:>Create Account")
    print("[2]:>Add Image")
    print("[3]:>Add Story")
    print("[4]:>Comment")
    print("[5]:>Send Direct")
    print("[6]:>Search Account")
    print("[7]:>Add Users List")
    chs = int(input("[*]:>"))
    eml_rd = open("email_pass.txt").readlines()
    email = []
    passwd = []
    username = []
    acc = eml_rd
    for i in range(len(eml_rd)):
        acc[i] = eml_rd[i].strip()
        space = acc[i].index(" ")
        email.append(acc[i][:space])
        space2 = acc[i][space+4:].index(" ")
        passwd.append(acc[i][space+4:space+4+space2])
        username.append(acc[i][space+8+space2:])
    if chs == 1:
        print("Which account do you want to create?")
        for i in range(len(email)):
            print("["+str(i+1)+"]:>"+email[i])
        print("["+str(len(email))+"]:>All")
        account = int(input("[*]:>")) +1
        if account == len(email):
            for i in range(len(email)):
                try:
                    print("Try to create account:"+email[i]+", username:"+username[i]+" with password:"+passwd[i]+" ...")
                    create_user = Create_Account(email[i],passwd[i],username[i])
                    print("Account "+email[i]+" created!\n")
                except:
                    print("Something goes wrong... Search for next user....\n")
        else:
            try:
                print("Try to create account:"+email[account]+",username:"+username[account]+" with password:"+passwd[account]+" ...")
                create_user = Create_Account(email[account],passwd[account],username[account])
                print("Account "+email[account]+" created!\n")

            except:
                print("Something goes wrong.... Aborting...")
    elif chs == 2:
        print("Do you want to change text file? Yes/no")
        txt_file = input("[*]:>").lower()
        if txt_file == "y" or txt_file == "yes":
            print("Modify txt file for instagram upload")
            opera = input("[+] ")
            with open("txt_file.txt","w") as wr:
                wr.write(opera)
        print("Select account/s to use")
        for i in range(len(username)):
            print("["+str(i+1)+"]:>"+username[i])
        print("["+str(len(username))+"]:>All")
        email_choose = int(input("[*]:>")) +1
        if email_choose == len(email):
            print("Ok! Collecting all accounts...")
            for i in range(len(email)):
                print("Add picture with account:"+username[i])
                print("Try to Log In.........")
                try:
                    pictures_add = Add_photo(username[i],passwd[i])
                    print("Pictures added correctly\n")
                except:
                    print("Something goes wrong... Search for another username/passwd......\n")
            print("Exec ended!\nBye!!!")

        else:
            print("Add picture at:"+username[email_choose]+"........")
            print("Try to Log In........")
            try:
                pictures_add = Add_photo(username[email_choose],passwd[email_choose])
                print("Picture added correctly!\n")
            except:
                print("Something goes wrong... check username/email/passwd to be sure to Log In correctly\n")
            print("Exec ended!\nBye!!!")

    elif chs == 3:
        print("COOMING SOON\n")

    elif chs == 4:
        print("COOMING SOON\n")

    elif chs == 5:
        print("Which account do you want to use?")
        for i in range(len(username)):
            print("["+str(i+1)+"]:>"+username[i])
        print("["+str(len(username))+"]:>All")
        account = int(input("[*]:>")) +1
        print("Do you want to change message file?",end="")
        msg_c = input("(Yes/No/Show)").lower()
        if msg_c == "y" or msg_c == "yes":
            chng = input("[*]:> ")
            with open("message.txt","w") as wr:
                wr.write(chng)
            print("Message changed correctly!")
        elif msg_c == "s" or msg_c == "Show":
            print(open("message.txt").read())

        if os.path.exists("message.txt") != True:
            print("Message file doesn't exist...")
            with open("message.txt","w") as wr:
                wr.write(input("[*]:>"))
        if account == len(username):
            for i in range(len(username)):
                print("Collecting all accounts.....")
                print("Sending message with account "+str(username[i])+" ...")
                try:
                    msg = open("message.txt").read()
                    sending_message = Send_Direct(username[i],passwd[i],msg)
                    print("Message correctly sended!\n")
                except:
                    print("Enable to Log In... Search for another username/passwd......\n")
                print("Exec ended!\nBye!!!")
        else:
            print("Sending message at:"+username[account]+"........")
            print("Try to Log In........")
            try:
                msg = open("message.txt").read()
                sending_message = Send_Direct(username[account],passwd[account],msg)
                print("Message correctly sended!\n")
            except:
                print("Something goes wrong... check username/email/passwd to be sure to Log In correctly\n")
            print("Exec ended!\nBye!!!")
    elif chs == 6:
        print("Which account do you want to use?")
        for i in range(len(username)):
            print("["+str(i+1)+"]:>"+username[i])
        print("["+str(len(username))+"]:>All")
        account = int(input("[*]:>")) + 1

    elif chs == 7:
        print("Choose account to gain followers:")
        acc_follw = input("[*]:>")
        print("Which account do you want to use?")
        for i in range(len(username)):
            print("["+str(i+1)+"]:>"+username[i])
        account = int(input("[*]:>")) +1
        print("Gain followers from "+acc_follw+" with user "+username[account])
        print("Try to Log In..........")
        #try:
        gain_foll = Gain_Followers(username[account],passwd[account],acc_follw)
        print("Followes added to list!")
        #except:
        print("Something goes wrong... check username/email/passwd to be sure to Log In correctly\n")
        print("Exec ended!\nBye!!!")




if __name__ == "__main__":
    banner()
    choose_method()
