from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from wagtail.admin.views import generic
from wagtail.admin.menu import MenuItem
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from geomanager.models import Category


class CategoryCreateView(generic.CreateView):
    """
    Custom create view for categories.
    """
    model = Category
    template_name = "geomanager/category_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_index_url = self.get_success_url()

        navigation_items = [
            {"url": category_index_url, "label": Category._meta.verbose_name_plural},
            {"url": "#", "label": _("New") + f" {Category._meta.verbose_name}"},
        ]

        context.update({"navigation_items": navigation_items})
        return context


class CategoryEditView(generic.EditView):
    """
    Custom edit view for categories.
    """
    model = Category
    template_name = "geomanager/category_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_index_url = self.get_success_url()

        navigation_items = [
            {"url": category_index_url, "label": Category._meta.verbose_name_plural},
            {"url": "#", "label": self.object.title},
        ]

        context.update({"navigation_items": navigation_items})
        return context


class CategoryModelAdmin(Page):
    """
    Custom admin interface for categories.
    """
    model = Category
    menu_label = _("Datasets")
    menu_icon = "layer-group"

    content_panels = Page.content_panels + [
        FieldPanel("title"),
        FieldPanel("icon"),
    ]

    def category_icon(self, obj):
        icon = obj.icon or "layer-group"

        icon_html = f"""
           <span class="icon-wrapper">
                <svg class="icon icon-{icon} icon" aria-hidden="true" style="height:40px;width:40px">
                    <use href="#icon-{icon}"></use>
                </svg>
            </span>
        """
        return mark_safe(icon_html)

    def mapviewer_map_url(self, obj):
        label = _("MapViewer")
        button_html = f"""
                <a href="{obj.mapviewer_map_url}" target="_blank" rel="noopener noreferrer" class="button button-small button--icon button-secondary">
                    <span class="icon-wrapper">
                        <svg class="icon icon-map icon" aria-hidden="true">
                            <use href="#icon-map"></use>
                        </svg>
                    </span>
                    {label}
                </a>
            """
        return mark_safe(button_html)

    def create_dataset(self, obj):
        label = _("Add Dataset")
        button_html = f"""
            <a href="{obj.dataset_create_url()}" class="button button-small button--icon bicolor">
                <span class="icon-wrapper">
                    <svg class="icon icon-plus icon" aria-hidden="true">
                        <use href="#icon-plus"></use>
                    </svg>
                </span>
              {label}
            </a>
        """
        return mark_safe(button_html)

    def view_datasets(self, obj):
        label = _("View Datasets")

        datasets_count = obj.datasets.count()

        button_html = f"""
            <a href="{obj.datasets_list_url()}" class="button button-small button--icon bicolor button-secondary">
                <span class="icon-wrapper">
                    <svg class="icon icon-database icon" aria-hidden="true">
                        <use href="#icon-database"></use>
                    </svg>
                </span>
                {label} ({datasets_count})
            </a>
        """
        return mark_safe(button_html)
