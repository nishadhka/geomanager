from django.urls import path
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from wagtail.admin.views.generic import CreateView, EditView, IndexView
from wagtail.admin.menu import MenuItem

from geomanager.models import Dataset, RasterFileLayer, LayerRasterFile, Category
from geomanager.views import (
    upload_raster_file,
    publish_raster,
    delete_raster_upload,
    preview_raster_layers
)


class RasterFileLayerCreateView(CreateView):
    model = RasterFileLayer
    template_name = "geomanager/raster_file_layer_create.html"

    def get_form(self):
        form = super().get_form()
        form.fields["dataset"].queryset = Dataset.objects.filter(layer_type="raster_file")

        dataset_id = self.request.GET.get("dataset_id")
        if dataset_id:
            form.initial.update({"dataset": dataset_id})
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        navigation_items = [
            {"url": "/admin/categories/", "label": Category._meta.verbose_name_plural},
            {"url": "/admin/datasets/", "label": Dataset._meta.verbose_name_plural},
            {"url": "#", "label": _("New") + f" {RasterFileLayer._meta.verbose_name}"},
        ]
        context["navigation_items"] = navigation_items
        return context


class RasterFileLayerEditView(EditView):
    model = RasterFileLayer
    template_name = "geomanager/raster_file_layer_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        navigation_items = [
            {"url": "/admin/categories/", "label": Category._meta.verbose_name_plural},
            {"url": "/admin/datasets/", "label": Dataset._meta.verbose_name_plural},
            {"url": "/admin/raster-file-layers/", "label": RasterFileLayer._meta.verbose_name_plural},
            {"url": "#", "label": self.instance.title},
        ]
        context["navigation_items"] = navigation_items
        return context


class RasterFileLayerIndexView(IndexView):
    model = RasterFileLayer
    template_name = "geomanager/raster_file_layer_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        navigation_items = [
            {"url": "/admin/categories/", "label": _("Categories")},
            {"url": "/admin/datasets/", "label": _("Datasets")},
            {"url": "#", "label": RasterFileLayer._meta.verbose_name_plural},
        ]
        context["navigation_items"] = navigation_items
        return context


class RasterFileLayerAdmin:
    model = RasterFileLayer
    menu_label = _("Raster File Layers")
    menu_icon = "database"
    list_display = ["title", "dataset_link", "uploaded_files", "mapviewer_map_url"]
    list_filter = ["dataset__category"]

    def dataset_link(self, obj):
        return mark_safe(f'<a href="{obj.dataset.get_admin_url()}">{obj.dataset.title}</a>')

    def uploaded_files(self, obj):
        return obj.raster_files.count()

    def mapviewer_map_url(self, obj):
        return mark_safe(f'<a href="{obj.mapviewer_map_url}" target="_blank">Map Viewer</a>')


# URL Definitions
urls = [
    path('upload-rasters/', upload_raster_file, name='geomanager_upload_rasters'),
    path('upload-rasters/<uuid:dataset_id>/', upload_raster_file, name='geomanager_dataset_upload_raster'),
    path('publish-rasters/<int:upload_id>/', publish_raster, name='geomanager_publish_raster'),
    path('delete-raster-upload/<int:upload_id>/', delete_raster_upload, name='geomanager_delete_raster_upload'),
    path('preview-raster-layers/<uuid:dataset_id>/', preview_raster_layers, name='geomanager_preview_raster_dataset'),
]

# Ensure this is registered in Wagtail hooks
# Example:
# @hooks.register("register_admin_urls")
# def register_admin_urls():
#     return urls
