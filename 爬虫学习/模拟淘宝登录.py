import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class taobao_infos:
    # 对象初始化
    def __init__(self):
        self.url = "https://login.taobao.com/member/login.jhtml"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images":2})#不加载图片，加快访问速度
        options.add_experimental_option("excludeSwitches", ['enable-automation'])# 设置开发者模式，防止被各大网站识别出来使用了Selenium
        chrome_driver = r'/home/huizi/chromedriver'
        self.browser = webdriver.Chrome(executable_path=chrome_driver,options=options)
        self.wait = WebDriverWait(self.browser, 10)

    # 登录淘宝
    def login(self):
        self.browser.get(self.url)
        print(self.browser.page_source)
        # filePath = r'/home/huizi/文档/weibo.html'
        # file = open(filePath,'w')
        # file.write(self.browser.page_source)
        # file.close()

        weibo_login = self.wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '.weibo-login')
        ))
        weibo_login.click()
        weibo_username = self.wait.until(EC.presence_of_element_located(
            (By.NAME, 'username')
        ))
        weibo_username.send_keys(weibo_user)
        weibo_password = self.wait.until(EC.presence_of_element_located(
            (By.NAME, 'password')
        ))
        weibo_password.send_keys(weibo_pwd)

        weibo_success = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.W_btn_g>span')
        ))
        weibo_success.click()
        # 由于淘宝的安全账户，导致无法登录，所以接下来无法操作

if __name__ == '__main__':
    weibo_user = '15668095291'
    weibo_pwd = 'youzi123'
    a = taobao_infos()
    a.login()
