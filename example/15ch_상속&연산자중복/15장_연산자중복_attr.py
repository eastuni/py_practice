class Myclass:

    class_name = "Myclass"
    
    def __getattr__(self, name):
        print(name, " 속성은 없습니다." )
        
    def __setattr__(self, name, value):
        print(name, "속성을 ", value, 
            "로 변경요청이 들어왔습니다.")
        
    def __str__(self):
        return str(Myclass ) + " <----클래스명"
    
c = Myclass()

print(c.class_name)
print(c.name)
print(c.data)
c.class_name="good class"
print(c.class_name)
print(str(c))
