from selenium import webdriver
import random
# import time

web = webdriver.Edge(executable_path=r'C:\\Users\\acnst\\Downloads\\Compressed\\edgedriver_win64\\msedgedriver.exe')
web.maximize_window()
# web.get("https://docs.google.com/forms/d/1qmPRJrKfwNwHg_3Ub1L4I3EXpx9Yo7W96tcORhofEwc/viewform?edit_requested=true")

i=1
while i<=5:
    web.get("https://docs.google.com/forms/d/1WxV9rY9EU4rcBtBXIr_-dIB7JSEv5Wtz6j_AFfxfVNg/viewform?edit_requested=true")

    # time.sleep(2) //*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[2]/div/span
    #               //*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[2]/div/span

    RadioButtonPeriod1 = web.find_element("xpath",f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[{3}]/label/div/div[2]/div/span')
    RadioButtonPeriod1.click()

    RadioButtonPeriod2 = web.find_element("xpath",f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[{3}]/label/div/div[2]/div/span')
    RadioButtonPeriod2.click()

    RadioButtonPeriod3 = web.find_element("xpath",f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[{3}]/label/div/div[2]/div/span')
    RadioButtonPeriod3.click()

    RadioButtonPeriod4 = web.find_element("xpath",f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[{3}]/label/div/div[2]/div/span')
    RadioButtonPeriod4.click()

    RadioButtonPeriod5 = web.find_element("xpath",f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div/span/div/div[{3}]/label/div/div[2]/div/span')
    RadioButtonPeriod5.click()

    RadioButtonPeriod6 = web.find_element("xpath",f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[{3}]/label/div/div[2]/div/span')
    RadioButtonPeriod6.click()

    RadioButtonPeriod7 = web.find_element("xpath",f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[{3}]/label/div/div[2]/div/span')
    RadioButtonPeriod7.click()

    Submit = web.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    Submit.click()
    i+=1

print("Terminado")
#
# get_confirmation_div_text = web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
# print(get_confirmation_div_text.text)
# if ((get_confirmation_div_text.text) == "Thank you for attending"):
#     print ("Test Was Successful")
# else:
#     print("Test Was Not Successful") 