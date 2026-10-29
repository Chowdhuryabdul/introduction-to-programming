class Exam:
    def __init__(self, exam_name):
        self.exam_name = exam_name
    
    def attend_in_exam(self, student_name):
       
            print (f'the {student_name} have attended in the exam')
        
    def mark(self, exam_mark, student_name):
        if exam_mark > 80:
            print (f'{student_name} has got the A+ as the mark: {exam_mark}')
        elif exam_mark < 80:
            print(f'{student_name} has got the A- as the mark is: {exam_mark}')



student1 = Exam('Bangla')
student1.attend_in_exam('rahim')
student1.mark(65, 'rahim')

student2 = Exam ('English')
student2.attend_in_exam('Karim')
student2.mark( 87, 'karim')