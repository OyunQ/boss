import random
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def get_request(job,driver):
    href = job.find_element_by_class_name('job-card-left').get_attribute('href')
    #打开新标签并切换到新标签
    driver.execute_script('window.open('');')
    driver.switch_to.window(driver.window_handles[1])
    
    driver.get(href)
    try:
        wait = WebDriverWait(driver,timeout=15)
        request = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div.job-box > div > div.job-detail > div:nth-child(1) > div.job-sec-text'))).text
        return request
    except TimeoutException as e:
        print(e)
        return''
    finally:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

def createDriver(user_agent,proxy):
    # 指定 chromedriver 的路径
    driver_path = r"C:\Program Files\Google\Chrome\chromedriver_win32_2\chromedriver.exe"
    # 创建 ChromeOptions 实例
    options = Options()
    # options.add_argument('--headless')  # 启用无头模式
    # options.add_argument('--disable-gpu')  # 需要添加，以便在无头模式下渲染图形
    # options.add_argument('--no-sandbox')  # 禁用沙箱
    options.add_argument('--disable-dev-shm-usage')  # 解决共享内存问题
    options.add_argument('window-size=1920x1080')  # 设置浏览器分辨率
    options.add_argument('--start-maximized')  
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument('--proxy-server=' + proxy)
    # 设置请求头
    options.add_argument('user-agent=' + user_agent) 
    options.add_argument('referer=https://www.zhipin.com/web/common/security-check.html?seed=s1WvTSlzR7bVt8/MBeKDc72xRMPqurs1rFjbujheEuUISYZwkVc6MfjuyPUp0ZvyTyd8AhJv869BpeO3xNZ7ug==&name=c0a08e98&ts=1719998960502&callbackUrl=https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=100010000')

    driver = webdriver.Chrome(executable_path=driver_path,options=options)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        '''
    })
    return driver
def randomUA():
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    ]
    return random.choice(user_agents)
def randomProxy():
    proxies = [
    "http://203.89.8.107:80",
    "http://125.77.25.178:8080",
    "http://60.12.168.114:9002",
    "http://112.51.96.118:9091",
    "http://58.20.248.139:9002",
    "http://111.160.204.146:9091",
    "http://125.77.25.177:8080",
    "http://36.134.91.82:8888",
    "http://220.248.70.237:9002",
    "http://49.7.11.187:80",
    "http://183.234.215.11:8443",
    "http://183.215.23.242:9091",
    "http://221.219.102.153:9000",
    "http://223.113.80.158:9091",
    "http://203.19.38.114:1080",
    "http://153.101.67.170:9002",
    "http://223.13.124.24:3128"
    ]
    p = []
    for proxy in proxies:
        if check_proxy(proxy):
            p.append(proxy)
    return random.choice(p)
#判断代理可用性
def check_proxy(proxy):
    try:
        requests.get('https://www.baidu.com',proxies={'http':proxy})
        return True
    except:
        return False