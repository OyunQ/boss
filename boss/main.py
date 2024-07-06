import csv
import spiders
import fun
from concurrent.futures import ThreadPoolExecutor



tag = input('请输入搜索词：')

wool = ThreadPoolExecutor(max_workers=10)
futures = []
f = open('boss.csv','w',newline='',encoding='utf-8')
w = csv.writer(f)
#构造列表头
w.writerow(['name','salary','city','degree','experience','request','company','size','welfare'])
for i in range(1,11):
    proxy = fun.randomProxy()
    driver = fun.createDriver(fun.randomUA(),proxy)
    url = f'https://www.zhipin.com/web/geek/job?query={tag}&city=100010000&experience=102&page={i}'
    spider = spiders.bossSpioder(driver,url,w)
    future = wool.submit(spider.crawl)
    futures.append(future)
#等待所有线程结束
for future in futures:
    future.result()
f.close()
print('完成')