from selenium import webdriver


# 声明浏览器对象
chrome_driver = r'/home/huizi/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_driver)
url = "https://www.qiushibaike.com/text/"
# url = "https:www.baidu.com"
# 打开相应的网址
browser.get(url)
# 打印网页源代码
# print(browser.page_source)
# 将信息存储到本地文件中/home/huizi/文档/
filePath = r"/home/huizi/文档/test.txt"
file = open(filePath,'w')
file.write(browser.page_source)
file.close()
# print('browser is opening')
# print(browser.find_element_by_tag_name("span").click())
# print(browser.title)
# print(browser.application_cache)
# print(browser.get_cookies())
# print(browser.delete_all_cookies())
# print(browser.get_cookies())
browser.close()