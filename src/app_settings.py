from PyQt5.QtCore import QSettings


class ApplicationSettings(QSettings):
    
    def __init__(self, scope : str = "SprayLoc", app_name : str = "Picture Optimizer"):
        super(ApplicationSettings, self).__init__(scope,app_name)
        
        self.applicationName() 
        
    def value(self, property_name : str) -> any:
        try :
            return super().value(property_name)
        except:
            print("value not found in settings !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return None
        
    
    