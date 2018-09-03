# -*- coding: utf-8 -*-
from selenium import webdriver
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
def login_taobao():
    '''
    selenium模拟登陆淘宝页面
    :return: cookie
    '''
    driver = webdriver.Chrome(executable_path=r"E:\anaconda\envs\scrapy_35\Scripts\chromedriver_win32\chromedriver.exe")
    driver.maximize_window() #将浏览器最大化显示
    driver.delete_all_cookies()
    driver.get("https://login.taobao.com/member/login.jhtml")
    #load the switch
    # 点击跳转输入密码验证码页面
    element=WebDriverWait(driver,60).until(lambda driver :
    driver.find_element_by_xpath("//*[@id='J_Quick2Static']"))
    element.click()
    driver.implicitly_wait(20)
    #输入用户名
    username=driver.find_element_by_name("TPL_username")
    if not username.is_displayed:
        driver.implicitly_wait(20)
        driver.find_element_by_xpath("//*[@id='J_Quick2Static']").click()
    driver.implicitly_wait(20)
    username.send_keys("*****")
    #输入密码
    driver.find_element_by_name("TPL_password").send_keys("*****")
    driver.implicitly_wait(100)
    #点击拖动验证码的实现
    yanzhengma = driver.find_elements_by_id("nc_1_n1z")
    if  yanzhengma!='':
        time.sleep(3)
        yanzhengma=driver.find_elements_by_id("nc_1_n1z")
        driver.implicitly_wait(20)
        ActionChains(driver).click_and_hold(yanzhengma[0]).perform()

        ActionChains(driver).move_by_offset(280,0).perform()
        time.sleep(1)
        ActionChains(driver).release().perform()
        time.sleep(1)

    #点击登陆按钮
    driver.find_element_by_xpath("//*[@id='J_SubmitStatic']").click()
    #保存登陆后的cookie
    url = "https://i.taobao.com/my_taobao.htm?nekot=yb3K0Mfn4bAxOTkx1535940877765"
    while driver.current_url == url:
        # 链接跳转则表示登陆成功
        time.sleep(3)
        pass

    list_cookies = driver.get_cookies()  # 获取selenium cookie
    driver.quit()

    cookie = {}
    # 转换dict调用
    for item in list_cookies:
        cookie[item['name']] = item['value']

    url = 'https://i.taobao.com/my_taobao.htm'
    header = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1;Trident/5.0)',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8', }
    response = requests.get(url, headers=header, cookies=cookie)



    time.sleep(100)


login_taobao()
