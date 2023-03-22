import streamlit as st
import pickle

dec_clf=pickle.load(open("decisiontreeclf.sav",'rb'))

dec_reg=pickle.load(open("decisionregressior.sav",'rb'))

reg_clf=pickle.load(open("randomforestclf.sav",'rb'))

reg_reg=pickle.load(open("randomforest.sav",'rb'))

svm_clf=pickle.load(open("svc.sav",'rb'))

svm_reg=pickle.load(open("svr.sav",'rb'))

st.title("Forest Fire Prediction")

col1, col2, = st.columns(2)

col3,col4 =st.columns(2)

col5,col6=st.columns(2)

col7,col8=st.columns(2)

with col1:
    ffmc = st.number_input(label="FFMC(18.7-96.2)",min_value=18.7, max_value=96.2,step=.5,format="%.1f")
   

with col2:
    dmc = st.number_input(label="DMC(1.1-291.3)",min_value=1.1, max_value=291.3,step=.5,format="%.1f")

with col3:
    dc = st.number_input(label="DC(7.9-860.6)",min_value=7.9, max_value=860.6,step=.5,format="%.1f")
    
with col4:
    isi = st.number_input(label="ISI(0.0-56.1)",min_value=0.0, max_value=56.1,step=.5,format="%.1f")
    
with col5:
    temp = st.number_input(label="TEMPERATURE(2.2-33.3)",min_value=2.2, max_value=33.3,step=.5,format="%.1f")
    
with col6:
    rh = st.number_input(label="RH(15.0-100.0)",min_value=15.0, max_value=100.0,step=.5,format="%.1f")
    
with col7:
    wind = st.number_input(label="WIND(0.4-9.4)",min_value=0.4, max_value=9.4,step=.5,format="%.1f")

with col8:
    rain = st.number_input(label="RAIN(0.0-6.4)",min_value=0.0, max_value=6.4,step=.5,format="%.1f")

model = st.selectbox(
    
    'Model',
    ('Decision Tree',"Random Forest" ,'SVM'))

if(st.button('predict')):
    values=[[ffmc,dmc,dc,isi,temp,rh,wind,rain]]
    if(model=='Decision Tree'):
        st.subheader("Decision Tree")
        dec_clf_pred=dec_clf.predict(values)
        dec_reg_pred=dec_reg.predict(values)
        
        if(dec_clf_pred==1):
            st.error("There is no fire")
        else:
            st.success("There is fire")
        st.subheader("Area")
        if(dec_reg_pred[0]==0):
            st.error(dec_reg_pred[0])
        else:
            st.success(dec_reg_pred[0])
 #---------------------------------------------------------------------------------           
    if(model=='Random Forest'):
        st.subheader("Random Forest")
        reg_clf_pred=reg_clf.predict(values)
        reg_reg_pred=reg_reg.predict(values)
        
        if(reg_clf_pred==1):
            st.error("There is no fire")
        else:
            st.success("There is fire")
        st.subheader("Area")
        if(reg_reg_pred[0]==0):
            st.error(reg_reg_pred[0])
        else:
            st.success(reg_reg_pred[0])
#----------------------------------------------------------------------------------
    if(model=='SVM'):
        st.subheader("Support Vector Machine")
        svm_clf_pred=svm_clf.predict(values)
        svm_reg_pred=svm_reg.predict(values)
        
        if(svm_clf_pred==1):
            st.error("There is no fire")
        else:
            st.success("There is fire")
        st.subheader("Area")
        if(svm_reg_pred[0]==0):
            st.error(svm_reg_pred[0])
        else:
            st.success(svm_reg_pred[0])
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
