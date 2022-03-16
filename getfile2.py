import requests
from http import cookiejar
from lxml import etree
session = requests.session()

def get_download(id):

    Referer = "http://basic.10jqka.com.cn/" + id + "/finance.html"
    header = {
        "Connection": "keep-alive",
        "Host": "basic.10jqka.com.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Referer": Referer,
    }
    # http://basic.10jqka.com.cn/300164/finance.html
    # http://basic.10jqka.com.cn/api/stock/export.php?export=benefit&type=year&code=300033
    url = "http://basic.10jqka.com.cn/api/stock/export.php"
    param = {
        "export": "benefit",
        "type": "year",
        "code": id
    }

    response = session.get(url=url, params=param, headers=header)

    if response == 200:
        file_name = param['code'] + "_" + param['export'] + "_" + param['type'] + ".xls"
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response)


if __name__ == '__main__':
    code = ["300164", "300807", "300534", "603963", "600249"]
    for id in code:
        get_download(id)
