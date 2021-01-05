from bs4 import BeautifulSoup
import requests
from selenium import webdriver

driver = webdriver.Chrome()
url = f'https://matsjira.cienetcorp.com/login.jsp'

driver.get(url)

# log in to jira
username = 'jeter.lin'
pw = 'sD4T1pDTZp'
driver.find_element_by_id('login-form-username').send_keys(username)
driver.find_element_by_id('login-form-password').send_keys(pw)
driver.find_element_by_id('login-form-submit').click()

def url_gen(TCid):
    frame = f'https://matsjira.cienetcorp.com/issues/?jql=project%20%3D%20TESTPLAN%20AND%20%22TEST%20PLAN%20NAME%22%20~%20MY22GB_NonFunc_96I-W157.2.3-QIH22B-230_User_W52%20AND%20text%20~%20'
    return frame + TCid

driver.get(f'https://matsjira.cienetcorp.com/issues/?jql=project%20%3D%20TESTPLAN%20AND%20%22TEST%20PLAN%20NAME%22%20~%20MY22GB_NonFunc_96I-W157.2.3-QIH22B-230_User_W52%20AND%20text%20~%20TC_MFL_76009_Wireless_Connectivity_0078')

original_TCID = driver.find_element_by_class_name('customfield_10202').text
result = driver.find_element_by_class_name('customfield_10341').text
precondition = driver.find_element_by_class_name('customfield_10331').text
test_step = driver.find_element_by_class_name('customfield_10342').text
expected = driver.find_element_by_class_name('customfield_10315').text
objective = driver.find_element_by_class_name('customfield_10336').text

print(original_TCID)
print(precondition)
print(test_step)
print(expected)
print(objective)