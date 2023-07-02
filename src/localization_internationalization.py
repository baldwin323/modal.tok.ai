```python
import json
from flask_babel import Babel, gettext

from src.user_schema import UserSchema
from src.content_schema import ContentSchema

babel = Babel()

supported_languages = ['en', 'es', 'fr', 'de', 'zh']

@babel.localeselector
def get_locale():
    user_id = session.get('user_id')
    if user_id is not None:
        user = UserSchema.query.get(user_id)
        return user.language
    return request.accept_languages.best_match(supported_languages)

def setLocalization(user_id, language):
    user = UserSchema.query.get(user_id)
    if language in supported_languages:
        user.language = language
        db.session.commit()
        return gettext('Language updated successfully')
    else:
        return gettext('Unsupported language')

def localizeContent(content_id, translations):
    content = ContentSchema.query.get(content_id)
    for lang, translation in translations.items():
        if lang in supported_languages:
            content.translations[lang] = translation
    db.session.commit()

def getLocalizedContent(content_id, language):
    content = ContentSchema.query.get(content_id)
    if language in content.translations:
        return content.translations[language]
    else:
        return content.translations['en']

def integrateRegionalPayment(user_id, payment_option):
    user = UserSchema.query.get(user_id)
    user.payment_option = payment_option
    db.session.commit()
```
