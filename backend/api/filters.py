import django_filters
from recipes.models import Ingredient, Recipe

class IngredientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='istartswith'
    )

    class Meta:
        model = Ingredient
        fields = ['name']

class RecipeFilter(django_filters.FilterSet):
    is_favorited = django_filters.BooleanFilter(method='filter_by_favorite')
    is_in_shopping_cart = django_filters.BooleanFilter(method='filter_by_shopping_cart')

    class Meta:
        model = Recipe
        fields = ['author']

    def _get_user_or_none(self) -> models.QuerySet:
        return self.request.user if self.request.user.is_authenticated else None

    def filter_by_favorite(self, queryset: models.QuerySet, name: str, value: bool) -> models.QuerySet:
        if (user := self._get_user_or_none()) is None:
            return queryset
        return queryset.filter(favorited_by__user=user) if value else queryset.exclude(favorited_by__user=user)

    def filter_by_shopping_cart(self, queryset: models.QuerySet, name: str, value: bool) -> models.QuerySet:
        if (user := self._get_user_or_none()) is None:
            return queryset
        return queryset.filter(shopping_cart__user=user) if value else queryset.exclude(shopping_cart__user=user)
