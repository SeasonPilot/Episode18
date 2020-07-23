from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage



class LoginPage(BasePage):
    _close_locator=(By.ID, "iv_close")
    _other_locator=(By.ID, "tv_login_by_phone_or_others")
    _register_phone_number=(By.ID, "register_phone_number")
    _register_code=(By.ID, "register_code")
    _button_next=(By.ID, "button_next")
    _tv_login_with_account=(By.ID, "tv_login_with_account")
    _login_account=(By.ID, "login_account")
    _login_password=(By.ID, "login_password")
    _close2_locator=(By.ID, "iv_action_back")
    _error_msg = (By.ID, "md_content")
    _back_locator = (By.XPATH, "//*[contains(@resource-id, 'iv_close') or contains(@resource-id, 'iv_action_back')]")

    def loginByWX(self):
        return self            # 这里不是return loginWX()

    def loginByMSG(self, phone, code):
        return self

    def loginByPassword(self, account, password):
        self.find(self._other_locator).click()             # _other_locator前面要加self来访问类变量
        self.find(self._tv_login_with_account).click()
        self.find(self._login_account).send_keys(account)
        self.find(self._login_password).send_keys(password)
        self.find(self._button_next).click()
        return self

    def loginSuccesBypassword(self, account, password):
        from page_object.page.MainPage import MainPage
        return MainPage()

    def back(self):
        self.find(self._back_locator).click()
        from page_object.page.ProfilePage import ProfilePage
        return ProfilePage()

    def getErrorMsg(self):
        msg=self.find(self._error_msg).text
        self.findByText("确定").click()
        return msg