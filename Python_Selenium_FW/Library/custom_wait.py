from Library import *

class element_to_be_enabled:
    """ Custom Class to check if the element is enabled """
    def __init__(self, bytype, locator):
        self.bytype = bytype
        self.locator = locator

    def __call__(self, driver):
        element = driver.find_element(self.bytype, self.locator)
        return True if element.is_enabled() else False


def wait_(func=None, *, visibility=True, enabled=True, timeout=60, is_alert=False):
    if func is None:
        return partial(wait_, visibility=visibility, enabled=enabled, timeout=timeout,
                       is_alert=is_alert)

    @wraps(func)
    def wrapper(*args, **kwargs):
        instance, element = args
        locator_type, locator = element
        wait = WebDriverWait(instance.driver, timeout, poll_frequency=0.5)
        if is_alert:
            wait.until(ec.alert_is_present(), message='Alert does not exist')
            return func(*args, **kwargs)
        if visibility:
            wait.until(ec.visibility_of_element_located((locator_type, locator)),
                       message=f'{locator} not visible after timeout period of {timeout} seconds')
            if enabled:
                wait.until(element_to_be_enabled(locator_type, locator), message = f'{locator} is enabled after timeout period of {timeout} seconds')
                if func.__name__ == 'click_element':
                    wait.until(ec.element_to_be_clickable((locator_type, locator)), message=f'{locator} is not clickable after timeout period of {timeout} seconds')
            return func(*args, **kwargs)
        else:
            time.sleep(3)
            wait.until(ec.invisibility_of_element_located((locator_type, locator)),
                       message=f'{locator} is visible after timeout period of {timeout} seconds')
            return func(*args, **kwargs)
    return wrapper
