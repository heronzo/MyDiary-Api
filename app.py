from flask import Flask,jsonify

app=Flask(__name__)

entries =[
        {
            'id':1,
            'title':'Meeting',
            'description':'I have a meeting today with my team',
            'date':'19/07/2018'
        },
        {
            'id':2,
            'title':'Study',
            'description':'I need to study java',
            'date':'20/07/2018'
        },
        {
            'id':3,
            'title':'Play',
            'description':'I have a football match today',
            'date':'22/07/2018'
        },
        {
            'id':4,
            'title':'Work',
            'description':'Today i have a lot of work. I must update the whole customer logbook',
            'date':'23/07/2018'
        }
]

if __name__=="__main__":
    app.run(debug=True)