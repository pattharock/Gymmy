from selenium import webdriver
# from selenium.webdriver import findElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

# option = webdriver.ChromeOptions()
# option.add_argument("-incognito")

# print(webdriver)
browser = webdriver.Chrome(
    executable_path='/usr/local/bin/chromedriver')

browser.get('https://forms.gle/4g5ceVZvDjdpD1r27')

# textboxes = browser.find_elements_by_class_name(
#     "quantumWizTextinputPaperinputInput")
# radiobuttons = browser.find_elements_by_class_name(
#     "docssharedWizToggleLabeledLabelWrapper")
# checkboxes = browser.find_elements_by_class_name(
#     "quantumWizTogglePapercheckboxInnerBox")
# submitbutton = browser.find_element_by_class_name(
#     "appsMaterialWizButtonPaperbuttonContent")

# textboxes[0].send_keys("Hello World")

# radiobuttons[2].click()

# checkboxes[1].click()
# checkboxes[3].click()

# submitbutton[0].click()

# content = driver.find_element_by_css_selector('p.content')

# option1 = browser.findElement(By.cssSelector(".appsMaterialWizToggleRadiogroupOnRadio.exportInnerCircle"))
# textarea = browser.findElement(By.cssSelector(".quantumWizTextinputPapertextareaInput.exportTextarea"))


# find_element_by_class_name(
#     "appsMaterialWizToggleRadiogroupOnRadio exportInnerCircle")


# textarea = browser.find_element_by_class_name(
#     "quantumWizTextinputPapertextareaInput exportTextarea")

# try:
#     element = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By., "myDynamicElement"))
#     )
# finally:
#     browser.quit()

# .appsMaterialWizToggleRadiogroupOnRadio.exportInnerCircle

# .appsMaterialWizToggleRadiogroupEl.exportToggleEl

question1option1 = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                      ".appsMaterialWizToggleRadiogroupRadioButtonContainer")))

# .appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonProtected.freebirdFormviewerViewNavigationNoSubmitButton.freebirdThemedProtectedButtonM2

nextToPage2 = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                 ".appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl/appsMaterialWizButtonPaperbuttonProtected.freebirdFormviewerViewNavigationNoSubmitButton.freebirdThemedProtectedButtonM2")))

# textarea = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
#                                                                               ".quantumWizTextinputPapertextareaInput.exportTextarea")))

# submit = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
#                                                                             ".appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonFilled.freebirdFormviewerViewNavigationSubmitButton.freebirdThemedFilledButtonM2")))

# seconds = time.time()
# localtime = time.ctime(seconds)

# .appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonFilled.freebirdFormviewerViewNavigationSubmitButton.freebirdThemedFilledButtonM2.isUndragged
# .appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel
# .appsMaterialWizButtonPaperbuttonContent.exportButtonContent

# print(WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
#                                                                          ".docssharedWizToggleLabeledLabelText.exportLabel.freebirdFormviewerComponentsQuestionRadioLabel"))))

question1option1[0].click()

# textarea.send_keys(""+localtime)

# nextToPage2.click()

print(" ========= OPTION 1 ========= ")
print(question1option1)
print(" ============================ ")
print(" ========= NEXT PG2 ========= ")
print(nextToPage2)
print(" ============================ ")
# print(" ========== SUBMIT ========== ")
# print(submit)
# print(" ============================ ")

# .docssharedWizToggleLabeledLabelText.exportLabel.freebirdFormviewerComponentsQuestionRadioLabel
# .get_attribute("innerHTML")

# appsMaterialWizButtonEl appsMaterialWizButtonPaperbuttonEl appsMaterialWizButtonPaperbuttonFilled freebirdFormviewerViewNavigationSubmitButton freebirdThemedFilledButtonM2

# .appsMaterialWizButtonEl.appsMaterialWizButtonPaperbuttonEl.appsMaterialWizButtonPaperbuttonProtected.freebirdFormviewerViewNavigationNoSubmitButton.freebirdThemedProtectedButtonM2
