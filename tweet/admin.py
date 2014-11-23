from django.contrib import admin

from .models import Tweet, Configuracao


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = ('texto', 'agendado_para', 'publicado')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "configuracao" and not request.user.is_superuser:
            kwargs["queryset"] = Configuracao.objects.filter(dono=request.user)

        return super(TweetAdmin, self).\
            formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display = ('app_key', 'app_secret')
    exclude = ('dono',)

    def queryset(self, request):
        if request.user.is_superuser:
            return Configuracao.objects.all()

        return Configuracao.objects.filter(dono=request.user)

    def save_model(self, request, obj, form, change):
        obj.dono = request.user
        obj.save()
