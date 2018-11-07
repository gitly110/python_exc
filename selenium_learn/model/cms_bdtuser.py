
from model.cms_cookie_login import CookieLogin

class BdtUser(CookieLogin):
    def bdt_user(self):
        self.driver.find_element_by_xpath('//*[@id="_easyui_tree_1"]/span[1]').click()
        self.driver.find_element_by_xpath('//*[@id="_easyui_tree_6"]/span[4]').click()
        self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input3"]').send_keys()


