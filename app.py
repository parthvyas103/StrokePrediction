import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
model=pickle.load(open('model_pickle.pkl','rb'))


def predict_stroke(gender,age, hypertension, disease, married,
       work, residence, glucose, bmi,
       smoking):
    
    if (gender == "Male"):
        gender_male=1
        gender_other=0
    elif(gender == "Other"):
        gender_male = 0
        gender_other = 1
    else:
        gender_male=0
        gender_other=0
        
        # married
    if(married=="Yes"):
        married_yes = 1
    else:
        married_yes=0

        # work  type
    if(work=='Self-employed'):
        work_type_Never_worked = 0
        work_type_Private = 0
        work_type_Self_employed = 1
        work_type_children=0
    elif(work == 'Private'):
        work_type_Never_worked = 0
        work_type_Private = 1
        work_type_Self_employed = 0
        work_type_children=0
    elif(work=="children"):
        work_type_Never_worked = 0
        work_type_Private = 0
        work_type_Self_employed = 0
        work_type_children=1
    elif(work=="Never_worked"):
        work_type_Never_worked = 1
        work_type_Private = 0
        work_type_Self_employed = 0
        work_type_children=0
    else:
        work_type_Never_worked = 0
        work_type_Private = 0
        work_type_Self_employed = 0
        work_type_children=0

        # residence type
    if (residence=="Urban"):
        Residence_type_Urban=1
    else:
        Residence_type_Urban=0

        # smoking sttaus
    if(smoking=='formerly smoked'):
        smoking_status_formerly_smoked = 1
        smoking_status_never_smoked = 0
        smoking_status_smokes = 0
    elif(smoking == 'smokes'):
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 0
        smoking_status_smokes = 1
    elif(smoking=="never smoked"):
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 1
        smoking_status_smokes = 0
    else:
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 0
        smoking_status_smokes = 0

    feature = scaler.fit_transform([[age, hypertension, disease, glucose, bmi, gender_male, gender_other, married_yes, work_type_Never_worked, work_type_Private, work_type_Self_employed, work_type_children, Residence_type_Urban,smoking_status_formerly_smoked, smoking_status_never_smoked, smoking_status_smokes]])

    prediction = model.predict(feature)[0]
        # print(prediction) 
        # 
    return prediction
        

    

def main():
    st.title("Stroke Prediction")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">CVA(Stroke) Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    gender = st.text_input("Gender","Type Here")
    age = st.text_input("Age","Type Here")
    hypertension = st.text_input("Do you suffer from hypertension?","Type Here") 
    disease = st.text_input("Do you have any genetic heart condition?","Type Here")
    married = st.text_input("Are you married?","Type Here")
    work = st.text_input("Work type?","Type Here")
    residence = st.text_input("Residence Type?","Type Here")
    glucose = st.text_input("Average Glucose Level?","Type Here") 
    bmi = st.text_input("BMI","Type Here")
    smoking = st.text_input("Do you smoke?","Type Here")
    
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> You are less likely to have a Stroke</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> You are more likely to have a Stroke</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_stroke(gender,age, hypertension, disease, married,
       work, residence, glucose, bmi,
       smoking)
        st.success('The probability of you getting stroke is {}'.format(output))

        if output > 0.5:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()