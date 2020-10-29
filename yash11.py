b = ('To calculate area of a circle')

print(b)

in_ = eval(input('Enter radius of a circle:'))


if(type(in_)== int):
    print('Area of a circle' , 3.14*(in_**2))
          
elif(type(in_)== float):
    print('Area of a circle' , 3.14*(in_**2))
          
else:
    print('Enter a valid value')



     
        





