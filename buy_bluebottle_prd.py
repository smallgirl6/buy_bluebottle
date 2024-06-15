import sys
import io
import time  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import config  # 導入包含機密資訊的文件
import smtplib
from email.mime.text import MIMEText

# 設置輸出編碼為UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 設置網頁驅動
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
# 1 .Login (原本要先登入的，但發現需要二階段認證，所以用訪客模式購買)
    # # 打開指定網址
    # driver.get("https://store.bluebottlecoffee.jp/")
    # # 點擊登錄按鈕以進入登錄頁面
    # login_button = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "a.Header__AccountIcon"))
    # )
    # login_button.click()
    # # 確認已進入登入頁面
    # print("進入登入頁面。")
    # # 等待登錄頁面加載並填寫登錄信息
    # email_input = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.NAME, "customer[email]"))
    # )
    # password_input = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.NAME, "customer[password]"))
    # )
    # # 輸入郵箱和密碼
    # email_input.send_keys("config.blueboyttle_account")
    # password_input.send_keys("config.blueboyttle_password")
    # # 點擊「ログイン」按鈕
    # login_submit_button = driver.find_element(By.CSS_SELECTOR, "button.Form__Submit.Button.Button--primary.Button--full")
    # login_submit_button.click()
    # print("成功登入")
    # # 等待一段時間確保登入成功
    # time.sleep(5)
    print("1.SKIP")

# 2 .買第一項東西  
    # 打開指定網址
    driver.get(config.blueboyttle_collaboration_link)
    # 點選搜尋按鈕
    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.Header__Icon.Header__searchIcon"))
    )
    search_button.click()
    # 等待搜尋框變為可見
    search_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='search' and @class='Search__Input Heading']"))
    )
    search_input.send_keys(config.blueboyttle_PRODUCT_NAME1)
    # 搜尋結果中點擊包含環境變數的產品連結
    product_link1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{config.blueboyttle_PRODUCT_NAME1}')]"))
    )
    product_link1.click()
    # 等待頁面加載並點擊「カートに追加」按鈕
    add_to_cart_button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='Product__AddToCartButton']"))
    )
    add_to_cart_button1.click()
    # 確認產品已正常加入購物車
    print("2." + f"{config.blueboyttle_PRODUCT_NAME1}已成功添加到購物車。")

# 3 .買第二項東西  
    # 打開指定網址
    driver.get(config.blueboyttle_collaboration_link)
    # 點選搜尋按鈕
    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.Header__Icon.Header__searchIcon"))
    )
    search_button.click()
    # 等待搜尋框變為可見
    search_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='search' and @class='Search__Input Heading']"))
    )
    search_input.send_keys(config.blueboyttle_PRODUCT_NAME2)
    # 搜尋結果中點擊包含環境變數的產品連結
    product_link1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{config.blueboyttle_PRODUCT_NAME2}')]"))
    )
    product_link1.click()
    # 等待頁面加載並點擊「カートに追加」按鈕
    add_to_cart_button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='Product__AddToCartButton']"))
    )
    add_to_cart_button1.click()
    # 確認產品已正常加入購物車
    print("3." + f"{config.blueboyttle_PRODUCT_NAME2}已成功添加到購物車。")
    time.sleep(5)

# 4 .買完東西準備結帳
    # 選擇「上記事項を確認しました」的復選框
    confirm_checkbox = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='normal-check']"))
    )
    confirm_checkbox.click()
    # 點擊「ご購入手続きへ」按鈕
    checkout_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='checkout']"))
    )
    checkout_button.click()
    print("4.已成功點擊ご購入手続きへ按鈕。")
    # 等待配送頁面加載
    time.sleep(5)

# 5 .填寫配送信息
    email_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Eメール']"))
    )
    email_input.send_keys(config.email)
    time.sleep(5)
    country_select = driver.find_element(By.NAME, "checkout[shipping_address][country]")
    country_select.send_keys("日本")
    time.sleep(3)
    last_name_input = driver.find_element(By.NAME, "checkout[shipping_address][last_name]")
    last_name_input.send_keys(config.family_name)
    time.sleep(3)
    first_name_input = driver.find_element(By.NAME, "checkout[shipping_address][first_name]")
    first_name_input.send_keys(config.given_name)
    time.sleep(3)
    postal_code_input = driver.find_element(By.NAME, "checkout[shipping_address][zip]")
    postal_code_input.send_keys(config.postal_code)
    time.sleep(3)  
    province_select = driver.find_element(By.ID, "checkout_shipping_address_province")
    province_select.send_keys(config.province)
    time.sleep(3)
    city_input = driver.find_element(By.NAME, "checkout[shipping_address][city]")
    city_input.send_keys(config.city)
    time.sleep(3)
    address_input = driver.find_element(By.NAME, "checkout[shipping_address][address1]")
    address_input.send_keys(config.address2)
    time.sleep(3)
    apartment_input = driver.find_element(By.NAME, "checkout[shipping_address][address2]")
    apartment_input.send_keys(config.apartment2)
    time.sleep(3)
    phone_input = driver.find_element(By.NAME, "checkout[shipping_address][phone]")
    phone_input.send_keys(config.phone2)
    time.sleep(3)
    # 點擊「配送方法の選択へ進む」按鈕
    continue_to_shipping_button = driver.find_element(By.XPATH, "//button[@id='continue_button']")
    continue_to_shipping_button.click()
    print("5.已成功點擊配送方法の選択へ進む按鈕。")
    # 等待支付頁面加載
    time.sleep(5)

# 6 .確認配送資料頁面
    # 點擊「お支払いへ進む」按鈕
    proceed_to_payment_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='お支払いへ進む']/ancestor::button"))
    )
    proceed_to_payment_button.click()
    print("6.已成功點擊お支払いへ進む按鈕。")
    # 等待支付頁面加載
    time.sleep(5)

# 7 .填寫信用卡支付信息 這可能需要OPT認證，所以放棄
    iframe_number = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@name, 'card-fields-number')]"))
    )
    driver.switch_to.frame(iframe_number)
    card_number_input = driver.find_element(By.NAME, "number")
    card_number_input.send_keys(config.card_number)
    driver.switch_to.default_content()
    iframe_name = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@name, 'card-fields-name')]"))
    )
    driver.switch_to.frame(iframe_name)
    card_name_input = driver.find_element(By.NAME, "name")
    card_name_input.send_keys(config.card_name)
    driver.switch_to.default_content()
    iframe_expiry = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@name, 'card-fields-expiry')]"))
    )
    driver.switch_to.frame(iframe_expiry)
    card_expiry_input = driver.find_element(By.NAME, "expiry")
    # 先輸入月份 
    card_expiry_input.send_keys(config.card_expiry_month)
    time.sleep(1)  # 停頓一秒
    # 再輸入年份 
    card_expiry_input.send_keys(config.card_expiry_year)
    driver.switch_to.default_content()
    time.sleep(3)
    iframe_verification = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@name, 'card-fields-verification')]"))
    )
    driver.switch_to.frame(iframe_verification)
    card_verification_value_input = driver.find_element(By.NAME, "verification_value")
    card_verification_value_input.send_keys(config.card_verification)
    driver.switch_to.default_content()
    # 等待一段時間確保輸入沒問題
    time.sleep(5)
    pay_now_button = driver.find_element(By.ID, "continue_button")
    pay_now_button.click()
    time.sleep(10)
    print("7.已成功點擊今すぐ支払う按鈕。")


# # 8 選擇amazonpay
#     amazon_pay_radio = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "checkout_payment_gateway_39563100208"))
#     )
#     amazon_pay_radio.click()    
#     print("8.已選擇Amazon Pay。") 
#     # 點擊「今すぐ支払う」按鈕
#     pay_now_button = driver.find_element(By.ID, "continue_button")
#     pay_now_button.click()
#     # 等待跳到Amazon Pay登入頁面
#     time.sleep(5)

# # 9 在Amazon Pay登入頁面填寫郵件信箱和密碼
#     amazon_email_input = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "ap_email"))
#     )
#     amazon_password_input = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "ap_password"))
#     )
#     amazon_email_input.send_keys(config.amazon_account)
#     amazon_password_input.send_keys(config.amazon_password)
#     # 點擊「signin」按鈕
#     amazon_login_button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "signInSubmit"))
#     )
#     amazon_login_button.click()
#     print("9.已成功點擊signin按钮。")
#     time.sleep(5)
#     # 等待跳到Amazon Pay配送方法頁面

# # 10 .在Amazon Pay頁面選擇預設的配送信息
#     distribution_button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[@id='continue_button']/span[text()='配送方法の選択へ進む']/.."))
#     )
#     distribution_button.click()
#     print("10.已成功點擊Amazon Pay配送方法の選択へ進む按钮。")
#     time.sleep(5)
#     # 等待跳到Amazon Pay支払い方法頁面

# # 11 .在Amazon Pay頁面選擇預設的信用卡信息
#     payment_button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[@id='continue_button']/span[text()='お支払いへ進む']/.."))
#     )
#     payment_button.click()
#     print("11.已成功點擊Amazon Payお支払いへ進む按钮。")

# 12 .最後的結帳頁面 點擊“ご注文完了”按钮
    # order_complete_button = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[@id='continue_button']/span[text()='ご注文完了']/.."))
    # )
    # order_complete_button.click()
    # print("12.已成功點擊ご注文完了按钮。")
    # # 等待一段時間確保購物成功
    # time.sleep(10)

# 13 .發送成功郵件
    # 郵件伺服器配置
    smtp_server = "smtp.mail.me.com"
    smtp_port = 587
    smtp_user = config.icloud_account
    smtp_password = config.icloud_password
    # 創建郵件消息
    msg = MIMEText("成功購買TEST")
    msg["From"] = smtp_user
    msg["To"] = ", ".join([config.amazon_account, config.mail2]) 
    msg["Subject"] = "Blue Bottle Coffee 的購物通知TEST "
    # 連接到SMTP伺服器並發送郵件
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(smtp_user, [config.amazon_account, config.mail2], msg.as_string())
    print("13.郵件已發送成功")
    server.quit()

except Exception as e:
    print(f"執行過程中出現錯誤: {e}")

# 保持網頁打開，等待用戶輸入以結束程序
# input("操作完成，瀏覽器將保持打開狀態。按回車鍵以結束程序並關閉瀏覽器...")