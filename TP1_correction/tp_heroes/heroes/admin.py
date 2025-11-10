from django.contrib import admin
from .models import SuperHero, Pouvoir, HeroUser
from django.contrib.auth.admin import UserAdmin
# Admin simple pour Pouvoir
admin.site.register(Pouvoir)

# Admin personnalisé pour SuperHero
@admin.register(SuperHero)
class SuperHeroAdmin(admin.ModelAdmin):
    list_display = ('nom', 'alias', 'puissance', 'actif')
    list_filter = ('actif',)
    search_fields = ('nom', 'alias')

    # Action personnalisée
    actions = ['desactiver_heroes']

    def desactiver_heroes(self, request, queryset):
        queryset.update(actif=False)
        self.message_user(request, "Héros désactivés !")
    desactiver_heroes.short_description = "Désactiver les héros sélectionnés"

@admin.register(HeroUser)
class HeroUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Héros préféré', {'fields': ('favorite_hero',)}),
    )

    list_display = ('username', 'email', 'is_staff', 'favorite_hero')
