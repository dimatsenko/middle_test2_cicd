from django.test import TestCase
from django.urls import reverse
from recipe.models import Category, Recipe


class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipes = []
        for i in range(15):
            recipe = Recipe.objects.create(
                title=f"Recipe {i}",
                description=f"Description {i}",
                instructions=f"Instructions {i}",
                ingredients=f"Ingredients {i}",
                category=self.category
            )
            self.recipes.append(recipe)

    def test_main_view(self):
        url = reverse('recipe:main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        
        context_recipes = response.context['recipes']
        self.assertTrue(len(context_recipes) <= 10)
        
        for r in context_recipes:
            self.assertContains(response, r.title)
