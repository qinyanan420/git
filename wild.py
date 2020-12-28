from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersiom'] = '10.0'
desired_caps['deviceName'] = 'EAM4C20605010156'
desired_caps['appPackage'] = 'com.bingo.wild.android'
desired_caps['appActivity'] = 'com.bingo.wild.AppActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# 获取当前手机屏幕大小X,Y
X = driver.get_window_size()['width']
Y = driver.get_window_size()['height']
l = 2400
d = 1080
def taptest(driver,x,y):
    # 设定系数,控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
    a1 = x
    b1 = y
    # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
    driver.tap([(a1, b1),(a1, b1),(a1, b1),(a1, b1),(a1, b1)])
if __name__ == '__main__':
    time.sleep(2)
    print('点击google弹窗ok按钮')
    taptest(driver,1845,690)
    time.sleep(2)
    print('点击签到按钮')
    taptest(driver,235,270)
    time.sleep(2)
    print('点击Quick Tap Lotto的Claim按钮')
    taptest(driver,640,940)
    time.sleep(3)
    print('点击Start按钮')
    taptest(driver,1200,720)
    print('进行3s等待')
    time.sleep(3)
    a = time.time()
    print('进行Quick Tap点击')
    for i in range(100):
        if time.time() < a+10:
            taptest(driver,1850,900)
        else:
            print(i+1)
            break
    quit()