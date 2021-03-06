from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common.keys import Keys

from config import *

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-incognito")
# chrome_options.add_argument(
#     f"user-data-dir=C:/Users/{EMAIL}/AppData/Local/Google/Chrome/User Data/Default")
# chrome_options.add_argument(
#     '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')

browser = webdriver.Chrome(
    executable_path='/usr/local/bin/chromedriver')
# browser.maximize_window()

browser.get('https://docs.google.com/forms/d/e/1FAIpQLSffxZ8i68wYTKzGI1d47koDxVTPu-Qg5S6TZJQn10QW4s9LFQ/viewform?gxids=7628')
actions = ActionChains(browser)

emailAddressInput = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "div:nth-child(2) > div > div > div > input.quantumWizTextinputPaperinputInput.exportInput")))

nameInput = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "div:nth-child(3) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div > div > div > input.quantumWizTextinputPaperinputInput.exportInput")))

membershipNumberInput = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "div:nth-child(4) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div > div > div > input.quantumWizTextinputPaperinputInput.exportInput")))

cssSelectorForGymChoice = ""
if(GYM_CHOICE == "Campus"):
    cssSelectorForGymChoice = "#i19 > div > div.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle"
elif(GYM_CHOICE == "QRW"):
    cssSelectorForGymChoice = "#i25 > div > div.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle"
else:
    cssSelectorForGymChoice = "#i22 > div > div.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle"

sportsCenterInput = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, cssSelectorForGymChoice)))

buttonToPage2 = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "span.appsMaterialWizButtonPaperbuttonContent.exportButtonContent")))

emailAddressInput.send_keys(UNIVERSITY_EMAIL)
nameInput.send_keys(NAME)
membershipNumberInput.send_keys(UNO)
sportsCenterInput.click()
buttonToPage2.click()

scheduleASession = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#i9 > div > div.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle")))

nextToPage3 = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "div:nth-child(2) > span > span.appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")))

scheduleASession.click()
nextToPage3.click()

timeSlotDropDown = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "div.quantumWizMenuPaperselectOption.appsMaterialWizMenuPaperselectOption.freebirdThemedSelectOptionDarkerDisabled.exportOption.isSelected.isPlaceholder")))

timeSlotDropDown.click()

dropDownMenu = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "div.exportSelectPopup.quantumWizMenuPaperselectPopup.appsMaterialWizMenuPaperselectPopup")))

for i in range(24):
    actions.pause(0.1)
    actions.send_keys(Keys.DOWN)
actions.send_keys(Keys.RETURN)
actions.perform()
actions.pause(2)

for i in range(2):
    actions.pause(0.1)
    actions.send_keys(Keys.TAB)
actions.send_keys(Keys.RETURN)
actions.perform()

difficultyBreathing = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#i14 > div > div.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle")))
difficultyBreathing.click()

soreThroat = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#i24 > div > div.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle")))
soreThroat.click()

coughing = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#i34 > div > div.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle")))
coughing.click()

shortnessOfBreath = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#i44 > div > div.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle")))
shortnessOfBreath.click()

fever = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#i54 > div > div.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle")))
fever.click()

closeContact = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#i64 > div > div.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle")))
closeContact.click()

traveledOverseas = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#i76 > div > div.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle")))
traveledOverseas.click()

closeContactTravelledOverseas = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#i86 > div > div.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle")))
closeContactTravelledOverseas.click()

nextToPage5 = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "div:nth-child(2) > span > span.appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")))
nextToPage5.click()

declaration = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox")))
declaration.click()

submitForm = WebDriverWait(browser, 60).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "div.appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonFilled.freebirdFormviewerViewNavigationSubmitButton.freebirdThemedFilledButtonM2 > span > span.appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")))
submitForm.click()

# browser.quit()
