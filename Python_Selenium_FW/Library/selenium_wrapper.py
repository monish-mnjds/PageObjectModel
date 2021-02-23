from Library import *


class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver
    
    @wait_
    def enter_text(self, element, *, value):
        locator_type, locator_value = element
        self.driver.find_element(locator_type, locator_value).clear()
        self.driver.find_element(locator_type, locator_value).send_keys(str(value))
    
    @wait_
    def click_element(self, element):
        locator_type, locator_value = element
        self.driver.find_element(locator_type, locator_value).click()
    
    @wait_
    def select_list_item(self, element, *, item):
        locator_type, locator_value = element
        web_element = self.driver.find_element(locator_type, locator_value)
        select = Select(web_element)
        if isinstance(item, str):
            select.select_by_visible_text(item)
        else:
            select.select_by_index(item)
    
    @wait_
    def select_multiple_items(self, element, *, items):
        for item in items:
            self.select_list_item(element, item=item)

    @wait_
    def get_current_selected_item(self, element):
        locator_type, locator_value = element
        web_element = self.driver.find_element(locator_type, locator_value)
        select = Select(web_element)
        return select.first_selected_option.text

    @wait_
    def send_keyboard_input(self, key):
        time.sleep(1)
        if key.upper() not in {'ARROW_DOWN', 'ARROW_UP', 'BACK_SPACE', 'TAB', 'ENTER', 'PAGE_DOWN'}:
            raise ValueError('Keys Can be ',{'ARROW_DOWN', 'ARROW_UP', 'BACK_SPACE', 'TAB', 'ENTER', 'PAGE_DOWN'})
        action = ActionChains(self.driver)
        if key.upper() == 'ARROW_DOWN':
            action.send_keys(Keys.ARROW_DOWN).perform()
        elif key.upper() == 'ARROW_UP':
            action.send_keys(Keys.ARROW_UP).perform()
        elif key.upper() == 'BACK_SPACE':
            action.send_keys(Keys.BACK_SPACE).perform()
        elif key.upper() == 'ESCAPE':
            action.send_keys(Keys.ESCAPE).perform()
        elif key.upper() == 'TAB':
            action.send_keys(Keys.TAB).perform()
        elif key.upper() == 'ENTER':
            action.send_keys(Keys.ENTER).perform()
    
    @wait_
    def mouse_hover(self, element):
        locator_type, locator_value = element
        action = ActionChains(self.driver)
        element = self.driver.find_element(locator_type, locator_value)
        action.move_to_element(element).perform()
    
    @wait_(is_alert=True)
    def accept_alert(self):
        alert = Alert(self.driver)
        self.driver.switch_to.alert()
        alert.accept()
    
    @wait_(is_alert=True)
    def dismiss_alert(self):
        alert = Alert(self.driver)
        self.driver.switch_to.alert()
        alert.dismiss()
    
    @wait_(is_alert=True)
    def get_alert_text(self):
        alert = Alert(self.driver)
        self.driver.switch_to.alert()
        return alert.text.strip() if alert.text.strip() else None

    @wait_(enabled=False)
    def get_element_text(self, element):
        locator_type, locator_value = element
        element = self.driver.find_element(locator_type, locator_value)
        return element.text.strip()
    
    def switch_to_window(self, window_index):
        if window_index < len(self.driver.window_handles):
            win_handles = self.driver.window_handles
            self.driver.switch_to.window(win_handles[window_index])
        else:
            raise NoSuchWindowException(f'Window index :{window_index} does not exist')
    
    def switch_to_parent_window(self):
        win_handles = self.driver.window_handles
        self.driver.switch_to.window(win_handles[0])
    
    def close_window(self, window_index):
        win_handles = self.driver.window_handles
        if window_index < len(win_handles):
            win_handles = self.driver.window_handles
            self.driver.switch_to.window(win_handles[window_index])
            self.driver.close()
        else:
            raise NoSuchWindowException(f'Window index :{window_index} does not exist')
    
    def close_all_child_window(self):
        handles = self.driver.window_handles
        for index in range(1, len(handles)):
            self.driver.switch_to.window(handles[index])
            self.driver.close()

    def get_page_title(self):
        return self.driver.title.strip()
    
    def get_web_elements(self, element):
        locator_type, locator_value = element
        return self.driver.find_elements(locator_type, locator_value)

    @staticmethod
    def get_date_time_stamp():
        temp_date_time = datetime.datetime.now()
        return str(temp_date_time)[:19].replace(':', '').replace(' ', '_').replace('-', '_')
    
    @staticmethod
    def get_random_number():
        """Returns 6 Digit Random Number"""
        temp_date_time = datetime.datetime.now()
        return str(temp_date_time)[20:]

    @wait_(enabled=False, timeout=5)
    def wait_for_element(self, element):
        pass
