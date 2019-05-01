from selenium import webdriver
import time

hashtag = {}
path = "chromedriver.exe"
keyword = input("검색어를 입력하세요 : ")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-gpu")
chrome_options.add_argument("lang=ko_KR")
driver = webdriver.Chrome(path, chrome_options = chrome_options)

driver.get("https://www.instagram.com/explore/tags/" + keyword)
time.sleep(8)

html = []
num_ok = 0
# 33 > 50 samples
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

for i in driver.find_elements_by_css_selector('.v1Nh3 > a'):
    html.append(i.get_attribute('href'))

if len(html) == 0:
    print("검색 결과가 없습니다.")
    exit(0)

for url in html:
    driver.get(url)
    if driver.find_elements_by_css_selector('.dialog-404'):
        continue
    heartsignal = driver.find_elements_by_css_selector('.Nm9Fw')
    look = driver.find_elements_by_css_selector('vc0H2')

    if len(heartsignal) == 0:
        heart = 0
    elif '먼저' not in heartsignal[0].text:
        heartsignal = heartsignal[0]
        print("{} : {}".format(url,heartsignal))
        heart = heartsignal.text.split('좋아요 ')[1].split('개')[0]
    elif len(look) != 0:
        look.click()
        se_heart = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/div[4]/span')
        if len(se_heart) == 0:
            heart = 0
        else:
            heart = se_heart[0].text
    else:
        heart = 0
   
    if heart != 0:
        heart_value = int(heart.replace(',',''))
    else:
        heart_value = 0
    hashtag_list = driver.find_elements_by_css_selector('body')[0].text.split('#')[1:-1]

    for ch in hashtag_list:
        ch = ch.split(' ')[0].split('\n')[0]

        if ch not in hashtag.keys():
            hashtag[ch] = [heart_value, 1]
            print(hashtag)
        else:
            hashtag[ch][0] += heart_value
            hashtag[ch][1] += 1
    num_ok += 1
    print("%.2f %% Complete!!" %(num_ok/len(html) * 100))

    time.sleep(1)

driver.close()



