from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
from pyvirtualdisplay import Display# available since 2.26.0
import json
import time

start = time.perf_counter()

display = Display(visible=1, size=(1300,800))
display.start()
print("Enter product name")
st = input()
print(st)

driver = webdriver.Firefox(executable_path = "/home/shadrul/Downloads/geckodriver")
driver1 = webdriver.Firefox(executable_path = "/home/shadrul/Downloads/geckodriver")
# driver2 = webdriver.Firefox(executable_path = "/home/shadrul/Downloads/geckodriver")
driver1.maximize_window()
# driver2.maximize_window()

# go to websites
driver.get("https://www.flipkart.com/")
driver1.get("https://www.amazon.in/")
# driver2.get("https://www.snapdeal.com")


print (driver.title)


# find the element that's name attribute is q ()
inputElement = driver.find_element_by_name("q")
inputElement1 = driver1.find_element_by_id("twotabsearchtextbox")
# inputElement2 = driver2.find_element_by_name("keyword")


# type in the search
inputElement.send_keys(st)
inputElement1.send_keys(st)
# inputElement2.send_keys(st)

# submit the form ()
inputElement.submit()
inputElement1.submit()
# button = driver2.find_element_by_class_name("searchformButton")
# button.click()


try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the text
    WebDriverWait(driver, 20).until(EC.title_contains("Buy Products Online"))
    WebDriverWait(driver1, 20).until(EC.title_contains(st))
    # WebDriverWait(driver2, 20).until(EC.title_contains("Snapdeal.com - Online shopping India- Discounts - shop Online Perfumes, Watches, sunglasses etc"))

    # flipkart

    element_flip = driver.find_element_by_class_name("_3wU53n") 
    # acess space seprated class names  by removing space with css_selector
    p_element_flip = driver.find_element(By.CSS_SELECTOR,"._1vC4OE._2rQ-NK")
    mrp_element_flip = driver.find_element(By.CSS_SELECTOR,"._3auQ3N._2GcJzG")
    discount_element_flip = driver.find_element(By.CSS_SELECTOR,".VGWI6T")
    print("---------FLIPKART---------")
    print ("Product Name: ",element_flip.text)
    print("price: ",p_element_flip.text)
    print("mrp: ",mrp_element_flip.text)
    print("discount: ",discount_element_flip.text)
    print("\n \n")

    product={
    "name": element_flip.text,
    # "feature": feature_element.text,
    "price": p_element_flip.text,
    "mrp":mrp_element_flip.text,
    "discount": discount_element_flip.text
    }
    with open('productData.json', 'w') as outfile:
     json.dump(product, outfile)

    # amazon

    element_ama = driver1.find_element(By.CSS_SELECTOR,".a-size-medium.a-color-base.a-text-normal")
    # acess space seprated class names  by removing space with css_selector
    p_element_ama = driver1.find_elements_by_class_name("a-price")
    rating_ama = driver1.find_element(By.CSS_SELECTOR,".a-size-base.a-color-secondary")
    print("--------amazon---------")
    print("-->Product Name:   ",element_ama.text)
    print("-->price:          ",p_element_ama[0].text)
    print("-->mrp:            ",p_element_ama[1].text)
    print("-->Rating:   ",rating_ama.text)
    product_ama={
    "name": element_ama.text,
    # "feature": feature_element.text,
    "price": p_element_ama[0].text,
    "mrp":p_element_ama[1].text,
    "rating": rating_ama.text
    }
    with open('product_info.json', 'w') as outfile:
     json.dump(product_ama, outfile)
    print("\n \n")

    # create object and save the data to json file 
    # product={
    # "name": element.text,
    # "price": p_element.text,
    # "mrp":mrp_element.text,
    # "discount": discount_element.text
    # }
    # with open('productData.json', 'w') as outfile:
    #  json.dump(product, outfile)

    # snapdeal
    # product_button = driver2.find_element_by_class_name("picture-elem")
    # product_button.click()
    # tabs = driver2.window_handles

    # driver2.switch_to.window(tabs[1])

    # WebDriverWait(driver2,20).until(EC.title_contains("Snapdeal"))
    # element_snap = driver2.find_element(By.CSS_SELECTOR,".pdp-e-i-head")
    # # acess space seprated class names  by removing space with css_selector
    # p_element_snap = driver2.find_element(By.CSS_SELECTOR,".pdp-final-price")
    # mrp_element_snap = driver2.find_element(By.CSS_SELECTOR,".pdpCutPrice")
    # offers_snap = driver2.find_elements(By.CSS_SELECTOR,".genericOfferClass.electronics")
    # rating_snap= driver2.find_element(By.CSS_SELECTOR,".avrg-rating")
    # picture_snap = driver2.find_element(By.CSS_SELECTOR,".cloudzoom").get_attribute("src")

    # print("---------SNAPDEAL----------")
    # print("-->Product Name:   ",element_snap.text)
    # #print("-->features:        ",feature_element.text)
    # print("-->price:          ",p_element_snap.text)
    # print("-->mrp:            ",mrp_element_snap.text)
    # print("---->OFFERS:")
    # for offer in offers_snap:
    #     print(offer.text)
    # print("---->picture link:",picture_snap)
    # print("---->rate:",rating_snap.text)
    # print("#"*20)
    # print("\n \n")
    # product_snap={
    # "name": element_snap.text,
    # # "feature": feature_element.text,
    # "price": p_element_snap.text,
    # "mrp":mrp_element_snap.text,
    # "rating": rating_snap.text
    # }
    # with open('product_store.json', 'w') as outfile:
    #  json.dump(product_snap, outfile)

    # driver2.switch_to.window(tabs[0])
    

except NoSuchElementException:
    # flipkart
    element = driver.find_element_by_class_name("_2cLu-l")
    p_element = driver.find_element_by_class_name("_1vC4OE")
    mrp_element = driver.find_element_by_class_name("_3auQ3N")
    discount_element = driver.find_element_by_class_name("VGWI6T")

     # create object and save the data to json file 
    # product={
    # "name": element.text,
    # "price": p_element.text,
    # "mrp":mrp_element.text,
    # "discount": discount_element.text
    # }
    # with open('productData.json', 'w') as outfile:
    #  json.dump(product, outfile)

    print ("-->Product Name: ",element.text)
    print("-->price: ",p_element.text)
    print("-->mrp: ",mrp_element.text)
    print("-->discount: ",discount_element.text)
    print("\n \n")

    product={
    "name": element_flip.text,
    # "feature": feature_element.text,
    "price": p_element_flip.text,
    "mrp":mrp_element_flip.text,
    "discount": discount_element_flip.text
    }
    with open('productData.json', 'w') as outfile:
     json.dump(product, outfile)

    # amazon
    element = driver1.find_element(By.CSS_SELECTOR,".a-size-medium.a-color-base.a-text-normal")
    # acess space seprated class names  by removing space with css_selector
    p_element = driver1.find_elements_by_class_name("a-price")
    rating_ama = driver1.find_element(By.CSS_SELECTOR,".a-size-base.a-color-secondary")
    print("-->Product Name:   ",element.text)
    print("-->price:          ",p_element[0].text)
    print("-->mrp:            ",p_element[1].text)
    print("-->Rating:   ",rating_ama.text)
    print("\n \n")

    product_ama={
    "name": element_ama.text,
    # "feature": feature_element.text,
    "price": p_element_ama[0].text,
    "mrp":p_element_ama[1].text,
    "rating": rating_ama.text
    }
    with open('product_info.json', 'w') as outfile:
     json.dump(product_ama, outfile)
    print("\n \n")

    # snapdeal
    # product_button = driver2.find_element_by_class_name("picture-elem")
    # product_button.click()
    # tabs = driver2.window_handles

    # driver2.switch_to.window(tabs[1])

    # WebDriverWait(driver2,20).until(EC.title_contains("Snapdeal"))

    
    # element_snap = driver2.find_element(By.CSS_SELECTOR,".pdp-e-i-head")
    # # acess space seprated class names  by removing space with css_selector
    # p_element_snap = driver2.find_element(By.CSS_SELECTOR,".pdp-final-price")
    # mrp_element_snap = driver2.find_element(By.CSS_SELECTOR,".pdpCutPrice")
    # offers_snap = driver2.find_elements(By.CSS_SELECTOR,".genericOfferClass.electronics")
    # rating_snap= driver2.find_element(By.CSS_SELECTOR,".avrg-rating")
    # picture_snap = driver2.find_element(By.CSS_SELECTOR,".cloudzoom").get_attribute("src")

    # print("SNAPDEAL......")
    # print("-->Product Name:   ",element_snap.text)
    # #print("-->features:        ",feature_element.text)
    # print("-->price:          ",p_element_snap.text)
    # print("-->mrp:            ",mrp_element_snap.text)
    # print("-->OFFERS:")
    # for offer in offers_snap:
    #     print(offer.text)
    # print("-->picture link:",picture_snap)
    # print("-->rate:",rating_snap.text)
    # print("\n \n")

    # product_snap={
    # "name": element_snap.text,
    # # "feature": feature_element.text,
    # "price": p_element_snap.text,
    # "mrp":mrp_element_snap.text,
    # "rating": rating_snap.text
    # }
    # with open('product_store.json', 'w') as outfile:
    #  json.dump(product_snap, outfile)

    # driver2.switch_to.window(tabs[0])


finally:
    driver.quit()
    finish = time.perf_counter()
    print('Finished in {seconds} second(s)',finish-start)    
display.stop()

