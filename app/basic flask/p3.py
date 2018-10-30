from flask import Flask, render_template
app=Flask(__name__)

@app.route('/index')
def  index():
  user = {'username':'Dhiraj'}
  posts=[
    {
          'author':{'username':'Daniel'},
          'body': 'Beautiful day in Sri lanka!'
          },
    {
          'author':{'username':'Amar'},
          'body': 'Tiger Zinda hai movie was so cool!'
    }
  ]
  return render_template('temp.html', user=user , posts=posts)
if __name__=='__main__':
  app.run(debug=True)
