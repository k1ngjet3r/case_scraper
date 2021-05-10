from atlassian import Jira
from openpyxl import load_workbook, workbook

jira_instance = Jira(url='http://matsjira.cienetcorp.com/',
                    username='jeter.lin',
                    password='sD4T1pDTZp'
                    )

jira_instance.issue(key='TC_MFL_MyProfile_Security_None_002', fields=['summary'])
