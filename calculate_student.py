from dal import Repository
import random
import re
import json
# import matplotlib.pyplot as plt
import logging
import numpy
import mysql.connector


log = logging.getLogger(__name__)

"""
 Takes a dict of student ids with filename of corresponding student's exam paper
 Opens answer key, compares answers, and assigns a percentage grade
"""
class CalculateStudent():
    repo = Repository()

    def calculate(self, student_answers):
        for student, answer in student_answers.items():
            stu = repo.get_student(student)

            try:
                answers_file = open("answer_key.txt")
                answers = answers_file.readlines()
                answers_file.close()

                my_obj = open(answer)
                answers2 = my_obj.readlines()
                my_obj.close()

                wrong = 0
                for i in range(len(answers)):
                    if answers[i] != answers2[i]:
                        wrong += 1

                result = ((len(answers) - wrong)//len(answers)) * 100
            except:
                log.error("error")

            stu.results.add(result)
            repo.update(stu)

