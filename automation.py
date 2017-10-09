from selenium import webdriver
import time

#path for chromedriver
pathChromedriver = 'C:\\Users\\Luis\\PycharmProjects\\challengeQAAutomation\\chromedriver.exe'
browser = webdriver.Chrome(pathChromedriver)
browser.get('https://www.olx.pt')

def newAdvertNotLogged():

    #newAdvert
    browser.find_element_by_xpath('//*[@id="postNewAdLink"]/span').click()
    time.sleep(1)

    #titleAdvert
    browser.find_element_by_xpath('//*[@id="add-title"]').send_keys('My first Advert')

    #descriptionAdvert
    browser.find_element_by_xpath('//*[@id="add-description"]').send_keys('This is my first advert')

    #categoryAdvert
    browser.find_element_by_xpath('//*[@id="targetrenderSelect1-0"]/dt/a').click()
    time.sleep(2)

    #defineCategoryAdvert
    browser.find_element_by_xpath('//*[@id="cat-99"]').click()
    time.sleep(2)

    #subCategoryAdvert
    browser.find_element_by_xpath('//*[@id="category-99"]/div[2]/div[2]/div/ul/li[1]/a/span[1]').click()
    time.sleep(2)

    #brand
    browser.find_element_by_xpath('//*[@id="targetparam1147"]/dt/a').click()
    time.sleep(1)

    #brandSelect
    browser.find_element_by_xpath('//*[@id="targetparam1147"]/dd/ul/li[2]/a').click()

    # close cookiesBar
    browser.find_element_by_xpath('//*[@id="cookiesBar"]/a').click()
    time.sleep(3)

    #state
    browser.find_element_by_xpath('//*[@id="targetparam1143"]/dt/a').click()

    #stateSelect
    browser.find_element_by_xpath('//*[@id="targetparam1143"]/dd/ul/li[2]/a').click()

    #person
    browser.find_element_by_xpath('//*[@id="add-person"]').send_keys('John Snow')

    #email
    browser.find_element_by_xpath('//*[@id="add-email"]').send_keys('qachallengept@gmail.com')

    #price
    browser.find_element_by_xpath('//*[@id="parameter-div-price"]/div[3]/div/div[1]/p[1]/input').send_keys('10')

    #typeA
    browser.find_element_by_xpath('//*[@id="targetid_private_business"]/dt/a').click()

    #typeSelect
    browser.find_element_by_xpath('//*[@id="targetid_private_business"]/dd/ul/li[3]/a').click()

    #address
    browser.find_element_by_xpath('//*[@id="mapAddress"]').send_keys('Benfica, Lisboa, Lisboa')
    time.sleep(1)

    browser.find_element_by_xpath('//*[contains(@id,"suggested-city-")]').click()

    #approve
    browser.find_element_by_xpath('//*[@id="accept"]/div/div[2]/div/label').click()
    time.sleep(1)

    #save
    browser.find_element_by_xpath('//*[@id="save"]').click()

    #screeShot
    browser.save_screenshot('newAdvertNotLogged.png')
    time.sleep(5)
    browser.quit()

def registerNewUser():

    #closePopUp
    browser.find_element_by_xpath('//*[@id="hide_homepage_video"]').click()
    time.sleep(1)

    #Login
    browser.find_element_by_xpath('//*[@id="topLoginLink"]/div').click()

    #register
    browser.find_element_by_xpath('//*[@id="register_tab"]').click()

    #email
    browser.find_element_by_xpath('//*[@id="userEmailRegister"]').send_keys('qachallengept@gmail.com')

    #password
    browser.find_element_by_xpath('//*[@id="userPassRegister"]').send_keys('initial1234')

    #terms
    browser.find_element_by_xpath('//*[@id="registerForm"]/div[3]/div/div/label[1]').click()

    #finishRegister
    browser.find_element_by_xpath('//*[@id="button_register"]').click()

    #screenShot
    browser.save_screenshot('registerNewUser.png')
    time.sleep(5)
    browser.quit()

def activateNewUser():

    #closePopUp
    browser.find_element_by_xpath('//*[@id="hide_homepage_video"]').click()
    time.sleep(1)

    #login
    browser.find_element_by_xpath('//*[@id="topLoginLink"]/div').click()

    #register
    browser.find_element_by_xpath('//*[@id="register_tab"]').click()

    #email
    browser.find_element_by_xpath('//*[@id="userEmailRegister"]').send_keys('qachallengept@gmail.com')

    #password
    browser.find_element_by_xpath('//*[@id="userPassRegister"]').send_keys('inicial1234')

    #terms
    browser.find_element_by_xpath('//*[@id="registerForm"]/div[3]/div/div/label[1]').click()

    #finishRegister
    browser.find_element_by_xpath('//*[@id="button_register"]').click()

    #emailAccess
    browser.find_element_by_xpath('//*[@id="body-container"]/div/div/div[2]/div[1]/a/span/span').click()

    #signInEmail
    browser.find_element_by_xpath('/html/body/nav/div/a[2]').click()

    #email1
    browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys('qachallengept@gmail.com')

    #nextStep
    browser.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
    time.sleep(2)

    #enterPassword
    browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('inicial1234')

    #nextStep2
    browser.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
    time.sleep(10)

    #openEmail
    browser.find_element_by_xpath('//*[@id=":37"]/span').click()

    #activate
    browser.find_element_by_xpath('//*[starts-with(@id,"m_") and contains(@id,"Table_01"])').click()

    browser.find_element_by_tag_name('')

    #screenShot
    browser.save_screenshot('activateNewUser.png')
    browser.quit()

def newAdvert():

    #closePopUp
    browser.find_element_by_xpath('//*[@id="hide_homepage_video"]').click()
    time.sleep(1)

    #login
    browser.find_element_by_xpath('//*[@id="topLoginLink"]/div').click()

    #insert user
    browser.find_element_by_xpath('//*[@id="userEmail"]').send_keys('qachallengept@gmail.com')

    #insert password
    browser.find_element_by_xpath('//*[@id="userPass"]').send_keys('inicial1234')

    #submit login
    browser.find_element_by_xpath('//*[@id="se_userLogin"]').click()

    #newAdvert
    browser.find_element_by_xpath('//*[@id="postNewAdLink"]/span').click()
    time.sleep(3)

    #close fancy-box
    browser.find_element_by_xpath('//*[@id="fancybox-close"]').click()
    time.sleep(3)

    #close fancy-box
    browser.find_element_by_xpath('//*[@id="fancybox-close"]').click()
    time.sleep(3)

    #close cookiesBar
    browser.find_element_by_xpath('//*[@id="cookiesBar"]/a').click()
    time.sleep(3)

    #titleAdvert
    browser.find_element_by_xpath('//*[@id="add-title"]').send_keys('My first Advert')

    #descriptionAdvert
    browser.find_element_by_xpath('//*[@id="add-description"]').send_keys('This is my first advert')

    #categoryAdvert
    browser.find_element_by_xpath('//*[@id="targetrenderSelect1-0"]/dt/a').click()
    time.sleep(2)

    #defineCategoryAdvert
    browser.find_element_by_xpath('//*[@id="cat-99"]').click()
    time.sleep(2)

    #subCategoryAdvert
    browser.find_element_by_xpath('//*[@id="category-99"]/div[2]/div[2]/div/ul/li[1]/a/span[1]').click()
    time.sleep(2)

    #close fancy - box
    browser.find_element_by_xpath('//*[@id="fancybox-close"]').click()
    time.sleep(6)

    #brand
    browser.find_element_by_xpath('//*[@id="targetparam1147"]/dt/a').click()
    time.sleep(1)

    #brandSelect
    browser.find_element_by_xpath('//*[@id="targetparam1147"]/dd/ul/li[2]/a').click()

    #state
    browser.find_element_by_xpath('//*[@id="targetparam1143"]/dt/a').click()

    #stateSelect
    browser.find_element_by_xpath('//*[@id="targetparam1143"]/dd/ul/li[2]/a').click()

    #person
    browser.find_element_by_xpath('//*[@id="add-person"]').send_keys('John Snow')

    #price
    browser.find_element_by_xpath('//*[@id="parameter-div-price"]/div[3]/div/div[1]/p[1]/input').send_keys('10')

    #typeA
    browser.find_element_by_xpath('//*[@id="targetid_private_business"]/dt/a').click()

    #typeSelect
    browser.find_element_by_xpath('//*[@id="targetid_private_business"]/dd/ul/li[3]/a').click()

    #address
    browser.find_element_by_xpath('//*[@id="mapAddress"]').send_keys('Benfica, Lisboa, Lisboa')
    time.sleep(1)

    browser.find_element_by_xpath('//*[contains(@id,"suggested-city-")]').click()
    time.sleep(10)

    #save
    browser.find_element_by_xpath('//*[@id="save"]').click()
    browser.find_element_by_xpath('//*[@id="smsVerificationStep1Form"]/fieldset/div/div/input[2]').send_keys('910000000')

    browser.save_screenshot('newAdvert.png')
    time.sleep(5)

    #sreenShot
    browser.save_screenshot('newAdvert.png')
    browser.quit()

def editUser():

    #closePopUp
    browser.find_element_by_xpath('//*[@id="hide_homepage_video"]').click()
    time.sleep(1)

    #login
    browser.find_element_by_xpath('//*[@id="topLoginLink"]/div').click()

    #insert user
    browser.find_element_by_xpath('//*[@id="userEmail"]').send_keys('qachallengept@gmail.com')

    #insert password
    browser.find_element_by_xpath('//*[@id="userPass"]').send_keys('inicial1234')

    #submit login
    browser.find_element_by_xpath('//*[@id="se_userLogin"]').click()

    #close cookiesBar
    browser.find_element_by_xpath('//*[@id="cookiesBar"]/a').click()
    time.sleep(3)

    webdriver.ActionChains(browser).move_to_element(browser.find_element_by_xpath('//*[@id="topLoginLink"]/span')).perform()
    time.sleep(5)

    #settings
    webdriver.ActionChains(browser).move_to_element(browser.find_element_by_xpath('//*[@id="login-box-settings"]/span')).click().perform()
    time.sleep(2)

    #notification
    browser.find_element_by_xpath('//*[@id="notification_center"]/a/span').click()
    time.sleep(2)

    browser.find_element_by_xpath('//*[@id="formNotificationCenter"]/ul/li[1]/div[2]/label[1]').click()
    time.sleep(2)

    #save settings
    browser.find_element_by_xpath('//*[@id="saveButtonNotificationCenter"]').click()
    time.sleep(3)

    #screenShot
    browser.save_screenshot('editUser.png')
    browser.quit()

def loginLogout():

    #closePopUp
    browser.find_element_by_xpath('//*[@id="hide_homepage_video"]').click()
    time.sleep(1)

    #login
    browser.find_element_by_xpath('//*[@id="topLoginLink"]/div').click()

    #insert user
    browser.find_element_by_xpath('//*[@id="userEmail"]').send_keys('qachallengept@gmail.com')

    #insert password
    browser.find_element_by_xpath('//*[@id="userPass"]').send_keys('inicial1234')

    #submit login
    browser.find_element_by_xpath('//*[@id="se_userLogin"]').click()

    #close cookiesBar
    browser.find_element_by_xpath('//*[@id="cookiesBar"]/a').click()
    time.sleep(3)

    webdriver.ActionChains(browser).move_to_element(browser.find_element_by_xpath('//*[@id="topLoginLink"]/span')).perform()
    time.sleep(5)

    #logOut
    webdriver.ActionChains(browser).move_to_element(browser.find_element_by_xpath('//*[@id="login-box-logout"]/span/span')).click().perform()

    browser.save_screenshot('loginLogout.png')
    browser.quit()

newAdvertNotLogged()
time.sleep(10)
registerNewUser()
time.sleep(10)
editUser()
time.sleep(10)
loginLogout()
time.sleep(10)
activateNewUser()
time.sleep(10)
newAdvert()

