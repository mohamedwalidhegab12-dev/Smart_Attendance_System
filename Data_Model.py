from DB_Students import insert_student  
import pickle
import numpy as np
from images import *
from Embedding_pic import get_embedding

def add_new_student():
    with open("Data_Model.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')

        name = data[0]
        student_id = data[1]
        level = data[2]
        department = data[3]
        email = data[4]
        image_path = data[5] 

        embedding = get_embedding(image_path)
        emb_blob = pickle.dumps(embedding) 

        insert_student(name, student_id, level, department, email, emb_blob)

add_new_student()    