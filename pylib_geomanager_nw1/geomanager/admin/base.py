from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from wagtail.admin.views import generic
from wagtail.admin.menu import MenuItem
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from django.urls import reverse

from geomanager.models import Dataset, Category


class BaseModelAdmin(Page):
    """
    Base class for managing models in Wagtail admin.
    """
    template_name = "geomanager/modeladmin/index.html"
    create_template_name = "geomanager/modeladmin/create.html"
    edit_template_name = "geomanager/modeladmin/edit.html"

    content_panels = Page.content_panels + [
        FieldPanel("title"),
    ]


class LayerIndexView(generic.IndexView):
    """
    Custom view for the layer index page.
    """
    model = Dataset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        model_verbose_name = self.model._meta.verbose_name_plural

        datasets_url = reverse("wagtailadmin_explore_root")
        categories_url = reverse("wagtailadmin_explore_root")

        navigation_items = [
            {"url": categories_url, "label": _("Categories")},
            {"url": datasets_url, "label": _("Datasets")},
            {"url": "#", "label": model_verbose_name},
        ]

        context_data.update({
            "custom_create_url": {
                "label": _("Create from datasets"),
                "url": datasets_url
            },
            "navigation_items": navigation_items,
        })

        return context_data


class LayerFileDeleteView(generic.DeleteView):
    """
    Custom view for deleting layer files.
    """
    @cached_property
    def index_url(self):
        index_url = self.get_success_url()
        if self.object:
            layer_id = str(self.object.layer.pk)
            index_url += f"?layer__id={layer_id}"
        return index_url


# Adding items to the Wagtail admin menu
class GeomanagerMenuItem(MenuItem):
    def __init__(self, *args, **kwargs):
        super().__init__("Geomanager", reverse("wagtailadmin_explore_root"), *args, **kwargs)


# Register the menu item (optional)
def register_admin_menu_items():
    from wagtail.admin.menu import admin_menu
    admin_menu.add_item(GeomanagerMenuItem())
