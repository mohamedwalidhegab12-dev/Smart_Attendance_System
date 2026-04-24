import sqlite3
import numpy as np
import pickle

def compare_with_database(current_face_vector, threshold=0.4):
    try:
        if current_face_vector is None:
            print("[Warning] No face vector provided for comparison.")
            return None
        current_vector = np.array(current_face_vector).flatten()

        conn = sqlite3.connect("University.db")
        cursor = conn.cursor()
        cursor.execute("SELECT ID, Embedding FROM Students")
        rows = cursor.fetchall()
        conn.close()

        best_match_id = None
        min_dist = float("inf") 

        for student_id, stored_vector_raw in rows:
            if stored_vector_raw is None:
                continue
            
            stored_vector = np.array(pickle.loads(stored_vector_raw)).flatten()
            
            dot_product = np.dot(current_vector, stored_vector)
            norm_current = np.linalg.norm(current_vector)
            norm_stored = np.linalg.norm(stored_vector)
            
            cosine_similarity = dot_product / (norm_current * norm_stored)
            dist = 1 - cosine_similarity  
            
            if dist < threshold and dist < min_dist:
                min_dist = dist
                best_match_id = student_id

        return best_match_id

    except Exception as e:
        print(f"Database Comparison Error: {e}")
        return None