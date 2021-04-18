import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Display Progress Bar')
'START!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

st.write('Display Image')

# チャックの有無で画像表示するか変える
if st.checkbox('Show Image'):
    img = Image.open("./sample.jpg")
    st.image(img, caption='coffee', use_column_width=True)

left, right = st.beta_columns(2)
option = left.selectbox(
    'あなたが好きな数字を押してください',
    list(range(1, 11))
)
right.write('あなたの好きな数字は、'+str(option)+'です。')

# text = st.sidebar.text_input('あなたの趣味を教えてください')
text = left.text_input('あなたの趣味を教えてください')
right.write('あなたの趣味:'+str(text))

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
condition = left.slider('あなたの今の調子は？', 0, 100, 50)
right.write('コンディション：'+str(condition))

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせに対する回答')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

sinzyuku = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.write(df)
st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
```

"""

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)
st.map(sinzyuku)
