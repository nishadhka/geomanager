from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from wagtail.admin.views import generic
from wagtail.admin.menu import MenuItem
from wagtail.models import Page

from geomanager.models import Category, Dataset, SubCategory


class DatasetIndexView(generic.IndexView):
    """
    Custom index view for datasets.
    """
    model = Dataset
    template_name = "geomanager/dataset_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_index_url = "/admin/categories/"  # Replace with your admin category URL

        navigation_items = [
            {"url": category_index_url, "label": Category._meta.verbose_name_plural},
            {"url": "#", "label": Dataset._meta.verbose_name_plural},
        ]

        context.update({
            "custom_create_url": {
                "label": _("Create from categories"),
                "url": category_index_url
            },
            "navigation_items": navigation_items,
        })

        return context


class DatasetCreateView(generic.CreateView):
    """
    Custom create view for datasets.
    """
    model = Dataset
    template_name = "geomanager/dataset_create.html"

    def get_form(self):
        form = super().get_form()
        category_id = self.request.GET.get("category_id")
        if category_id:
            form.fields["sub_category"].queryset = SubCategory.objects.filter(category=category_id)
            form.initial.update({"category": category_id})
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_index_url = "/admin/categories/"  # Replace with your admin category URL

        navigation_items = [
            {"url": category_index_url, "label": Category._meta.verbose_name_plural},
            {"url": "#", "label": _("New") + f" {Dataset._meta.verbose_name}"},
        ]

        context.update({
            "navigation_items": navigation_items,
        })

        return context


class DatasetEditView(generic.EditView):
    """
    Custom edit view for datasets.
    """
    model = Dataset
    template_name = "geomanager/dataset_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_index_url = "/admin/categories/"  # Replace with your admin category URL
        datasets_index_url = "/admin/datasets/"  # Replace with your admin dataset URL

        navigation_items = [
            {"url": category_index_url, "label": Category._meta.verbose_name_plural},
            {"url": datasets_index_url, "label": Dataset._meta.verbose_name_plural},
            {"url": "#", "label": self.object.title},
        ]

        context.update({
            "navigation_items": navigation_items,
        })

        return context


class DatasetAdmin(Page):
    """
    Admin configuration for Datasets.
    """
    model = Dataset
    menu_label = _("Datasets")
    menu_icon = "database"
    content_panels = Page.content_panels + [
        # Add panels for your dataset fields here
    ]

    def mapviewer_map_url(self, obj):
        label = _("MapViewer")

        if not obj.has_layers():
            return None

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

    def view_layers(self, obj):
        label = _("View Layers")

        if not obj.has_layers():
            return self.add_layer(obj)

        button_html = f"""
            <a href="{obj.layers_list_url()}" class="button button-small button--icon bicolor button-secondary">
                <span class="icon-wrapper">
                    <svg class="icon icon-layer-group icon" aria-hidden="true">
                        <use href="#icon-layer-group"></use>
                    </svg>
                </span>
                {label}
            </a>
        """
        return mark_safe(button_html)

    def add_layer(self, obj):
        label = _("Add Layer")
        button_html = f"""
            <a href="{obj.create_layer_url()}" class="button button-small bicolor button--icon ">
                <span class="icon-wrapper">
                    <svg class="icon icon-plus icon" aria-hidden="true">
                        <use href="#icon-plus"></use>
                    </svg>
                </span>
                {label}
            </a>
        """
        return mark_safe(button_html)
