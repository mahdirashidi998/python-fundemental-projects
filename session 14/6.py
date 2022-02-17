import time
class SMS_store:
    def __init__(self):
        self.l1=[]
    def  add_new_arrival(self,tuple):
        self.l1.append((False,).__add__(tuple))
    def  massage_count(self):
        return len(self.l1)
    def  get_unread_indexes(self):
        for i in self.l1:
            li = []
            if i[0] == False :
                li.append(i[1:])
        return li
    def  get_message(self,i):
        self.l1[i] = (True,self.l1[i][1:])
        return self.l1[i][1:]
    def  delete(self,i) :
        self.l1.remove(i)
    def  clear(self):
        self.l1 = []


inbox= SMS_store()
inbox.add_new_arrival(('0912',time.localtime(time.time()),'abas qoli goft'))
print(inbox.get_unread_indexes())
