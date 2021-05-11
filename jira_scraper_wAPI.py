from atlassian import Jira
from openpyxl import load_workbook, workbook

jira_instance = Jira(url='https://matsjira.cienetcorp.com/issues/?jql=project%20%3D%20TESTSPEC22%20AND%20%22Original%20GM%20TC%20ID%22%20%20~%20TC_MFL_MyProfile_Security_None_002',
                    username='jeter.lin',
                    password='sD4T1pDTZp'
                    )

jira_instance.issue(key='customfield_10202', fields=['Original GM TC ID','summary'])

result = jira_instance.jql('project = TESTSPEC22 AND "Original GM TC ID"  ~ TC_MFL_MyProfile_Security_None_002', fields=['Original GM TC ID','summary'])

print(result)