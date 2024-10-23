class multipleFunctions_in_1Class():
    def SubfiedsInAI():
        lst=['Sub - Fields in AI are :','Machine Learning','Neutral Network','Vision','Robotics']
        for i in lst:
            print(i)

    def oddEven():
        num=int(input('Enter the number: '))
        if num%2==0:
            print(f'{num} is Even number')
        else:
            print(f'{num} is odd number')

    def Elegible():
        gender=input('Your Gender:')
        age=int(input('Your age:'))
        gender_lower=gender.lower()
        if gender=='male':
            if age<=21:
                print('NOT ELIGIBILE')
            else:
                print('ELIGIBILE')
        else:
            if age<=18:
                print('NOT ELIGIBILE')
            else:
                print('ELIGIBILE')

    def Percentage():
        subject1 = int(input('Enter your subject1 mark'))
        subject2 = int(input('Enter your subject2 mark'))
        subject3 = int(input('Enter your subject3 mark'))
        subject4 = int(input('Enter your subject4 mark'))
        subject5 = int(input('Enter your subject5 mark'))
        Total=subject1+subject2+subject3+subject4+subject5
        Percentage=Total/5
        print(f'Total : {Total}')
        print(f'Percentage : {Percentage}')

    def triangle():
        height=int(input('Enter the Height:'))
        breadth=int(input('Enter the Breadth:'))
        print('Area formula:(Height*Breadth)/2')
        area = height * breadth / 2
        print(f'Area of Triangle:{area}')

    def triangle2():
        height1=int(input('Enter the Height1:'))
        height2= int(input('Enter the Height2:'))
        breadth2=int(input('Enter the Breadth:'))
        print('Perimeter formula: Height1+Height2+Breadth')
        perimeter=height1+height2+breadth2
        print(f'perimeter of Trainagle: {perimeter}')


    