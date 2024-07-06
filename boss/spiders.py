import fun 
import time
import random
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class bossSpioder:
    def __init__(self,driver,url,w):
        self.__driver = driver
        self.__url = url
        self.__w = w
        #添加线程锁对象
        self.__lock = threading.Lock()
        self.__data = {
            'name':[],
            'salary':[],
            'city':[],
            'degree':[],
            'experience':[],
            'request':[],
            'company':[],
            'size':[],
            'welfare':[]
        } #方便后续数据处理
    
    def __get__(self,w):
        self.__driver.get(self.__url)
        try:
            wait = WebDriverWait(self.__driver,timeout=15)
            job_cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'job-card-wrapper')))        
            for job in job_cards:
                name = job.find_element_by_class_name('job-name').text
                salary = job.find_element_by_class_name('salary').text
                city = job.find_element_by_class_name('job-area').text
                degree =job.find_element_by_class_name('tag-list').find_elements_by_tag_name('li')[1].text
                experience = job.find_element_by_class_name('tag-list').find_elements_by_tag_name('li')[0].text
                time.sleep(random.randint(1,3))
                request = fun.get_request(job,self.__driver)
                company = job.find_element_by_class_name('company-name').text
                size = job.find_element_by_class_name('company-tag-list').find_elements_by_tag_name('li')[2].text
                welfare = job.find_element_by_class_name('info-desc').text
                with self.__lock:
                    w.writerow([name,salary,city,degree,experience,request,company,size,welfare])
        except Exception as e:
            print(e)
    def crawl(self):
        self.__get__(self.__w)
      
    # def getData(self):
    #     return self.__data
    
    
    
    
    
    # for _ in range(10):
    #         try:
    #             wait = WebDriverWait(self.__driver,timeout=15)
    #             job_cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'job-card-wrapper')))
                
    #             for job in job_cards:
    #                 name = job.find_element_by_class_name('job-name').text
    #                 salary = job.find_element_by_class_name('salary').text
    #                 city = job.find_element_by_class_name('job-area').text
    #                 degree =job.find_element_by_class_name('tag-list').find_elements_by_tag_name('li')[1].text
    #                 experience = job.find_element_by_class_name('tag-list').find_elements_by_tag_name('li')[0].text
    #                 time.sleep(random.randint(1,3))
    #                 request = fun.get_request(job,self.__driver)
    #                 company = job.find_element_by_class_name('company-name').text
    #                 size = job.find_element_by_class_name('company-tag-list').find_elements_by_tag_name('li')[2].text
    #                 welfare = job.find_element_by_class_name('info-desc').text
    #                 w.writerow([name,salary,city,degree,experience,request,company,size,welfare])
                    
    #                 # self.__data['name'].append(name)
    #                 # self.__data['salary'].append(salary)
    #                 # self.__data['city'].append(city)
    #                 # self.__data['degree'].append(degree)
    #                 # self.__data['experience'].append(experience)
    #                 # self.__data['request'].append(request)
    #                 # self.__data['company'].append(company)
    #                 # self.__data['size'].append(size)
    #                 # self.__data['welfare'].append(welfare)
    #             # time.sleep(random.randint(3,8))
    #             # self.__driver.find_element_by_class_name('ui-icon-arrow-right').click()
    #         except Exception as e:
    #             print(e)