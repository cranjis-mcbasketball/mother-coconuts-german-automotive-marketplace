from django.contrib import admin
from .models import *
# Register models (always do this after updating columns)

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(WishlistItem)
admin.site.register(Order)
