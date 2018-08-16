from django.apps import AppConfig


class NutritionPlanValuesConfig(AppConfig):
    name = 'wger.nutrition'
    verbose_name = "NutritionPlan"

    def ready(self):
        import wger.nutrition.signals  # noqa F401
