from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def assign():
  h1="Dhiraj"
  my_dict={'Daniel':'Beautiful Day in Sri lanka','Amar':'Tiger Zinda hai movie as so cool!'}
  return render_template('temp.html',dict=my_dict,head=h1)

if __name__=='__main__':
  app.run(debug=True)

  
