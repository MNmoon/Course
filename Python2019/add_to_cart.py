#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import  unittest

class Assert_test(unittest.TestCase):
    def setUp(self):
        #chrome driver storage location
        self.chromedriver = '/Users/zhangyi/Documents/Chrome_driver/chromedriver'
        #expect price
        self.expect_price = '47.30'


    def test_case(self):
        #get actual price from amazon
        actual_price = self.get_price()
        try:
            #success when two values are equal
            self.assertEqual(self.expect_price, actual_price, msg=None)
            #if two values not equal,print prompt message
        except Exception as e:
            print 'Fail,actual price:{0}  expect price:{1}'.format(actual_price,expect_price)

    def get_price(self):
        """
        :return:actual price of book
        """
        #use webdriver to start up browser
        wd = webdriver.Chrome(self.chromedriver)
        #When looking for an element or element does not appear immediately, the implicit wait will wait for a while to find
        #will slow down test case execution
        wd.implicitly_wait(3)
        #open  web page
        wd.get('https://www.amazon.com/')
        #find the id of search box
        element = wd.find_element_by_id('twotabsearchtextbox')
        #Enter the software test and hit enter
        element.send_keys('软件测试\n'.decode('utf-8'))

        #Find software test (2nd version of the original book)
        link = wd.find_element_by_xpath(
            '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[1]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div/h2/a')

        #get the href to page:software test (2nd version of the original book)
        new_url = link.get_attribute('href')
        #open the page of software test (2nd version of the original book)
        wd.get(new_url)

        #add to cart
        ele = wd.find_element_by_css_selector('input#add-to-cart-button')
        # get actual price
        price_content = wd.find_element_by_xpath('//*[@id="a-autoid-4-announce"]/span[2]/span')
        #extract price from price_content
        price = str(price_content.text).split('$')[-1]
        #close browser
        wd.quit()
        #return actual price
        return price

    def tearDown(self):
        pass

if __name__ == "__main__":

    unittest.main()