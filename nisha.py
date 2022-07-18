import streamlit as st
from tensorflow.keras.models import load_model




def main():
    
    
    st.title('Prediction')
    preg=int(st.text_input("Pregnancies", 6))
    glucose=int(st.text_input("Glucose", 148))
    bp=int(st.text_input("BloodPressure", 72))
    skin=int(st.text_input("SkinThickness",35))
    insulin=int(st.text_input("Insulin",0))
    bmi=float(st.text_input("BMI", 33.6))
    dpf=float(st.text_input("DiabetesPedigreeFunction", 0.627))
    age=int(st.text_input("Age",50))

    if st.button(label="Predict"):
        pred=model.predict([[preg,glucose,bp,skin,insulin,bmi,dpf,age]])
        print(pred[0][0])
        if pred[0][0] > 0.5 :
            st.error("Person is Diabetic")
        else:
            st.success("Person is non-diabetic")
        


if __name__== "__main__" :
    model= load_model("model.h5")
    main()
