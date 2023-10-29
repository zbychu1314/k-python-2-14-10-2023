#example_list = [1,2,3,4,5,6,7,8,2,3,4]
##for x in example_list
#
#lista=[x for liczba in example_list if (x:=liczba**2)]
#print(lista)
#
#############################
#x = int(input('Podaj liczbe: '))
#while x >0:
#    print(x)
#    (x:=x-1)

##############################

#liczby = [1,2,3,4,5,6,10,11,13,14]
#x=0
#while x <len(liczby) and ((liczba:=liczby[x])<=10):
#    x += 1
#    print(liczba)
#

###############################

numbers = [2,4,6,8]
def multiply_2x(number):
    return 2*number

for result in (map(multiply_2x,numbers)):
    print(result)

filtered_list=list(filter(lambda x: x >5,numbers))
print(filtered_list)

students = ['Bob', 'John', 'Tom']
grades = [3, 5, 4] 

for student, grade in zip(students,grades):
    print(f'Student {student} has grade {grade}')

skladniki = ['jajka', 'mleko', 'ser', 'wedlina']

for index, item in enumerate(skladniki,start=1):
    print(f'{index}:{item}')