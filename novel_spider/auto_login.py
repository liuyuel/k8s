# 导入selenium2中的webdriver库
from selenium import webdriver
from selenium.webdriver.common.by import By


def has_element(by=By.ID, value=None):
    try:
        driver.find_element(by, value)
        return True
    except:
        return False


# python E:\pythonProject\docker_registry\novel_spider\auto_login.py
if __name__ == '__main__':
    # 实例化出一个Firefox浏览器
    driver = webdriver.Chrome(executable_path=r'C:\Users\yueliuk\AppData\Local\Google\Chrome\Application\chromedriver.exe')

    # 设置浏览器窗口的位置和大小
    driver.set_window_position(20, 40)
    driver.set_window_size(1100, 700)

    # 打开一个页面（合天登录页）
    driver.get("http://1.1.1.3")

    # 通过使用选择器选择元素进行模拟输入和点击按钮提交
    if has_element(By.CLASS_NAME, 'logout'):
        driver.execute_script('document.getElementsByClassName("logout")[0].click()')
        driver.quit()
        driver = webdriver.Chrome(executable_path=r'C:\Users\yueliuk\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        driver.get("http://1.1.1.3")

    driver.find_element(By.ID, 'password_name').clear()
    driver.find_element(By.ID, 'password_name').send_keys('yueliuk')
    driver.find_element(By.ID, 'password_pwd').clear()
    driver.find_element(By.ID, 'password_pwd').send_keys('lY1234567890@#')
    driver.find_element(By.ID, 'password_submitBtn').click()

    # 退出窗口
    driver.quit()
