<h1>🫗Automated BlueBottle Product Purchase Script🫗</h1>

<h2>✨Purpose</h2>
Automate the process of purchasing limited edition products from Blue Bottle at a specified time.
<br>
<br>

![image](https://github.com/smallgirl6/buy_bluebottle/assets/111422800/e07b2ff5-540c-4eec-a185-8a02a3002c65)



<h2>✨Workflow</h2>

1. <strike>**Login Issue(Skipped):**</strike> <br>Initially, the script was supposed to log into the Blue Bottle member page, but since it requires two-factor authentication during purchase, it is more cumbersome. Therefore, the login code is commented out, and we will proceed with guest mode for purchasing.

2. **Purchase First Item:** <br>Navigate to the Blue Bottle website, click on the magnifying glass to open the search bar, enter the product name in the search bar to find the desired item, click on the item to go to the product page, and add the product to the cart.

3. **Purchase Second Item:** <br>Navigate to the Blue Bottle website, click on the magnifying glass to open the search bar, enter the product name in the search bar to find the desired item, click on the item to go to the product page, and add the product to the cart.

4. **Prepare for Checkout:** <br>After finishing shopping, select the checkbox "上記事項を確認しました" and click the "ご購入手続きへ" button.

5. **Enter Shipping Information:** <br>Fill in the shipping information and click the "配送方法の選択へ進む" button.

6. **Confirm Shipping Information:** <br>Confirm the shipping information page and click the "お支払いへ進む" button.

7. **Credit Card Payment (Skipped):**<br> Enter the new card information and click the "今すぐ支払う" button.

8. **<strike>Select Amazon Pay (Skipped):**</strike> <br>Choose Amazon Pay as the payment method and click the "今すぐ支払う" button.

9. **<strike>Amazon Pay Login (Skipped):**</strike> <br>On the Amazon Pay login page, fill in the email and password, then click the "signin" button.

10. **<strike>Select Shipping Information on Amazon Pay (Skipped):** </strike><br>On the Amazon Pay page, select the default shipping information and click the "配送方法の選択へ進む" button.

11. **<strike>Select Payment Information on Amazon Pay (Skipped):**</strike> <br>On the Amazon Pay page, select the default credit card information and click the "お支払いへ進む" button.

12. **<strike>Final Checkout (Skipped):** </strike><br>On the final checkout page, click the "ご注文完了" button.

13. **Send Success Email:** <br>Send an email notification of the successful purchase to my inbox.

**Note:** Since the purchase needs to be made at a specified time, configure the Task Scheduler to specify the time and script to be executed. Also, ensure it is set to wake the computer from sleep mode to execute the script.

![image](https://github.com/smallgirl6/buy_bluebottle/assets/111422800/ca8fc8fd-31a7-4e26-b544-8848c6d25f23)
<br>
![image](https://github.com/smallgirl6/buy_bluebottle/assets/111422800/d0498c8f-31b1-4a04-ad0c-edc726f06c0f)
