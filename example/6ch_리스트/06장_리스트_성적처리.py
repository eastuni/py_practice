basedata='''김영민, 69, 100, 100
박동식, 100, 98, 98
최민규, 88, 96, 90
동후민, 88, 98, 97
신형균, 99, 44, 66
김철규, 88, 69, 100'''

        #캐리지리턴 키 중심으로 분리하여 리스트만듬
data = basedata.split('\n')
        #콤마로 분리하여 각 인원별 재할당  (중첩리스트)
for  i  in  range(len(data)):  
      data[i]= data[i].split(',' )
      print(data[i])                  

for  k  in range(len(data)):       #인원수 만큼 반복      
      sum=0
      for  j   in  range(1, 4):    #과목수 만큼 순환(세바퀴)
           data[k][j]=int(data[k][j]) 
           sum += data[k][j]           #세과목 합계
       
      data[k].append(sum)            #각 인원별 리스트에 합계 추가
      av = int(sum/3)                
      data[k].append(av)             #각 인원별 리스트에 평균 추가    
      print(data[k])


data.sort(key= lambda a: a[4], reverse=True)
for  k  in  range(len(data)):
          print(data[k])


for  k   in   range(len(data)):
      data[k].append(1)
for  k  in  range(len(data)):
    
     for  k2  in  range(k +1, len(data) ):
         if  data[k][4] < data[k2][4]:
               data[k][6] += 1
         elif  data[k][4] > data[k2][4]:    
               data[k2][6] += 1



print('\n             성적 처리 결과')
print('--------------------------------------------')
print("  {0:4s}  {1:2s} {2:2s}  {3:2s}   {4:2s} {5:2s}  {6:2s}  ".format('이름','국어','영어','수학','총점','평균','석차'))
print('--------------------------------------------')

for k in range(len(data)):
     print(" {0:4s}  {1:3d}  {2:3d}   {3:3d}   {4:4d}  {5:3d}  {6:3d}  ".format(data[k][0],
                                                                                			data[k][1],
                                                                                			data[k][2],
                                                                                			data[k][3],
                                                                                			data[k][4],
                                                                               			data[k][5],
                                                                               			 data[k][6]))
