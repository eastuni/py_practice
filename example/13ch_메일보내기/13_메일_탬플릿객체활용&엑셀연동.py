# 받는사람 보내는사람 모두 자신의 환경에 맞게 테스트하세요"
# 엑셀파일도 메일주소를 올바르게 입력해 테스트하세요

import smtplib
import openpyxl
from email.message import EmailMessage

str1 = ''' 님 안녕하십니까? 
     합격을 축하드립니다. 합격통지서를 소지하시고
     센터 사무실로 방문해 주시기 바랍니다.....(중략).'''

str2 =''' 님 안녕하십니까? 
     안타깝지만 이번 시험에 불합격되셨습니다. 다음기회에
     다시 응시하시기 바랍니다...(중략).'''

str3 =''' 님 안녕하십니까? 
     이번에 응시하지 않으셨군요.
     다음기회에 응시를 통해 한단계 도약하시는 계기를      
     만드시기 바랍니다....(중략)'''
    
msg_source= (str1, str2, str3)  # 튜플로 만든다

#---메일 오픈
my_smtp=smtplib.SMTP("smtp.gmail.com",587)
my_smtp.starttls()
# 자신의 환경에 맞게 ID 패스워드 맞게 테스트하세요"
my_smtp.login('-----', '-----')
 
#---엑셀 오픈
wb = openpyxl.load_workbook('test2.xlsx')
sh=wb.active


msg = EmailMessage()
msg['Subject'] = " 응시결과 안내문 "
msg['From'] = 'twotwoppp@gmail.com'

for  o_row  in sh.rows:
      u_name = o_row[0].value    # 고객명
      u_mail = o_row[3].value    # 고객메일주소 
      u_pass = o_row[4].value    # 합불여부

      msg['To'] =  u_mail

      if u_pass == 'p':
            msg_point = 0
          
      elif u_pass == 'f':
            msg_point = 1
          
      else:
            msg_point = 2                            #메시지를 조합 
         
      mymsg= u_name + msg_source[msg_point]
      msg.set_content(mymsg)      #조합된것 넣기
      my_smtp.send_message(msg)   #전송한다. 
      print(mymsg )     
      del   msg['To']        # 새로운것 넣기위해 삭제 (중요)  
      msg.clear_content()  # 새로운것 넣기위해 삭제 (중요) 
