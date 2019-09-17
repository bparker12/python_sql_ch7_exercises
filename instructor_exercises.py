import sqlite3
# List all exercises assigned by each instructor. Display each instructor name and the exercises s/he has assigned beneath their name. Use a dictionary to track each instructor. Remember that the key should be the instructor id and the value should be the entire instructor object.

# Joe Shepherd has assigned:
#     * Urban Planner

# Andy Collins has assigned:
#     * Stock Report
#     * Bag o Loot
#     * Kandy Korner

class InstructorExercise:

    def __init__(self):
        self.db_path = "/Users/stuff/workspace/python/SQL/Ch3_StudentExercise3/student_exercise/studentexercises.db"

    def student_workload(self):

        with sqlite3.connect(self.db_path) as conn:
            instructors = dict()

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.name,
                    i.Id InstructorId,
                    i.slack_handle,
                    i.speciality,
                    i.first_name,
                    i.last_name
                from Exercise e
                join Student_Exercises se on se.ExerciseId = e.Id
                join Instructor i on i.Id = se.StudentId;
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row [1]
                instructor_id = row[2]
                slack_handle = row[3]
                speciality = row[4]
                instructor_name = f'{row[5]} {row[6]}'

                if instructor_name not in instructors:
                    instructors[instructor_name] = [exercise_name]
                else:
                    instructors[instructor_name].append(exercise_name)

            for instructor_name, exercises in instructors.items():
                print(instructor_name)
                for exercise in exercises:
                    print(f'\t* {exercise}')

slavedriving = InstructorExercise()
slavedriving.student_workload()