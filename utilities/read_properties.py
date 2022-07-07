import configparser

conf = configparser.ConfigParser()
conf.read('C:\\Users\\Victor\\PycharmProjects\\testv11111\\Configurations\\config.ini')
class ReadProperties:
    @staticmethod
    def get_username():
        return conf.get('SectionOne', 'username_name')

    @staticmethod
    def get_password():
        return conf.get('SectionOne', 'password_name')

    @staticmethod
    def get_login_button():
        return conf.get('SectionOne', 'login_button_name')

    @staticmethod
    def get_manager_id():
        return conf.get('SectionOne', 'manager_id_xpath')
