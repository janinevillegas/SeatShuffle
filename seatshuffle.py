import random
import streamlit as st


cs111 = ["Arwah", "Adetola", "Landon", "Cristian", "Nelstar", "Suhaib", "Deandre", "An Doan", "Ahmad", "Jose", "Owen", "Kennedy",
    "Mira", "Emily", "Krisha", "Dustin", "Noah", "Olek", "Mohamed", "Tooba", "Ruben", "Khoa", "Leonardo", "Olivia", "Huy",
    "Timothy", "David", "An Vo", "Grace"]


class_length = 28
group1 = []

for i in range(4):
    num = random.randint(0, class_length)
    group1.append(cs111[num])
    class_length -= 1
    cs111.pop(num)

group2 = []
for i in range(4):
    num = random.randint(0, class_length)
    group2.append(cs111[num])
    class_length -= 1
    cs111.pop(num)

group3 = []
for i in range(4):
    num = random.randint(0, class_length)
    group3.append(cs111[num])
    class_length -= 1
    cs111.pop(num)

group4 = []
for i in range(4):
    num = random.randint(0, class_length)
    group4.append(cs111[num])
    class_length -= 1
    cs111.pop(num)

group5 = []
for i in range(4):
    num = random.randint(0, class_length)
    group5.append(cs111[num])
    class_length -= 1
    cs111.pop(num)

group6 = []
for i in range(4):
    num = random.randint(0, class_length)
    group6.append(cs111[num])
    class_length -= 1
    cs111.pop(num)

group7 = cs111


st.title("CS 111 Seat Shuffle - Prof. Bello")

st.markdown("""
<style>
.box {
    background-color: #ffe3f6;  /* box color */
    border: 2px solid #1f0617;  /* border color */
    border-radius: 10px;
    padding: 20px;
    height: 100px;
    width: 100px;
    box-sizing: border-box;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    color: #611045;              /* text color */
}

.box h3 {
    color: #1f0617;              /* heading color */
    margin-top: 0;
    font-size: 16px;
}

.box p {
    color: #1f0617;              /* paragraph color */
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.table {
    background-color: #ffe3f6;  /* box color */
    border: 2px solid #1f0617;  /* border color */
    border-radius: 10px;
    padding: 8px;
    height: 160px;
    width: 120px;
    box-sizing: border-box;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    color: #1f0617;              /* text color */
}

.table h3 {
    color: #1f0617;              /* heading color */
    margin-top: 0;
    font-size: 16px;
    text-align: center;
}

.table p {
    color: #1f0617;              /* paragraph color */
    font-size: 12px;
    line-height: 0.8;
}
</style>
""", unsafe_allow_html=True)



col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="box">
        <h3>Podium</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<br>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="table">
        <h3>Table 1</h3>
        <p>{group1[0]}</p>
        <p>{group1[1]}</p>
        <p>{group1[2]}</p>
        <p>{group1[3]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<br>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="table">
        <h3>Table 2</h3>
        <p>{group2[0]}</p>
        <p>{group2[1]}</p>
        <p>{group2[2]}</p>
        <p>{group2[3]}</p>
    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown(f"""
    <div class="table">
        <h3>Table 3</h3>
        <p>n/a</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<br>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="table">
        <h3>Table 4</h3>
        <p>{group3[0]}</p>
        <p>{group3[1]}</p>
        <p>{group3[2]}</p>
        <p>{group3[3]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<br>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="table">
        <h3>Table 5</h3>
        <p>{group4[0]}</p>
        <p>{group4[1]}</p>
        <p>{group4[2]}</p>
        <p>{group4[3]}</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="table">
        <h3>Table 6</h3>
        <p>{group5[0]}</p>
        <p>{group5[1]}</p>
        <p>{group5[2]}</p>
        <p>{group5[3]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<br>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="table">
        <h3>Table 7</h3>
        <p>{group6[0]}</p>
        <p>{group6[1]}</p>
        <p>{group6[2]}</p>
        <p>{group6[3]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<br>""", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="table">
        <h3>Table 8</h3>
        <p>{group7[0]}</p>
        <p>{group7[1]}</p>
        <p>{group7[2]}</p>
        <p>{group7[3]}</p>
        <p>{group7[4]}</p>
    </div>
    """, unsafe_allow_html=True)

with col4:

    if st.button("Shuffle Seats", width="stretch", type="secondary"):
        st.rerun()
