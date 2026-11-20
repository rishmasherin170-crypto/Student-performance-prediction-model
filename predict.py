import joblib
import pandas as pd
model=joblib.load("models/student_models.pkl")
new_student=pd.DataFrame({"study_hours":[7],"attendance":[85],"previous_marks":[75]})
prediction=model.predict(new_student)
if prediction[0]==1:
    print("student result:Pass")
else:
    print("student result:Fail")
    