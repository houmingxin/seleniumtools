"""
    固定的用法，知道怎么用就行了
"""
from selenium.webdriver.support.ui import WebDriverWait

def find_elemenet(driver, locator, timeout=60): #locator是定位元素的值和方式
    """
        方法：显式等待，动态查找元素
        参数：
            driver：浏览器的把柄
            locator：元素的方法和值，自定义("id", "kw")
                - ("id", "username")
                - ("xpath", "xxxxxxx")
                - ("name", "xxxxxx")
                - ("css selector", "xxxxx")
                - ("class name", "xxxxxxxx")
                - ("link text", "抗击肺炎")
                - ("partial link text", "抗击肺")
            timeout：元素查找的超时，默认是60S 
        注意：知道怎么用就行了
    """
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))#lambda匿名方法,把方法当作变量传参