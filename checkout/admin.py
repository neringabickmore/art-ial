from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Order item information administration
    """

    model = OrderLineItem
    readonly_fields = ('line_item_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Placed orders administration
    """

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'purchase_date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'purchase_date', 'full_name',
              'email', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'county', 'country',
              'postcode', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid')

    list_display = ('order_number', 'purchase_date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-purchase_date',)

admin.site.register(Order, OrderAdmin)
