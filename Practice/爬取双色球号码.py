from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook

# 打开谷歌浏览器
dr = webdriver.Chrome()

# 隐性等待
dr.implicitly_wait(20)

# 浏览器窗口最大化
dr.maximize_window()

# 跳转到双色球号码网站
dr.get('https://www.cwl.gov.cn/ygkj/wqkjgg/ssq/')

# 强制等待1秒钟
time.sleep(1)

'''
# 获取开奖期数
kjqs = dr.find_element(By.XPATH, '//tbody/tr[1]/td[1]')
print(kjqs.text)

# 获取开奖日期
kjrq = dr.find_element(By.XPATH, '//tbody/tr[1]/td[1]')
print(kjrq.text)

# 获取开奖号码
kjhm = dr.find_element(By.XPATH, '//tbody/tr[1]/td[3]//div')
print(kjhm.text)
print('*_*'*10)

# 获取开奖期数
kjqs = dr.find_element(By.XPATH, '//tbody/tr[2]/td[1]')
print(kjqs.text)

# 获取开奖日期
kjrq = dr.find_element(By.XPATH, '//tbody/tr[2]/td[1]')
print(kjrq.text)

# 获取开奖号码
kjhm = dr.find_element(By.XPATH, '//tbody/tr[2]/td[3]//div')
print(kjhm.text)
print('*_*'*10)

'''

# for i in range(1, 31):
#     # 获取开奖期数
#     kjqs = dr.find_element(By.XPATH, f'//tbody/tr[{i}]/td[1]')
#     print(kjqs.text)

#     # 获取开奖日期
#     kjrq = dr.find_element(By.XPATH, f'//tbody/tr[{i}]/td[1]')
#     print(kjrq.text)

#     # 获取开奖号码
#     kjhm = dr.find_element(By.XPATH, f'//tbody/tr[{i}]/td[3]//div')
#     print(kjhm.text)
#     print('*_*'*5 + f'第{i}组号码' + '*_*'*5)


# def hq_haom():
#     for i in range(1, 31):
#         # 获取开奖期数
#         kjqs = dr.find_element(By.XPATH, f'//tbody/tr[{i}]/td[1]')
#         print(kjqs.text)

#         # 获取开奖日期
#         kjrq = dr.find_element(By.XPATH, f'//tbody/tr[{i}]/td[1]')
#         print(kjrq.text)

#         # 获取开奖号码
#         kjhm = dr.find_element(By.XPATH, f'//tbody/tr[{i}]/td[3]//div')
#         print(kjhm.text)
#         print('*_*'*5 + f'第{i}组号码' + '*_*'*5)

bnu_list = []


def down_ballnum():
    # 获取每一页的数据
    for i in range(1, 31):
        # 获取期数
        # kjqs = dr.find_element_by_xpath('//tbody/tr[@data-alias="undefined"]/td[1]')
        # kjqs = dr.find_element_by_xpath(f'//tbody/tr[{i}]/td[1]')
        kjqs = dr.find_element(By.XPATH, f'//tbody/tr[{i}]/td[1]')

        # 获取开奖日期
        # kjrq = dr.find_element_by_xpath(f'//tbody/tr[{i}]/td[2]')
        kjrq = dr.find_element(By.XPATH, f'//tbody/tr[{i}]/td[2]')

        # 获取中奖号码
        # kjhm = dr.find_element_by_xpath(f'//tbody/tr[{i}]/td[3]//div')
        kjhm = dr.find_element(By.XPATH, f'//tbody/tr[{i}]/td[3]//div')

        # 添加到列表中
        bnu_list.append([kjqs.text, kjrq.text, kjhm.text.replace('\n', '、')])
        print([kjqs.text, kjrq.text, kjhm.text.replace('\n', '、')])
        print('*_*'*5 + f'第{i}组号码' + '*_*'*5)
    # print(bnu_list)
    return bnu_list

# 写数据到excel文件中


def save_excel(path, number_lists):
    # 创建一个新的工作簿
    workbook = Workbook()

    # 获取活动的工作表（默认创建的第一个工作表）
    ballsheet = workbook.active

    # 写入标题
    ballsheet['A1'] = '开奖期数'
    ballsheet['B1'] = '开奖期数'
    ballsheet['C1'] = '开奖结果'

    for row in number_lists:
        ballsheet.append(row)
    workbook.save(path)


# 翻页函数
for j in range(2, 61):
    # nextpage = dr.find_element_by_link_text(f'{j}')
    nextpage = dr.find_element(By.LINK_TEXT, f'{j}')
    time.sleep(1)
    nextpage.click()
    time.sleep(1)

    # 调用号码生成函数
    num_lists = down_ballnum()

    # 调用写excel函数
    save_excel(r'd:\ball111.xlsx', num_lists)
