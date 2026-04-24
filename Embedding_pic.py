from deepface import DeepFace
import cv2
import numpy as np 
import os

# Hide TensorFlow warnings to focus on results
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def get_embedding(source):
    """
    Extract face embedding from a given source.
    source: can be an image path (string) or a camera frame (numpy array).
    """
    try:
        # 1. Handle case if source is a file path (string)
        if isinstance(source, str):
            if not os.path.exists(source):
                print(f"[ERROR] File does not exist at path: {source}")
                return None
            
            # Read image from disk and convert to OpenCV numpy array
            img = cv2.imread(source)
            if img is None:
                print(f"[ERROR] Could not open image, check extension: {source}")
                return None
        
        # 2. Handle case if source is a direct frame from camera
        elif isinstance(source, np.ndarray):
            img = source
        else:
            print("[ERROR] Invalid data type provided to get_embedding")
            return None

        # Convert colors from BGR (OpenCV default) to RGB (DeepFace requirement)
        rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Extract Embedding using ArcFace model
        result = DeepFace.represent(
            img_path=rgb_frame, 
            model_name="ArcFace",
            detector_backend="opencv", 
            enforce_detection=True, # Prevent crash if face is not clear
            align=True                
        )

        if result and len(result) > 0:
            return result[0]["embedding"]
        
        return None

    except Exception as e:
        print(f"[ERROR] Processing failed: {e}")
        return None  

if __name__ == "__main__":
    print("Embedding module is ready!")
    # Test example:
    # embedding = get_embedding("20241701057.jpeg")
    # if embedding: print("Success!")