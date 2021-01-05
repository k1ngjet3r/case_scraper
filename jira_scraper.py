from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from openpyxl import load_workbook
from openpyxl import Workbook


class Scraper():
    def __init__(self, TCid, test_case_list, output_name):
        self.tc_list_sheet = (load_workbook(str(test_case_list))).active
        self.output_name = str(output_name)
        self.wb = Workbook()

    def case_list(self):
        id_list = []
        for id in self.tc_list_sheet.iter_rows(max_col=1, values_only=True):
            if id is not None:
                id_list.append(id)
            else:
                break
        return id_list

    def scrapping(self):
        print('Opening Jira...')
        try:
            driver = webdriver.Chrome()
            url = f'https://matsjira.cienetcorp.com/login.jsp'
            driver.get(url)
        except:
            raise SystemExit(
                'Unable to connect to Jira server, please check your wifi setting!')

        username = 'jeter.lin'
        pw = 'sD4T1pDTZp'
        print('Entering the username and password')
        driver.find_element_by_id('login-form-username').send_keys(username)
        driver.find_element_by_id('login-form-password').send_keys(pw)
        driver.find_element_by_id('login-form-submit').click()

        sheet = self.wb.active
        sheet.create_sheet('Not found')
        sheet.create_sheet('Detailed list')

        id_list = self.case_list()
        cur_num = 0
        total_tc = len(id_list)

        for id in id_list:
            cur_num += 1
            print('fatching...{}/{}'.format(cur_num, total_tc))
            driver.get(self.url_gen(id))
            try:
                original_TCID = driver.find_element_by_class_name(
                    'customfield_10202').text
                result = driver.find_element_by_class_name(
                    'customfield_10341').text
                precondition = driver.find_element_by_class_name(
                    'customfield_10331').text
                test_step = driver.find_element_by_class_name(
                    'customfield_10342').text
                expected = driver.find_element_by_class_name(
                    'customfield_10315').text
                objective = driver.find_element_by_class_name(
                    'customfield_10336').text
                case_detail = [original_TCID, result,
                               precondition, test_step, expected, objective]
                print('Found!')
                print('==========================================')
                sheet['Detailed list'].append(case_detail)
            except:
                print('cannot find the detail of case: {}'.format(id))
                print('==========================================')
                sheet['Not found'].append([id])

        print('Done!, saving the file named {}'.format(self.output_name))
        sheet.save(self.output_name)

    def url_gen(self, tcid):
        frame = f'https://matsjira.cienetcorp.com/issues/?jql=project%20%3D%20%22TESTSPEC%20MY22%22%20AND%20text%20~%20'
        return frame + tcid
