# İçe aktar
from flask import Flask, render_template,request, redirect
# Veri tabanı kitaplığını bağlama
from flask_sqlalchemy import SQLAlchemy
from speech_recog import speech_tr, speech_eng
import speech_recognition
from ozet import summarization


app = Flask(__name__)
# SQLite'ı bağlama
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veri tabanı oluşturma
db = SQLAlchemy(app)
# Tablo oluşturma

class Card(db.Model):
    # Sütun oluşturma
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Başlık
    title = db.Column(db.String(100), nullable=False)
    # Tanım
    subtitle = db.Column(db.String(300), nullable=False)
    # Metin
    text = db.Column(db.String, nullable=False)

    # Nesnenin ve kimliğin çıktısı
    def __repr__(self):
        return f'<Card {self.id}>'
    

#Ödev #2. Kullanıcı tablosunu oluşturun
class User(db.Model):
    # Sütunları oluşturma
     # kimlik
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'



# İçerik sayfasını çalıştırma
@app.route('/', methods=['GET','POST'])
def login():
        error = ''
        if request.method == 'POST':
            form_username = request.form['username']
            form_password = request.form['password']
            
            #Ödev #4. yetkilendirmeyi uygulamak
            users_db = User.query.all()
            for user in users_db:
                if form_username == user.username and form_password == user.password:
                    return redirect('/index')
            else:
                error = 'Incorrect username or password'
                return render_template('login.html', error=error)

            
        else:
            return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        username= request.form['username']
        password = request.form['password']
        
        #Ödev #3 Kullanıcı verilerinin veri tabanına kaydedilmesini sağlayın
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        
        return redirect('/')
    
    else:    
        return render_template('registration.html')


# İçerik sayfasını çalıştırma
@app.route('/index')
def index():
    # Veri tabanı girişlerini görüntüleme
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

# Kayıt sayfasını çalıştırma
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)

    return render_template('card.html', card=card)

# Giriş oluşturma sayfasını çalıştırma
@app.route('/create')
def create():
    return render_template('create_card.html')

# Giriş formu
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Veri tabanına gönderilecek bir nesne oluşturma
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')


@app.route("/record")
def record():
    try:
        text = speech_tr()
    except speech_recognition.exceptions.UnknownValueError: 
        text = "Ses algılanamadı."   
    except speech_recognition.exceptions.RequestError:
        text = "Bağlantı hatası."    
    except: 
        text = "Bir sorun oluştu."    
    return render_template("create_card.html", text=text)


@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        input_text = request.form['input_text']
        sentence_count = 1 #int(request.form.get('sentence_count', 1))  # Varsayılan 1
        summary = summarization(input_text, sentence_count)
        return render_template('summarize.html', summary=summary, input_text=input_text)
    

    return render_template('summarize.html')



if __name__ == "__main__":
    app.run(debug=True)
