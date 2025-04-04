class parent:
    def show(self):
        print("Inside parent")
        
class child(parent):
    def show(self):
        super().show()
        print("inside child")
obj=child()
obj.show()