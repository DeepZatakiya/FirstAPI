from flask import Flask,render_template
import os
import matplotlib
import matplotlib.pyplot as plt

app=Flask(__name__)


@app.route("/")
def dummy_api():
    plt.plot([0,1,2,3,4],[0,3,5,9,11])
    plt.xlabel('Moths')
    plt.ylabel('Books Read')
    x='C:/Users/Deep Zatakiya/OneDrive/Desktop/API/templates/2.png'
    plt.savefig(x)
    return (x)
'''
    return render_template("index.html")'''
if __name__=="__main__":
    app.run()
