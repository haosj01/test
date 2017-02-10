#coding:utf-8

import unittest
import requests
import os,sys
import HTMLTestRunner
path=os.path.dirname(os.path.abspath(__file__))
sys.path.append(r'E:\test')
import xlrd
import xlwt
import paramunittest


workbook = xlrd.open_workbook(r'E:\test\test_case\data.xlsx')
sheet= workbook.sheet_by_index(0)
col_1=sheet.col_values(0)
col_2=sheet.col_values(1)
data=zip(col_1,col_2)


@paramunittest.parametrized(
##    *data
    ('status',10021,''),
    ('message','parameter error','')
)


class AddEventTest(unittest.TestCase):
    u'''添加发布会'''
    def setUp(self):
        self.url=r'http://127.0.0.1:8000/api/add_event/'

    def setParameters(self,a,b,c):#设置参数
        self.a=a
        self.b=b
        self.c=c
        
    def test_add_event_all_null(self):
        u'''所有参数为空'''
        payload={'eid':'','name':'','limit':'','status':'','address':'','start_time':''}
        r=requests.get(self.url,params=payload)
        a=self.a
        b=self.b
        self.result=r.json()
        self.assertEqual(self.result[a],b)
        print u"实际结果：%s,预期结果：%s"%(self.result[a],b)


class GetEventListTest(unittest.TestCase):
    def setUp(self):
        self.url=r'http://127.0.0.1:8000/api/get_event_list/'
        self.auth=('admin','woainima')
    def test_event_list_eid(self):
        payload={'eid':1}
        r=requests.get(self.url,auth=self.auth,params=payload)
        result=r.json()
        self.assertEqual(result['data']['name'],u'苹果8发布会')



if __name__ == "__main__":
##    unittest.main()
    test_dir='.'
    suite=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

    filename='E:\\test\\result01.html'
    fo=open(filename,'wb')
    
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fo,
        title=u'测试报告',
        description=u'用例执行情况')

    runner.run(suite)
    fo.close()
