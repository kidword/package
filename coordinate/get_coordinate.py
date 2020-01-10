"""
百度api获取经纬度坐标
天地图经纬度转成详细地址
"""
import requests
import json
from urllib import parse
from fake_useragent import UserAgent


class Coordinate:
    def __init__(self):
        self.base = 'http://api.map.baidu.com/geocoder?'
        self.tiandi_url = 'http://api.tianditu.gov.cn/geocoder?postStr={"lon": %s, "lat": %s, "ver": 1}' \
                          '&type=geocode&tk=4d98f25cc47a0a7cddfc4d4e30210dd1'

    def get_lon_lat(self, data):
        """
        得到坐标
        :param data: 需获取坐标的数据列表
        :return: 坐标结果列表
        """
        ua = UserAgent()
        headers = {"User-Agent": ua.random}
        for d in data:
            query = {
                'key': 'f247cdb592eb43ebac6ccd27f796e2d2',
                'address': d,
                'output': 'json',
            }
            url = self.base + parse.urlencode(query)
            doc = requests.get(url, headers=headers)
            s = doc.content.decode('utf-8')
            try:
                json_data = json.loads(s)
                lat = json_data['result']['location']['lat']
                lng = json_data['result']['location']['lng']
                print('地方为：', d, "经纬度为：", lng, lat)
            except Exception as e:
                print(e)

    def get_address(self, address):
        """
        得到地址
        :param address: 地址经纬度
        :return: 具体地址
        """
        url = self.tiandi_url % (address[0], address[1])
        response = requests.get(url)
        print(response.text)

if __name__ == '__main__':
    c = Coordinate()
    c.get_address(['116.25', '40'])
