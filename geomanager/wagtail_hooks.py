from adminboundarymanager.models import AdminBoundarySettings
from wagtail import hooks
from wagtail.api.v2.utils import get_full_url
from wagtail.admin.menu import SubmenuMenuItem
from wagtail.admin.urls import urlpatterns as wagtail_admin_urls

from .models import GeoStationSettings, AdditionalMapBoundaryData  # Ensure the correct model name is imported
from .utils.boundary import create_boundary_dataset
from . import urls as geomanager_urls


@hooks.register("register_admin_urls")
def urlconf_geomanager():
    """
    Register custom GeoManager URLs.
    """
    return geomanager_urls


@hooks.register("construct_main_menu")
def customize_main_menu(request, menu_items):
    """
    Add GeoManager menu items to the main menu.
    """
    menu_items.append(
        SubmenuMenuItem(
            "GeoManager",
            wagtail_admin_urls,
            name="geomanager",
            classnames="icon icon-folder-open-inverse",
        )
    )


@hooks.register("register_icons")
def register_icons(icons):
    """
    Register custom icons for the admin interface.
    """
    return icons + [
        "wagtailfontawesomesvg/solid/palette.svg",
        "wagtailfontawesomesvg/solid/database.svg",
        "wagtailfontawesomesvg/solid/layer-group.svg",
        "wagtailfontawesomesvg/solid/globe.svg",
        "wagtailfontawesomesvg/solid/map.svg",
    ]


@hooks.register("construct_settings_menu")
def hide_settings_menu_item(request, menu_items):
    """
    Hide specific settings menu items.
    """
    hidden_settings = ["admin-boundary-settings", "geomanager-settings"]
    menu_items[:] = [item for item in menu_items if item.name not in hidden_settings]


@hooks.register("register_geomanager_datasets")
def register_geomanager_datasets(request):
    """
    Register GeoManager datasets for boundary and additional data.
    """
    datasets = []

    # Retrieve admin boundary settings
    abm_settings = AdminBoundarySettings.for_request(request)
    if abm_settings and abm_settings.boundary_tiles_url:
        boundary_tiles_url = get_full_url(request, abm_settings.boundary_tiles_url)

        # Create boundary dataset
        boundary_dataset = create_boundary_dataset(boundary_tiles_url)
        datasets.append(boundary_dataset)

    # Retrieve additional boundary datasets
    extra_boundary_datasets = AdditionalMapBoundaryData.objects.filter(active=True)

    for extra_boundary in extra_boundary_datasets:
        dataset_config = extra_boundary.get_dataset_config(request)
        datasets.append(dataset_config)

    return datasets
