
class Cat():
    # __init__ is the class constructor
    def __init__(self, color,breed,birthday, name,owner):
        self.color=color
        self.breed=breed
        self.birthday=birthday
        self.name=name
        self.owner=owner

cat1=Cat(color='yellow',breed='N/A',birthday='1/29',name='kk',owner='yes')
cat2=Cat(color='red',breed='N/A',birthday='2/27',name='dd',owner='no')

print(cat1.color,cat1.owner)
print(cat2.color,cat2.birthday)


@property
def name(self):
    return self.name
@name.setter
def name1(self, name1=str):
    input(name1,'input your cat name:')
    if len.name1>=5 and name1=='dog' and type.name1==int:
        print('this name is wrong')
    else:print(name1=name)







