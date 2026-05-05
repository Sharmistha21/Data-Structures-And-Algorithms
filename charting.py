import plotly.express as px

df=px.data.iris()
fig=px.line(df,y="sepal_width",line_dash='species',color='species')
fig.show()

df=px.data.tips()
fig=px.bar(df,x='day',y='total_bill',color='sex',facet_row='time',facet_col='sex')
fig.show()