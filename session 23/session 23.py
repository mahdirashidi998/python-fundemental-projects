class Mytime:
    def  __init__(self,hour,minute,second):
        self.h = hour
        self.m = minute
        self.s = second
    def  __str__(self):
        a = '{0}:{1}:{2}'.format(self.h,self.m,self.s)
        return a
    def  increment(self,secs):
        return to_hour(self.to_secs() + secs)
        
    def  to_secs(self):
        return (self.h * 3600 + self.m * 60 + self.s)
    def  between(self,t1,t2):
        return (t1.to_secs() <= self.to_secs() and t2.to_secs() > self.to_secs())
    def  __gt__(self,t1):
        return (self.to_secs() > t1.to_secs())
def  add_time(t1,t2):
    h = t1.h + t2.h
    m = t1.m + t2.m
    s = t1.s + t2.s
    if s >= 60:
        m += 1
        s -= 60
    if m >= 60:
        h+=1
        m -=60

    t = Mytime(h,m,s)
    return t
def  to_hour(t1):
    h = t1 // 3600
    t1 = t1 - (t1 // 3600) * 3600
    m = t1//60
    t1 = t1 - (t1 // 60) * 60
    s = t1
    return Mytime(h,m,s)
t1 = Mytime(2,12,44)
t2 = Mytime(3,12,24)
t3 = Mytime(2,16,3)
print(t1.increment(3614))