import sqlite3

# Output a report in your terminal that lists all students and the exerices each is assigned. Use a dictionary to track each exercise. Remember that the key should be the exercise id and the value should be the entire exercise object.

# Example
# Overly Excited is being worked on by:
#   * Ryan Tanay
#   * Meg Ducharme
#   * Tanner Terry

# Trestlebridge is being worked on by:
#   * Steven Holmes
#   * Kirren Covey

class PopularExercises:

    def __init__(self):
        self.db_path = "/Users/stuff/workspace/python/SQL/Ch3_StudentExercise3/student_exercise/studentexercises.db"

    def pop_exercises(self):

        with sqlite3.connect(self.db_path) as conn:

            exercises = dict()

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.name,
                    s.Id StudentId,
                    s.slack_handle,
                    s.first_name,
                    s.last_name
                from Exercise e
                join Student_Exercises se on se.ExerciseId = e.Id
                join Student s on s.Id = se.StudentId;
            """)

        dataset = db_cursor

        for row in dataset:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_slack = row[3]
            student_name = f'{row[4]} {row[5]}'

            if exercise_name not in exercises:
                exercises[exercise_name] = [student_name]
            else:
                exercises[exercise_name].append(student_name)

        for exercise_name, students in exercises.items():
            print(f'{exercise_name} is being worked on by:')
            for student in students:
                print(f'\t* {student}')


pop = PopularExercises()
pop.pop_exercises()