from flask import Flask, request, render_template, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# メール設定
app.config["MAIL_SERVER"] = "smtp.example.com"  # SMTPサーバのアドレスを入力します。
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "shintaro060776@gmail.com"  # あなたのメールアドレス
app.config["MAIL_PASSWORD"] = "Shin20090317"  # あなたのメールのパスワード

mail = Mail(app)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message_body = request.form['message']
        
        msg = Message("問い合わせ: " + name, sender=email, recipients=['shintaro060776@gmail.com'])
        msg.body = f"""
        From: {name} <{email}>
        
        {message_body}
        """
        
        mail.send(msg)
        flash("メッセージが送信されました！")
        return redirect("/")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)