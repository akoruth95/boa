import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    def __init__(self):
        #prod email list should be retrieved from hosted file in future
        self.prod_email_list = ["alankoruth@yahoo.com"]
        self.dev_email_list = ["akoruth95@gmail.com"]
        self.test_email_list = ["akoruth95@gmail.com"]

    def getEnvironment(self):
        if 'APP_SETTINGS' in os.environ:
            return os.environ['APP_SETTINGS']
        return 'local'
    
    def getEmailList(self):
        if 'APP_SETTINGS' in os.environ:
            if os.environ['APP_SETTINGS'] == 'production':
                return self.prod_email_list
            if os.environ['APP_SETTINGS'] == 'staging':
                return self.dev_email_list
        return self.test_email_list

    def updateProdEmailList(self):
        #should update hosted email list in future?
        return