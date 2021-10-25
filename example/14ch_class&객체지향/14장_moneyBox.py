''' 클래스 예제로서 금고(Moneybox)클래스
Moneybox 인스턴스 생성시 지점명을 입력받는다.
계좌개설시 계좌번호는 유일해야 한다. --->클래스변수

Moneybox 개설(open), 저금(deposit), 인출(withdraw), 조회(check) 메쏘드를 가지고 있다.
Moneybox는 클래스이고 지점은 인스턴스이다.
지점은 여러명의 개설자를 가질 수 있다. 

'''


class Moneybox():

    num= 0
    branch=[]
   
    def   __init__(self, branch):
          self.branch = branch
          Moneybox.branch.append(branch)
          self.account= {}

    def   open(self, name, money= 0):     #개설메쏘드
          Moneybox.num  += 1
          self.account[Moneybox.num]= [name, money]
          return Moneybox.num

    def    deposit(self, num, money):       #저축메쏘드  
         self.account[Moneybox.num][1] += money
        
    def   withdraw(self, num, money):       #인출메쏘드
         self.account[Moneybox.num][1] -= money

    def   check(self,num):                 #조회메쏘드
         return self.account[Moneybox.num][1]



if __name__ == '__main__':
    m=Moneybox("용산")                    #용산지점(인스턴스)
    a= m.open("홍길동", 2000)              #용산지점 첫번째사람
    m.deposit(a, 2000)
    print(m.check(a))

    a2=m.open("박문수", 6000)             #같은 용산지점에 두번째 사람)
    m.deposit(a2, 4000)
    m.withdraw(a2, 2000)
    print(m.check(a2))

    k=Moneybox("서초")                    #서초지점 (새로운 인스턴스)
    s=k.open('김정호')                    #서조지점 첫번째사람 
    k.deposit(s, 3000)
    print(k.check(s))

    print(Moneybox.num)
    print("mmm", m.num )
    for i in m.account:
        print(i,  m.account[i])
    print(m.branch    )
    print(Moneybox.branch)
    print(k.account)

  
                                      #10억원이 부적절한 절차를 통해 입금처리
    m.account[a][1]= 1000000000       #data hiding의 중요성 
    for i in m.account:
        print(i,m.account[i])
    m.sssss=10000
    print(m.sssss)

