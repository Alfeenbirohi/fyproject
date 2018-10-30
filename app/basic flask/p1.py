from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
  title="Python Flask Workshop"
  my_dict={1:'Alfeen',2:'mani',3:'Siddhesh'}
  my_tup=('Sid','Adarsh','Kunal','Nikhil')
  return render_template('temp.html',name1=my_dict,name=title,name2=my_tup)

if __name__=='__main__':
  app.run(debug=True)
  
