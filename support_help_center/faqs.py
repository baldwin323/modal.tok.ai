```python
class FAQ:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

faqs = []

def updateFaqs(new_faq):
    faqs.append(new_faq)

def getFaqs():
    return faqs

def findFaq(question):
    for faq in faqs:
        if faq.question == question:
            return faq
    return None

def deleteFaq(question):
    faq = findFaq(question)
    if faq:
        faqs.remove(faq)

def editFaq(question, new_answer):
    faq = findFaq(question)
    if faq:
        faq.answer = new_answer
```