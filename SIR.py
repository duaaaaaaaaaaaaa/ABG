import streamlit as st
import matplotlib.pyplot as plt

st.title('SIR 전염병 확산 시뮬레이터')

beta  = st.slider('감염률 (β)', 0.01, 1.0, 0.3)
gamma = st.slider('회복률 (γ)', 0.01, 0.5, 0.05)
N     = st.number_input('전체 인구', value=1000)

S, I, R = N - 10, 10, 0
S_list, I_list, R_list = [], [], []

for day in range(200):
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
    new_I = beta * S * I / N
    new_R = gamma * I
    S -= new_I
    I += new_I - new_R
    R += new_R

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(S_list, label='S', color='steelblue')
ax.plot(I_list, label='I', color='tomato')
ax.plot(R_list, label='R', color='mediumseagreen')
ax.legend()
ax.grid(True, alpha=0.3)
st.pyplot(fig)
