quetions=[
    ["Q1 Currant Railway minister of india is ?","mamtaa banerjee","ram vilash","ashwini vaishnaw","piyush gohel",3]
    3,["Q2 Which god is also known as ‘Gauri Nandan’?","Agni","Indra","Hanuman","Ganesh",4]
    ,["Q3 Which city is known as Pink City in India?","Banglore","maysore","Jaipur","Kochi",3]
    ,["Q4 Who wrote India's National Anthem?","Rabindarnath tagor","lal Bahadur Shastri","Chetan Bhagat","D .RK Narayan",4]
    ,["Q5 How many religions are there in India?","6","7","8","9",1]
    ,["Q6 When is the National Hindi Diwas celebrated?","13 Septamber","14 Septamber","14 july","15 Augest",2]
    ,["Q7 How many states are there in India?","28","29","30","31",2]
    ,["Q8 Where in India Gate located?","Agra","Punjab","Mumbai","New Delhi",4]
    ,["Q9 Who wrote Vande Mataram?","Sarat Chandra Chattopadhyay","Rabindranath Tagore","Bankim Chandra Chatterjee","Ishwar Chandra Vidyasagar",3]
    ,["Q10 Which of the following musical instruments is NOT of foreign origin ?","Tabla","flute","Sitar","violin",2]
    ,["Q11 Who was the first Indian woman to win a medal in the Olympics?","P.T. Usha","Kunjarani Devi","Bachendri Pal","Karnam Maleshwari",4]
    ,["Q12 Which of the following is not a state of India? ?","Vrindachal","Goa","Jharkhand","Chattisgarh",1]
    ,["Q13 The fine step-well complex of 'Agrasen ki Baoli' is located at","Gwalior","Amritsar","Agra","New Delhi",4]
    ,["Q14 Which Indian city hosts Indian movie industry?","Goa","Mumbai","Channai","Calcutta",2]
    ,["Q15 Which city is known as the `Silicon Valley Of India`?","Delhi","Mumbai","Channai","Banglore",4]
]
level=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
for i in range(0,len(quetions)):
    quetion = quetions[i]
    print(f"\n \nQuetion for Rs:{level[i]}")
    print(quetion[0])
    print(f"A.{quetion[1]}             B.{quetion[2]}")
    print(f"C.{quetion[3]}             D.{quetion[4]}")
    rep=int(input("enter number in between 1-4 :"))
    if(rep==quetion[-1]):
        print(f"currct answer you have won Rs {level[i]}")
        if(i == 4):
            money=10000
        elif(i == 9):
            money=320000
        elif(i == 14):
            money=10000000
    else:
        print("wromg anser")
        break

print(f"you take home is {money}")