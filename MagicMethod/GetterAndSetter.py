"""
@File: GetterAndSetter
@Author: Ray
@Date: 2018-04-09 19:52:39
@Version: 1.0
"""

import requests


class Magic:
    def __init__(self):
        self._url = "http://lf.snssdk.com/article/v2/tab_comments/?gro" \
                    "up_id=6389542758708675073&item_id=638954275870867" \
                    "5073&aggr_type=1&count=20&offset=0&tab_index=0&ii" \
                    "d=9659309930&device_id=25691803112&ac=wifi&channe" \
                    "l=vivo&aid=13&app_name=news_article&version_code=" \
                    "609&version_name=6.0.9&device_platform=android&ab" \
                    "_version=116029%2C112577%2C120222%2C101786%2C1205" \
                    "42%2C119380%2C110341%2C113607%2C119525%2C106784%2" \
                    "C113608%2C120243%2C119889%2C105610%2C120212%2C120" \
                    "459%2C104323%2C120641%2C112578%2C115571%2C120419%" \
                    "2C31646%2C121005%2C118216%2C114338&ab_client=a1%2" \
                    "Cc4%2Ce1%2Cf2%2Cg2%2Cf7&ab_group=100170&ab_featur" \
                    "e=94563%2C102749&abflag=3&ssmix=a&device_type=viv" \
                    "o+V3Max+A&device_brand=vivo&language=zh&os_api=22" \
                    "&os_version=5.1.1&uuid=862545038604758&openudid=f" \
                    "96595e789672db8&manifest_version_code=609&resolut" \
                    "ion=1080*1920&dpi=480&update_version_code=6091&_r" \
                    "ticket=1492784667138"
        self._data = requests.get(self._url).json()

    def __getattr__(self, name):
        return self._data[name]


if __name__ == "__main__":
    mgc = Magic()
    print(mgc.tab_info)
    print(mgc.message)
