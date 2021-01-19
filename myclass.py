class MyRouter(object):
    "this is a class that describes the characteristics of a router."
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios 
        
    def print_router(self, manuf_date):
        print("the router name is: ", self.routername)
        print("the router model is: ", self.model)
        print("the serial number of: ", self.serialno)
        print("the model and date combined: ", self.model + manuf_date)
        
        
        