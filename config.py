OPS = "+-*/"
ALL_CHARS = {True: "0123456789+-*/", False: "123456789"}
FIRST_GUESS = "48-32=16"
HISTORY_STR = "2+4*6=26,66/6-8=3,8-32/8=4,10+52=62,2+1+8=11,5+6+6=17,5*4-2=18,7*90=630,4*5-19=1,5+8*7=61,93-76=17,8+8+7=23,95*2=190,9+6-1=14,7+9+2=18,2*6+3=15,9*1*8=72,4*7+8=36,6*7-6=36,40*1/5=8,8-9+10=9,5*6/10=3,2+7+8=17,8-48/6=0,4*6-9=15,3+35/7=8,1+9+6=16,5*73=365,72/9/4=2,21-7-8=6,60-11=49,43*3=129,462/7=66,9*25=225,44+27=71,79-9*8=7,50*3=150,6-16/4=2,62-31=31,52/4-8=5,8+4+2=14,4+16/4=8,75+20=95,17-8-5=4,8+9-6=11,34+32=66,9/3*7=21,498/83=6,1+6+9=16,40+42=82,9+8+8=25,27/3-4=5,8+9+9=26,42/6-3=4,92*7=644,28-3*7=7,11-5-5=1,74-57=17,9*66=594,39*8=312,56+28=84,3*5+3=18,2+3*5=17,96/6/4=4,11-9+1=3,165/5=33,6*5-21=9,8*3+2=26,4+8+9=21,5*39=195,84-70=14,33-7*4=5,8*4-29=3,8-40/5=0,194/97=2,93-39=54,2*4+4=12,11-9+3=5,1-9+15=7,184/92=2,5*7+8=43,62-44=18,3*43=129,12-3*4=0,15-6-8=1,8-49/7=1,10-9+4=5,57-6*8=9,63/9-3=4,31+22=53,1-6+14=9,9*2+6=24,44-8*5=4,6+1*5=11,48/2/4=6,249/83=3,56/8-5=2,9*4+2=38,27/3-8=1,7+2+8=17,52+31=83,216/8=27,14/7+4=6,16/4-4=0,7-4+8=11,1*3+8=11,96+9=105,12-4-2=6,8/16*6=3,103-97=6,45-30=15,96/8-8=4,5*7-26=9,48/8/1=6,11+5-8=8,4+1*8=12,8-25/5=3,81-68=13,301/43=7,96-17=79,99*4=396,49-9*5=4,18/6+6=9,5*49=245,14+46=60,98-19=79,74+25=99,6*5/15=2,7*82=574,357/7=51,44-5*7=9,9+6*4=33,5*4-4=16,75-9*8=3,12/6+7=9,8-13+6=1,2*6*1=12,12/1/3=4,57-19=38,62-52=10,51-6*8=3,22-8-9=5,4+4*9=40,15-6-3=6,35-16=19,33/3-6=5,5*7-30=5,3*45=135,96-43=53,3*92=276,10+1-8=3,34+37=71,1*9*9=81,3/7*21=9,55+12=67,94-65=29,114/57=2,27+11=38,6*8+6=54,76-57=19,5*7+7=42,268/4=67,54/9/3=2,10+45=55,8*5-37=3,1*14-9=5,63+15=78,8*4-1=31,31*9=279,99-49=50,100-2=98,38+47=85,58+34=92"

class color:
    # full list: https://pkg.go.dev/github.com/whitedevops/colors
    purple = '\033[95m'
    green = '\033[92m'
    dark_grey = "\033[90m"
    ENDC = '\033[0m'

    color_encoded = [f"{dark_grey}███{ENDC}",
                    f"{purple}███{ENDC}",
                    f"{green}███{ENDC}"]
