from django.contrib import admin
from .models import Order, OrderLineItem, SubscriptionOrderLineItem


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class SubscriptionAdminInline(admin.TabularInline):
    model = SubscriptionOrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, SubscriptionAdminInline)

admin.site.register(Order, OrderAdmin)
