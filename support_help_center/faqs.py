```python
class FAQ:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

faqs = []

def updateFAQ(question, answer):
    faq = FAQ(question, answer)
    faqs.append(faq)

def getFAQs():
    return faqs

def findFAQ(question):
    for faq in faqs:
        if faq.question == question:
            return faq.answer
    return "No answer found for your question."

def deleteFAQ(question):
    for faq in faqs:
        if faq.question == question:
            faqs.remove(faq)
            return "FAQ removed successfully."
    return "No such FAQ found."
```