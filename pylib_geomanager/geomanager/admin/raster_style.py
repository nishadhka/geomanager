from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from wagtail.admin.views.generic import CreateView, EditView, IndexView
from wagtail.admin.panels import FieldPanel

from geomanager.models import RasterFileLayer, RasterStyle


class RasterStyleCreateView(CreateView):
    """Customized create view for RasterStyle."""
    model = RasterStyle
    template_name = "geomanager/raster_style_create.html"

    def get_form(self):
        form = super().get_form()
        layer_id = self.request.GET.get("layer_id")
        if layer_id:
            try:
                layer = RasterFileLayer.objects.get(pk=layer_id)
                form.fields["layer_id"] = forms.CharField(
                    required=False, widget=forms.HiddenInput()
                )
                form.initial.update({"layer_id": layer.pk})
            except RasterFileLayer.DoesNotExist:
                pass
        return form

    def form_valid(self, form):
        response = super().form_valid(form)
        layer_id = form.cleaned_data.get("layer_id")
        if layer_id:
            try:
                layer = RasterFileLayer.objects.get(pk=layer_id)
                layer.style = self.instance
                layer.save()
            except RasterFileLayer.DoesNotExist:
                pass
        return response


class RasterStyleEditView(EditView):
    """Edit view for RasterStyle."""
    model = RasterStyle
    template_name = "geomanager/raster_style_edit.html"


class RasterStyleIndexView(IndexView):
    """Index view for RasterStyle."""
    model = RasterStyle
    template_name = "geomanager/raster_style_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "extra_js": [
                "geomanager/js/vendor/d3.min.js",
                "geomanager/js/raster_style_index_extra.js",
            ],
        })
        return context


class RasterStyleAdmin:
    """Admin class for RasterStyle."""
    model = RasterStyle
    menu_label = _("Raster Styles")
    menu_icon = "palette"
    create_view_class = RasterStyleCreateView
    edit_view_class = RasterStyleEditView
    index_view_class = RasterStyleIndexView
    list_display = ("name", "min", "max", "preview")
    panels = [
        FieldPanel("name"),
        FieldPanel("min"),
        FieldPanel("max"),
    ]

    def preview(self, obj):
        legend_config = obj.get_legend_config()
        context = {
            "legend_config": legend_config,
            "colors_str": ",".join([item.get("color") for item in legend_config.get("items")]),
        }
        html = render_to_string("geomanager/modeladmin/raster_style_legend_preview.html", context)
        return mark_safe(html)
