import streamlit as st
import time
from PIL import Image

st.title("streamlit 超入門")
latest_iteration = st.empty()
bar = st.progress(0)
show_expander = False
img1 = Image.open("./yakei.webp")


for i in range(100):
    latest_iteration.text(f"Iteration: {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.01)
    if (i + 1) == 100:
        show_expander = True

if show_expander:
    # expanderの内部に記述したい時はexpander.writeを使う
    expander1 = st.expander("A社へのお問合せはこちら")
    expander1.write("TEL: **********")
    show_image1 = expander1.button("A社のイメージを表示する")
    if show_image1:
        expander1.image(img1)

    expander2 = st.expander("B社へのお問合せはこちら")
    expander2.write("TEL: @@@@@@@@@@")
else:
    st.write("データを読み込み中です。少々お待ちください。")
