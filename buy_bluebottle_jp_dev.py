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
import config  # 機密情報を含むファイルをインポート
import smtplib
from email.mime.text import MIMEText

# 出力エンコードをUTF-8に設定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ウェブドライバーを設定
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
# 1.ログイン（元々はログインが必要だったが、2段階認証が必要なため、ゲストモードで購入）
    # # 指定URLを開く
    # driver.get("https://store.bluebottlecoffee.jp/")
    # # ログインボタンをクリックしてログインページに入る
    # login_button = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "a.Header__AccountIcon"))
    # )
    # login_button.click()
    # # ログインページに入ったことを確認
    # print("ログインページに入りました。")
    # # ログインページの読み込みを待ってログイン情報を入力
    # email_input = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.NAME, "customer[email]"))
    # )
    # password_input = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.NAME, "customer[password]"))
    # )
    # # メールアドレスとパスワードを入力
    # email_input.send_keys("config.blueboyttle_account")
    # password_input.send_keys("config.blueboyttle_password")
    # # 「ログイン」ボタンをクリック
    # login_submit_button = driver.find_element(By.CSS_SELECTOR, "button.Form__Submit.Button.Button--primary.Button--full")
    # login_submit_button.click()
    # print("ログイン成功")
    # # ログイン成功を確認するために少し待つ
    # time.sleep(5)
    print("1.SKIP")

# 2.第一の商品を購入
    # 指定URLを開く
    driver.get(config.blueboyttle_collaboration_link)
    # 「blueboyttle_PRODUCT_NAME1_TEST」を含む商品リンクを探す
    product_link1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{config.blueboyttle_PRODUCT_NAME1_TEST}')]"))
    )
    # 清澄マグの商品リンクをクリック
    product_link1.click()
    # ページが読み込まれるのを待ち、「カートに追加」ボタンがインタラクティブか確認
    add_to_cart_button1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='Product__AddToCartButton']"))
    )
    # 「カートに追加」ボタンをクリック
    add_to_cart_button1.click()
    # 商品がカートに正常に追加されたことを確認
    print("2." + f"{config.blueboyttle_PRODUCT_NAME1_TEST}がカートに正常に追加されました。")

# 3.第二の商品を購入
    # 指定URLを開く
    driver.get(config.blueboyttle_collaboration_link)
    # 「blueboyttle_PRODUCT_NAME2_TEST」を含む商品リンクを探す
    product_link2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{config.blueboyttle_PRODUCT_NAME2_TEST}')]"))
    )
    # デイオフ タンブラーの商品リンクをクリック
    product_link2.click()
    # ページが読み込まれるのを待ち、「カートに追加」ボタンがインタラクティブか確認
    add_to_cart_button2 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='Product__AddToCartButton']"))
    )
    # 「カートに追加」ボタンをクリック
    add_to_cart_button2.click()
    # 商品がカートに正常に追加されたことを確認
    print("3." + f"{config.blueboyttle_PRODUCT_NAME2_TEST}がカートに正常に追加されました。")
    # カートに追加するのを待つ
    time.sleep(3)
    
# 4.買い物が終わり、チェックアウトの準備
    # 「上記事項を確認しました」のチェックボックスを選択
    confirm_checkbox = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='normal-check']"))
    )
    confirm_checkbox.click()
    # 「ご購入手続きへ」ボタンをクリック
    checkout_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='checkout']"))
    )
    checkout_button.click()
    print("4.「ご購入手続きへ」ボタンが正常にクリックされました。")
    # 配送ページの読み込みを待つ
    time.sleep(5)

# 5.配送情報を入力
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
    # 「配送方法の選択へ進む」ボタンをクリック
    continue_to_shipping_button = driver.find_element(By.XPATH, "//button[@id='continue_button']")
    continue_to_shipping_button.click()
    print("5.「配送方法の選択へ進む」ボタンが正常にクリックされました。")
    # 支払いページの読み込みを待つ
    time.sleep(5)

# 6.配送情報確認ページ
    # 「お支払いへ進む」ボタンをクリック
    proceed_to_payment_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='お支払いへ進む']/ancestor::button"))
    )
    proceed_to_payment_button.click()
    print("6.「お支払いへ進む」ボタンが正常にクリックされました。")
    # 支払いページの読み込みを待つ
    time.sleep(5)

# 7.クレジットカード支払い情報を入力（OTP認証が必要なため、スキップ）
    # iframe_number = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.XPATH, "//iframe[contains(@name, 'card-fields-number')]"))
    # )
    # driver.switch_to.frame(iframe_number)
    # card_number_input = driver.find_element(By.NAME, "number")
    # card_number_input.send_keys(config.card_number)
    # driver.switch_to.default_content()
    # iframe_name = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.XPATH, "//iframe[contains(@name, 'card-fields-name')]"))
    # )
    # driver.switch_to.frame(iframe_name)
    # card_name_input = driver.find_element(By.NAME, "name")
    # card_name_input.send_keys(config.card_name)
    # driver.switch_to.default_content()
    # iframe_expiry = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.XPATH, "//iframe[contains(@name, 'card-fields-expiry')]"))
    # )
    # driver.switch_to.frame(iframe_expiry)
    # card_expiry_input = driver.find_element
    # (By.NAME, "expiry")
    # # 先に月を入力
    # card_expiry_input.send_keys(config.card_expiry_month)
    # time.sleep(1)  # 一秒待つ
    # # 次に年を入力
    # card_expiry_input.send_keys(config.card_expiry_year)
    # driver.switch_to.default_content()
    # time.sleep(3)
    # iframe_verification = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.XPATH, "//iframe[contains(@name, 'card-fields-verification')]"))
    # )
    # driver.switch_to.frame(iframe_verification)
    # card_verification_value_input = driver.find_element(By.NAME, "verification_value")
    # card_verification_value_input.send_keys(config.card_verification)
    # driver.switch_to.default_content()
    # # 入力に問題がないことを確認するために少し待つ
    # time.sleep(5)
    print("7.SKIP")
# 8. Amazon Payを選択
    amazon_pay_radio = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "checkout_payment_gateway_39563100208"))
    )
    amazon_pay_radio.click()    
    print("8.Amazon Payを選択しました。") 
    # 「今すぐ支払う」ボタンをクリック
    pay_now_button = driver.find_element(By.ID, "continue_button")
    pay_now_button.click()
    # Amazon Payのログインページに遷移するのを待つ
    time.sleep(5)

# 9. Amazon Payのログインページでメールアドレスとパスワードを入力
    amazon_email_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "ap_email"))
    )
    amazon_password_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "ap_password"))
    )
    amazon_email_input.send_keys(config.amazon_account)
    amazon_password_input.send_keys(config.amazon_password)
    # 「signin」ボタンをクリック
    amazon_login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "signInSubmit"))
    )
    amazon_login_button.click()
    print("9.「signin」ボタンが正常にクリックされました。")
    time.sleep(5)
    # Amazon Payの配送方法ページに遷移するのを待つ

# 10. Amazon Payのページでデフォルトの配送情報を選択
    distribution_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='continue_button']/span[text()='配送方法の選択へ進む']/.."))
    )
    distribution_button.click()
    print("10.Amazon Payの「配送方法の選択へ進む」ボタンが正常にクリックされました。")
    time.sleep(5)
    # Amazon Payの支払い方法ページに遷移するのを待つ

# 11. Amazon Payのページでデフォルトのクレジットカード情報を選択
    payment_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='continue_button']/span[text()='お支払いへ進む']/.."))
    )
    payment_button.click()
    print("11.Amazon Payの「お支払いへ進む」ボタンが正常にクリックされました。")

# 12. 最後のチェックアウトページで「ご注文完了」ボタンをクリック
    order_complete_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='continue_button']/span[text()='ご注文完了']/.."))
    )
    order_complete_button.click()
    print("12.「ご注文完了」ボタンが正常にクリックされました。")
    # 買い物が成功したことを確認するために少し待つ
    time.sleep(10)

# 13. 成功メールを送信
    # メールサーバーの設定
    smtp_server = "smtp.mail.me.com"
    smtp_port = 587
    smtp_user = config.icloud_account
    smtp_password = config.icloud_password
    # メールメッセージを作成
    msg = MIMEText("購入成功テスト")
    msg["From"] = smtp_user
    msg["To"] = ", ".join([config.amazon_account, config.mail2]) 
    msg["Subject"] = "Blue Bottle Coffeeの購入通知テスト"
    # SMTPサーバーに接続してメールを送信
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(smtp_user, [config.amazon_account, config.mail2], msg.as_string())
    print("13.メールが正常に送信されました。")
    server.quit()

except Exception as e:
    print(f"実行中にエラーが発生しました: {e}")

# ブラウザを開いたままにし、プログラムを終了するためにユーザー入力を待つ
# input("操作が完了しました。ブラウザは開いたままです。プログラムを終了してブラウザを閉じるにはEnterキーを押してください...")
