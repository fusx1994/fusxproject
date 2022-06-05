

import json
import time
import requests

huaanyifuetfurl='http://fundf10.eastmoney.com/jjfl_000217.html'

# 你复制的webhook地址
url = "https://open.feishu.cn/open-apis/bot/v2/hook/c82827a4-d570-42ea-a525-359f3e4ab23a"
from selenium import webdriver
import decimal
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(executable_path='/root/Desktop/code/geckodriver',options=options)
try:
	driver.maximize_window()
	driver.implicitly_wait(60)
	driver.get(huaanyifuetfurl)
	fund_gsz=driver.find_element_by_xpath('//*[@id="fund_gsz"]')
	fund_gszf=driver.find_element_by_xpath('//*[@id="fund_gszf"]')
	ti=driver.find_element_by_xpath('//*[@id="bodydiv"]/div[8]/div[3]/div[1]/div[1]/div[2]/p[1]/label[2]')
	data = {
		"msg_type": "interactive",
		"card": {
		    "config": {
		        "wide_screen_mode": True
		    },
		    "header": {
		        "title": {
		            "tag": "plain_text",
		            "content": "华安黄金"
		        },
		        "template": "red"
		    },
		    "elements": [{"tag": "div",
		                  "text": {"content": f"概况:{ti.text}",
		                           "tag": "lark_md"}},
				{"tag": "div",
					 "text":{"content": f"华安当日金价:{str(decimal.Decimal(ti.text.strip().split('(')[0].strip().split('：')[1].strip()) * 270)}",
		                           "tag": "lark_md"}
		                  }

				]}
	    }


	headers = {
	'Content-Type': 'application/json'
	}

	response = requests.request("POST", url, headers=headers,json=data)

	print(response.text)

except Exception as e:
    print(e)
finally:
    driver.quit()





