def grading(stud_score):
    if 90 <= stud_score <= 100:
        return 'Grade A Student'
    elif 80 <= stud_score < 90:
        return 'Grade B Student'
    elif 70 <= stud_score < 80:
        return 'Grade C Student'
    elif 60 <= stud_score < 70:
        return 'Grade D Student'
    elif 0 <= stud_score < 60:
        return 'Grade E Student'
    else:
        return 'Enter a valid grade between 0 and 100'

stud_count = int(input('Enter number of students: '))
final_result = []

for i in range(stud_count):
    stud_name = input('Enter Student Name: ')
    stud_score = int(input('Enter Student Score: '))

    grading_result = grading(stud_score)
    final_result.append([stud_name, grading_result])

print()
print('The List of Students With Respective Grades')

for name, garde in final_result:
    print(f'{name}: {garde}')




    


