```python
from PricingSchema import PricingSchema

def set_pay_per_view(content_id, price):
    # Fetch the content from the database using the content_id
    content = ContentSchema.objects.get(id=content_id)

    # Create a new pricing schema for the content
    pricing = PricingSchema(content=content, price=price, type='pay-per-view')

    # Save the pricing schema to the database
    pricing.save()

    return 'pricing_set_successful'
```