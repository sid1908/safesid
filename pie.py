from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pie(pper,nper,nuper,ptweets1,ntweets1):
    ptweets1 = ptweets1
    ntweets1 = ntweets1
    pper = pper
    nper = nper
    nuper = nuper
    
    labels = [
    'POSITIVE SENTIMENT', 'NEGATIVE SENTIMENT', 'NUETRAL SENTIMENT']

    values = [
        pper, nper, nuper]

    colors = [
        "#F7464A", "#46BFBD", "#FDB45C",]

    return render_template('pie_chart.html', title='SENTIMENT ANALYSIS', max=100, set=zip(values, labels, colors), p=ptweets1, n=ntweets1 )

if __name__ == '__main__':
    app.debug = True
    app.run()
