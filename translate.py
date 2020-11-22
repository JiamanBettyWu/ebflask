import boto3

translate = boto3.client(service_name='translate', region_name='us-east-1')

result = translate.translate_text(Text="thank you", 
            SourceLanguageCode="en", TargetLanguageCode="de")
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
print(result)