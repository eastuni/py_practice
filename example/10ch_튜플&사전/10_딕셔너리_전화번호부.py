#전화번호.txt 파일로부터 읽어옵니다. (파일저장이 있어야합니다.)

f=open('전화번호.txt', 'r')
basedata=f.read()
f.close()

data = basedata.split('\n')  

telDic={}  

for   j   in   range(len(data)):      
     person = data[j].split(',')  
     telDic[person[0]] = person


print("\n\n                     전화번호 목록")
print("--------------------------------------------------------------------")
print("이름            전화번호           주   소            소속회사")
print("--------------------------------------------------------------------")

for  k  in  telDic:    # 사전의 아이템 수 만큼 반복
     print("{} ----> {:15s}  {:15s}  {:10s}".format(k, telDic[k][1], telDic[k][2], telDic[k][3]))    

while True:
  sName =input("\n이름을 입력하세요[끝내려면==>끝 입력]....  ")
  if sName =='끝':
      print("\n 프로그램을 끝냅니다.\n")
      break
    
  if sName in telDic:
      print(sName, " ----> ", telDic[sName])
  else:
      print("등록된 전화번호 없습니다.")
