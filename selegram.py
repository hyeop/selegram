from selenium import webdriver
import time
 0
    elif '먼저' not in heartsignal[0].text:
       hashtag[ch][1] += 1
    num_ok += 1
    print("%.2f %% Complete!!" %(num_ok/len(html) * 100))

    time.sleep(1)

driver.close()



