from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, FavoriteRecipes, ShoppingCart

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('measurement_unit',)
    ordering = ('name',)

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    min_num = 1
    autocomplete_fields = ('ingredient',)
    verbose_name = 'Ингредиент'
    verbose_name_plural = 'Ингредиенты'

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'cooking_time',
        'count_favorites',
        'created_at'
    )
    list_filter = ('author', 'tags', 'created_at')
    search_fields = ('name', 'author__username', 'author__email')
    readonly_fields = ('count_favorites',)
    filter_horizontal = ('tags',)
    inlines = (RecipeIngredientInline,)
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'author', 'image', 'tags')
        }),
        ('Описание', {
            'fields': ('text',)
        }),
        ('Время приготовления', {
            'fields': ('cooking_time',)
        }),
    )

    def count_favorites(self, obj):
        return obj.favorited_by.count()
    count_favorites.short_description = 'В избранном'

@admin.register(FavoriteRecipes)
class FavoriteRecipesAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('user__username', 'recipe__name')
    date_hierarchy = 'added_at'

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('user__username', 'recipe__name')
    date_hierarchy = 'added_at'
