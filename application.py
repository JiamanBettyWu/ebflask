from flask import Flask, url_for, request, redirect, render_template
import boto3

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/')
def hello():
    return "hello!!!"
#@application.route('/index/')
#def index(text, tl):
#    print('Hello! \n The text is {} \n the target is {}'.format(text, tl))
#    return "Hello! changes"
@application.route("/translate", methods = ["POST", "GET"])
def translate():
    return render_template('translate.html')

@application.route('/translate_text', methods = ["POST", "GET"])
def translate_info():
    if request.method == "POST":
        text = request.form["tx"]
        sl = request.form["sl"]
        tl = request.form["tl"]

        translate = boto3.client(service_name='translate', region_name='us-east-1')

        result = translate.translate_text(Text=text, SourceLanguageCode=sl, TargetLanguageCode=tl)
        print('TranslatedText: ' + result.get('TranslatedText'))
        print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
        print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
        # return 'Hello! \n The text is {} \n the target is {}'.format(text, tl)
        return result.get('TranslatedText')


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()