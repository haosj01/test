#coding:gbk
import urllib
from xml.parsers.expat import ParserCreate
import re
# ��������Ԥ��
# �ٶ�����
xml = ''
try:
    page = urllib.urlopen('http://api.map.baidu.com/telematics/v2/weather?location=%E4%B8%8A%E6%B5%B7&ak=B8aced94da0b345579f481a1294c9094')
    xml = page.read()
finally:
    page.close()
# print xml


class BaiduWeatherSaxHandler(object):
    def __init__(self):
        self._weather = dict()
        self._count = 0
        self._current_element = ''
        self.city={}

    def start_element(self, name, attrs):
        self._current_element = name
        if name == 'result':
            self._count += 1
            self._weather[self._count] = dict()
        

    def end_element(self, name):
        pass

    def char_data(self, text):
        # �ų����з��Ϳհ�����
        re_str = '^[\n|\s]+$'
        if self._current_element and not re.match(re_str, text) and self._weather:
            self._weather[self._count][self._current_element] = text
        if not re.match(re_str, text) and self._current_element== 'currentCity' :
            self.city['currentCity']=text

    def show_weather(self):
        for v in self._weather.values():
            print v['date'], '\t'*(7-len(v['date'])), v['temperature'], v['weather'], v['wind']

    def current_element(self):
        return self._current_element


handler = BaiduWeatherSaxHandler()
parser = ParserCreate()

parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

parser.Parse(xml)


print handler.current_element()
print handler.city['currentCity']

# �ٶ�����Ϣ����characterdata��ģ�����һ�ַ���attrs��Ŀ����Լ�����
# url = 'http://flash.weather.com.cn/wmaps/xml/china.xml'
