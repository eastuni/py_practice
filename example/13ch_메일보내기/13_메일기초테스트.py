import smtplib

my_smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)
print( my_smtp)



   #보내는주소 받는주소 반드시 자신의 환경에 맞게 수정해서 테스트하세요
my_smtp.login('-----','-----')
my_smtp.sendmail("-----@gmail.com","----@gmail.com","대한민국".encode('utf-8'))




f_addr="----@gmail.com"
t_addr=['---@gmail.com', '--@naver.com', '--@daum.net', '----@daum.net']

msg='''
봄이오는 길목에서
만물이 소생하는 봄입니다.
그간 연락을 망설여 오다가
메일을 보냅니다..........'''

#여러명에게 보내기
f_addr="----@gmail.com"
t_addr=['----@gmail.com', '--@naver.com', '----@daum.net', '---@daum.net']
for one_addr in t_addr:
     my_smtp.sendmail(f_addr, one_addr, msg.encode('utf-8'))

print(" 모든메일 발송 완료")
