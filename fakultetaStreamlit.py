import streamlit as st
def fakulteta(n):
    n = int(n)
    if n<0:
        return "Število mora biti pozitivno!"
    F = 1
    n0=n

    while n > 1:
        F = F * n
        n = n - 1
    return F

st.title('Izračun fakultete')

n = st.number_input('Naravno število, za katerega želite izračunati fakuleto: ',value=0)

odTxt=fakulteta(n)
st.write(f"Fakulteta števila {n} je {odTxt}")


