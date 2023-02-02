from django.contrib import admin

from main.models import(
    Pen,
    Stock
)

class PenAdmin(admin.ModelAdmin):
    model = Pen
    list_display = [
        'model_title',
        'manufacturer',
        'color'
    ]
    readonly_fields = (
        'model_title',
        'manufacturer',
    )
    
class StockAdmin(admin.ModelAdmin):
    model = Stock
    

admin.site.register(Pen, PenAdmin)
admin.site.register(Stock, StockAdmin)
