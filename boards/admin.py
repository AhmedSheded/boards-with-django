from django.contrib import admin
from .models import Board, Topic
from django.contrib.auth.models import Group
# Register your models here.

# admin.site.unregister(Group)
admin.site.site_header = 'Sheded Admin Panel'
admin.site.site_title = 'Boards Admin Panel'


class InlineTopic(admin.StackedInline):
    model = Topic
    extra = 1


class BoardAdmin(admin.ModelAdmin):
    inlines = [InlineTopic]


class TopicAdmin(admin.ModelAdmin):
    fields = ('subject', 'board', 'created_by', 'views')
    list_display = ('subject', 'board', 'created_dt', 'created_by','combine_subject_board')

    def combine_subject_board(self, obj):
        return "{} - {}".format(obj.subject, obj.board)

    list_display_links = ['board', 'created_by']
    list_editable = ['subject']
    list_filter = ['created_by', 'board', 'created_dt']
    search_fields = ('board', 'created_by')


admin.site.register(Board, BoardAdmin)
admin.site.register(Topic, TopicAdmin)

