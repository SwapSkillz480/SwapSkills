from django.contrib import admin
from .models import SwapRequest, Feedback

@admin.register(SwapRequest)
class SwapRequestAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'status', 'skill_requested_by_sender', 'skill_offered_by_sender')
    list_filter = ('status', 'from_user', 'to_user')
    search_fields = ('skill_requested_by_sender', 'skill_offered_by_sender',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('swap_request', 'rating')
    list_filter = ('rating',)
    search_fields = ('swap_request__skill',)
