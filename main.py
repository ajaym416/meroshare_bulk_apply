import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

import undetected_chromedriver as uc

uc_options = uc.ChromeOptions()
uc_options.add_argument("--start-maximized")
uc_options.add_experimental_option(
    "prefs",
    {"credentials_enable_service": False, "profile.password_manager_enabled": False},
)

APPLIED_KITTA = 10
apply_btn = '//*[@id="main"]/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div[1]/div/div[2]/div/div[4]/button'


def apply_share(dp, username, password, crn, PIN):
    
    link = "https://meroshare.cdsc.com.np/#/login"
    driver.get(link)
    driver.maximize_window()
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1]",
            )
        )
    )
    time.sleep(3)
    select_dp = driver.find_element(
        by=By.XPATH,
        value="/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1]",
    )
    select_dp.click()

    enter_dp = driver.find_element(
        by=By.XPATH, value="/html/body/span/span/span[1]/input"
    )
    enter_dp.send_keys(dp)
    enter_dp.send_keys(Keys.RETURN)

    username_field = driver.find_element(
        by=By.XPATH,
        value="/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[2]/div/div/input",
    )
    username_field.send_keys(username)

    password_field = driver.find_element(
        by=By.XPATH,
        value="/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[3]/div/div/input",
    )
    password_field.send_keys(password)

    login = driver.find_element(
        by=By.XPATH,
        value="/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[4]/div/button",
    )
    time.sleep(3)

    login.click()

    time.sleep(2)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/app-dashboard/div/div[1]/nav/ul/li[8]")
        )
    )

    myasba = driver.find_element(
        by=By.XPATH, value="/html/body/app-dashboard/div/div[1]/nav/ul/li[8]"
    )
    myasba.click()

    def button_corresponding_to_company_name():
        # todo find the button by taking company name as input iterate over all the path if it matches the text then get the correspoding button//
        "/html/body/app-dashboard/div/main/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div/div/div[1]/div/span[1]"
        "/html/body/app-dashboard/div/main/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div/div/div[2]/div/div[4]/button"
        "/html/body/app-dashboard/div/main/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div/div/div[2]/div/div[4]/button"
        "/html/body/app-dashboard/div/main/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div/div/div[1]/div/span[1]"

    # # temporary apply button
    # WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH,
    #          "/html/body/app-dashboard/div/main/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div/div/div[2]/div/div[4]/button")))
    # apply_button = driver.find_element(by=By.XPATH, value=
    #     "/html/body/app-dashboard/div/main/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div/div/div[2]/div/div[4]/button")
    # apply_button.click()
    #
    # time.sleep(2)
    # temporary apply button

    # todo:
    try:
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, apply_btn))
        )
        # "/html/body/app-dashboard/div/main/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div/div/div[2]/div/div[4]/button"
        apply_button = driver.find_element(by=By.XPATH, value=apply_btn)
        apply_button.click()
    except TimeoutException:
        driver.refresh()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/app-dashboard/div/main/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div/div/div[2]/div/div[4]/button",
                )
            )
        )
        apply_button = driver.find_element(
            by=By.XPATH,
            value="/html/body/app-dashboard/div/main/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div/div/div[2]/div/div[4]/button",
        )
        apply_button.click()

    time.sleep(2)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/select",
            )
        )
    )
    select_bank = driver.find_element(
        by=By.XPATH,
        value="/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/select",
    )
    select_bank.click()

    if str(username) == alternative_crn_dp:
        print("for alternative crn invoked")
        select_bank_first_option = driver.find_element(
            by=By.XPATH,
            value="/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/select/option[3]",
        )
        select_bank_first_option.click()
    else:
        select_bank_first_option = driver.find_element(
            by=By.XPATH,
            value="/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/select/option[2]",
        )
        select_bank_first_option.click()

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="accountNumber"]'))
    )
    time.sleep(5)
    acc_num = driver.find_element(by=By.XPATH, value='//*[@id="accountNumber"]')
    acc_num.click()
    time.sleep(5)

    select_accnum_first_option = driver.find_element(
        by=By.XPATH, value='//*[@id="accountNumber"]/option[2]'
    )

    select_accnum_first_option.click()

    applied_kitta = driver.find_element(
        by=By.XPATH,
        value="/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[4]/div/div[5]/div/div/div[2]/div/input",
    )

    applied_kitta.send_keys(APPLIED_KITTA)

    enter_crn = driver.find_element(
        by=By.XPATH,
        value="/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[4]/div/div[7]/div/div/div[2]/div/input",
    )
    enter_crn.send_keys(crn)

    agreement_check_box = driver.find_element(
        by=By.XPATH,
        value="/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[1]/div/input",
    )
    agreement_check_box.click()

    time.sleep(2)

    proceed = driver.find_element(
        by=By.XPATH,
        value="/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]",
    )
    proceed.click()

    pin_field = driver.find_element(
        by=By.XPATH,
        value="/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[1]/div/div[3]/div/input",
    )
    pin_field.send_keys(PIN)
    pin_field.send_keys("\ue007")

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]",
            )
        )
    )

    final_apply_button = driver.find_element(
        by=By.XPATH,
        value="/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]",
    )
    final_apply_button.click()


if __name__ == "__main__":
    driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
    # driver = uc.Chrome(version_main=131)
    failed_list = []

    # alternative crn
    alternative_crn_dp = "01148754"

    df = pd.read_csv("dp_list.csv", dtype={"PIN": object, "username": object})
    for i, (dp, username, password, crn, PIN, name) in enumerate(df[['dp', 'username', 'password', 'crn', 'PIN', 'name']].values):
    # for i, (dp, username, password, crn, PIN, name) in enumerate(failed_list):
        if str(username) == alternative_crn_dp:
            print("alternative crm")
        try:
            # print(str(PIN))
            # print('')
            apply_share(dp, username, password, crn, str(PIN))
            time.sleep(2)
            print(f"share applied for {name}--{username}")
        except Exception as e:
            try:
                # print(str(PIN))
                # print('')
                print("trying again")
                driver.refresh()
                apply_share(dp, username, password, crn, str(PIN))
                time.sleep(2)
                print(f"share applied for {name}--{username}")
            except Exception as e:
                failed_list.append((dp, username, password, crn, PIN, name))
                print(f"problem occured while applying for-{name}")
    print(failed_list)
2
