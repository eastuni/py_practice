
# 끝내려면 문자 입력

while True:

    score= input(' 점수를 입력하세요... ' )

    if  not  score.isnumeric(): break
    
    score = int(score)
    if  score >= 60 :
            print("   합격하셨습니다.")
            print("   축하드립니다.")
    else:
            print("   안타깝군요 다음기회를.....")  
