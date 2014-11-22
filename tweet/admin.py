from django.contrib import admin


class TweetAdmin(admin.ModelAdmin):

	list_display=('texto', 'agendado_para')
