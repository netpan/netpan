class MYNUM:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
mynum1=MYNUM()
it=iter(mynum1)
for i in it:
    print(next(it))