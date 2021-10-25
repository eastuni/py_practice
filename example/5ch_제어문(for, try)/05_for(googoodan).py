while True:

    print( '\n\n' )  

    what= input( " 몇단을 원하십니까?...  " )

    if  what.isdecimal():

       what2=int(what)
       print( '\n\n' + " ******* {} 단 *******".format(what2))       

       for i  in  range(1,10):
          res= what2 * i
          print( ' {0:3d} × {1:3d} = {2:5d} '.format(what2, i, res))
   
    else:
       print( "\n 종료합니다.\n") 
       break 
