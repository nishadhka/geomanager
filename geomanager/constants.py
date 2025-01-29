MAPBOX_GL_STYLE_SPEC = {
    "PAINT_DEFAULTS": {
        "fill_color": "#000000",
        "fill_opacity": 1,
        "fill_outline_color": "#000000",
        "fill_antialias": True,

        "line_color": "#000000",
        "line_dasharray": "",
        "line_gap_width": 0,
        "line_opacity": 1,
        "line_width": 1,
        "line_offset": 0,

        "icon_color": "#000000",
        "icon_halo_blur": 0,
        "icon_halo_color": "#000000",
        "icon_halo_width": 0,
        "icon_opacity": 1,

        "text_color": "#000000",
        "text_halo_color": 0,
        "text_halo_width": 0,
        "text_translate": "",
        "text_translate_anchor": "map",

        "circle_color": "#000000",
        "circle_opacity": 1,
        "circle_radius": 5,
        "circle_stroke_color": "#000000",
        "circle_stroke_width": 0,
    },
    "LAYOUT_DEFAULTS": {
        "line_cap": "butt",
        "line_join": "miter",
        "line_miter_limit": 2,
        "line_round_limit": 1.05,

        "icon_allow_overlap": False,
        "icon_anchor": "center",
        "icon_ignore_placement": False,
        "icon_keep_upright": False,
        "icon_offset": "",
        "icon_optional": False,
        "icon_padding": 2,
        "icon_pitch_alignment": "auto",
        "icon_rotate": 0,
        "icon_rotation_alignment": "auto",
        "icon_size": 1,
        "icon_text_fit": "none",

        "symbol_placement": "point",
        "text_allow_overlap": False,
        "text_anchor": "center",
        "text_size": 16,
        "text_transform": "none",
        "text_ignore_placement": False,
        "text_justify": "center",
        "text_keep_upright": False,
        "text_letter_spacing": 0,
        "text_line_height": 1.2,
        "text_max_angle": 45,
        "text_max_width": 10,
        "text_offset": "",
        "text_opacity": 1,
        "text_padding": 2,
        "text_pitch_alignment": "auto",
        "text_radial_offset": 0,
        "text_rotate": 0,
        "text_rotation_alignment": "auto",
        "text_variable_anchor": "",
    }
}

DEFAULT_OPEN_MAP_TILES_STYLE = {
    "version": 8,
    "name": "Base",
    "metadata": {
        "openmaptiles:version": "3.x",
        "mapbox:groups": {
            "basemap_light": {
                "name": "basemap-light"
            },
            "basemap_dark": {
                "name": "basemap-dark"
            },
            "basemap_satellite": {
                "name": "basemap-satellite"
            },
            "labels_light": {
                "name": "labels-light"
            },
            "labels_dark": {
                "name": "labels-dark"
            },
            "roads": {
                "name": "roads"
            }
        }
    },
    "sources": {
        "openmaptiles": {
            "type": "vector",
            "url": ""
        }
    },
    "layers": [
        {
            "id": "background-light",
            "paint": {
                "background-color": "hsl(0, 0%, 100%)"
            },
            "layout": {
                "visibility": "none"
            },
            "type": "background",
            "metadata": {
                "mapbox:group": "basemap_light"
            }
        },
        {
            "id": "background-dark",
            "type": "background",
            "metadata": {
                "mapbox:group": "basemap_dark"
            },
            "layout": {
                "visibility": "none"
            },
            "paint": {
                "background-color": "hsl(60, 2%, 19%)"
            }
        },
        {
            "id": "background-satellite",
            "type": "background",
            "metadata": {
                "mapbox:group": "basemap_satellite"
            },
            "layout": {
                "visibility": "none"
            },
            "paint": {
                "background-color": "#fff"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Polygon"
                ],
                [
                    "!=",
                    "intermittent",
                    1
                ]
            ],
            "id": "water",
            "paint": {
                "fill-color": "hsl(203, 95%, 84%)"
            },
            "layout": {
                "visibility": "none"
            },
            "source": "openmaptiles",
            "source-layer": "water",
            "type": "fill",
            "metadata": {
                "mapbox:group": "basemap_light"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Polygon"
                ],
                [
                    "!=",
                    "intermittent",
                    1
                ]
            ],
            "id": "water_dark",
            "paint": {
                "fill-color": "hsl(60, 5%, 12%)"
            },
            "layout": {
                "visibility": "none"
            },
            "source": "openmaptiles",
            "source-layer": "water",
            "type": "fill",
            "metadata": {
                "mapbox:group": "basemap_dark"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Polygon"
                ],
                [
                    "==",
                    "intermittent",
                    1
                ]
            ],
            "id": "water_intermittent",
            "paint": {
                "fill-color": "hsl(203, 95%, 84%)",
                "fill-opacity": 0.7
            },
            "layout": {
                "visibility": "none"
            },
            "source": "openmaptiles",
            "source-layer": "water",
            "type": "fill",
            "metadata": {
                "mapbox:group": "basemap_light"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Polygon"
                ],
                [
                    "==",
                    "intermittent",
                    1
                ]
            ],
            "id": "water_intermittent_dark",
            "paint": {
                "fill-color": "hsl(60, 5%, 12%)",
                "fill-opacity": 0.7
            },
            "layout": {
                "visibility": "none"
            },
            "source": "openmaptiles",
            "source-layer": "water",
            "type": "fill",
            "metadata": {
                "mapbox:group": "basemap_dark"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "LineString"
                ],
                [
                    "!in",
                    "brunnel",
                    "tunnel",
                    "bridge"
                ],
                [
                    "!=",
                    "intermittent",
                    1
                ]
            ],
            "id": "waterway",
            "paint": {
                "line-color": "hsl(203, 95%, 84%)",
                "line-opacity": 1,
                "line-width": {
                    "base": 1.4,
                    "stops": [
                        [
                            8,
                            1
                        ],
                        [
                            20,
                            8
                        ]
                    ]
                }
            },
            "layout": {
                "visibility": "none"
            },
            "source": "openmaptiles",
            "source-layer": "waterway",
            "minzoom": 8,
            "type": "line",
            "metadata": {
                "mapbox:group": "basemap_light"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "LineString"
                ],
                [
                    "!in",
                    "brunnel",
                    "tunnel",
                    "bridge"
                ],
                [
                    "!=",
                    "intermittent",
                    1
                ]
            ],
            "id": "waterway_dark",
            "paint": {
                "line-color": "hsl(0, 0%, 0%)",
                "line-opacity": 1,
                "line-width": {
                    "base": 1.4,
                    "stops": [
                        [
                            8,
                            1
                        ],
                        [
                            20,
                            8
                        ]
                    ]
                }
            },
            "layout": {
                "visibility": "none"
            },
            "source": "openmaptiles",
            "source-layer": "waterway",
            "minzoom": 8,
            "type": "line",
            "metadata": {
                "mapbox:group": "basemap_dark"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "LineString"
                ],
                [
                    "!in",
                    "brunnel",
                    "tunnel",
                    "bridge"
                ],
                [
                    "==",
                    "intermittent",
                    1
                ]
            ],
            "id": "waterway_intermittent",
            "paint": {
                "line-color": "hsl(203, 95%, 84%)",
                "line-opacity": 1,
                "line-width": {
                    "base": 1.4,
                    "stops": [
                        [
                            8,
                            1
                        ],
                        [
                            20,
                            8
                        ]
                    ]
                },
                "line-dasharray": [
                    2,
                    1
                ]
            },
            "layout": {
                "visibility": "none"
            },
            "source": "openmaptiles",
            "source-layer": "waterway",
            "minzoom": 8,
            "type": "line",
            "metadata": {
                "mapbox:group": "basemap_light"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "LineString"
                ],
                [
                    "!in",
                    "brunnel",
                    "tunnel",
                    "bridge"
                ],
                [
                    "==",
                    "intermittent",
                    1
                ]
            ],
            "id": "waterway_intermittent_dark",
            "paint": {
                "line-color": "hsl(0, 0%, 0%)",
                "line-opacity": 1,
                "line-width": {
                    "base": 1.4,
                    "stops": [
                        [
                            8,
                            1
                        ],
                        [
                            20,
                            8
                        ]
                    ]
                },
                "line-dasharray": [
                    2,
                    1
                ]
            },
            "layout": {
                "visibility": "none"
            },
            "source": "openmaptiles",
            "source-layer": "waterway",
            "minzoom": 8,
            "type": "line",
            "metadata": {
                "mapbox:group": "basemap_dark"
            }
        },
        {
            "id": "road_pier",
            "type": "line",
            "metadata": {
                "mapbox:group": "roads"
            },
            "source": "openmaptiles",
            "source-layer": "transportation",
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "LineString"
                ],
                [
                    "in",
                    "class",
                    "pier"
                ]
            ],
            "layout": {
                "line-cap": "round",
                "line-join": "round",
                "visibility": "none"
            },
            "paint": {
                "line-color": "#fffca2",
                "line-width": {
                    "base": 1.2,
                    "stops": [
                        [
                            15,
                            1
                        ],
                        [
                            17,
                            4
                        ]
                    ]
                }
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "LineString"
                ],
                [
                    "in",
                    "class",
                    "path",
                    "track"
                ]
            ],
            "id": "road_path",
            "paint": {
                "line-color": "#fffca2",
                "line-dasharray": [
                    1,
                    1
                ],
                "line-width": {
                    "base": 1.55,
                    "stops": [
                        [
                            4,
                            0.25
                        ],
                        [
                            20,
                            10
                        ]
                    ]
                }
            },
            "layout": {
                "line-cap": "square",
                "line-join": "bevel",
                "visibility": "none"
            },
            "source": "openmaptiles",
            "source-layer": "transportation",
            "type": "line",
            "metadata": {
                "mapbox:group": "roads"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "LineString"
                ],
                [
                    "in",
                    "class",
                    "minor",
                    "service"
                ]
            ],
            "id": "road_minor",
            "paint": {
                "line-color": "#fffca2",
                "line-width": {
                    "base": 1.55,
                    "stops": [
                        [
                            4,
                            0.25
                        ],
                        [
                            20,
                            30
                        ]
                    ]
                }
            },
            "layout": {
                "line-cap": "round",
                "line-join": "round",
                "visibility": "none"
            },
            "source": "openmaptiles",
            "source-layer": "transportation",
            "type": "line",
            "minzoom": 13,
            "metadata": {
                "mapbox:group": "roads"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "LineString"
                ],
                [
                    "in",
                    "class",
                    "trunk",
                    "primary"
                ]
            ],
            "id": "road_trunk_primary",
            "paint": {
                "line-color": "#fffca2",
                "line-width": {
                    "base": 1.4,
                    "stops": [
                        [
                            6,
                            0.5
                        ],
                        [
                            20,
                            30
                        ]
                    ]
                }
            },
            "layout": {
                "line-cap": "round",
                "line-join": "round",
                "visibility": "none"
            },
            "source": "openmaptiles",
            "source-layer": "transportation",
            "type": "line",
            "metadata": {
                "mapbox:group": "roads"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "LineString"
                ],
                [
                    "in",
                    "class",
                    "secondary",
                    "tertiary"
                ]
            ],
            "id": "road_secondary_tertiary",
            "paint": {
                "line-color": "#fffca2",
                "line-width": {
                    "base": 1.4,
                    "stops": [
                        [
                            6,
                            0.5
                        ],
                        [
                            20,
                            20
                        ]
                    ]
                }
            },
            "layout": {
                "line-cap": "round",
                "line-join": "round",
                "visibility": "none"
            },
            "source": "openmaptiles",
            "source-layer": "transportation",
            "type": "line",
            "metadata": {
                "mapbox:group": "roads"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "LineString"
                ],
                [
                    "==",
                    "class",
                    "motorway"
                ]
            ],
            "id": "road_major_motorway",
            "layout": {
                "line-cap": "round",
                "line-join": "round",
                "visibility": "none"
            },
            "paint": {
                "line-color": "#fffca2",
                "line-offset": 0,
                "line-width": {
                    "base": 1.4,
                    "stops": [
                        [
                            8,
                            1
                        ],
                        [
                            16,
                            10
                        ]
                    ]
                }
            },
            "source": "openmaptiles",
            "source-layer": "transportation",
            "type": "line",
            "metadata": {
                "mapbox:group": "roads"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Point"
                ],
                [
                    "==",
                    "rank",
                    1
                ]
            ],
            "id": "poi_label",
            "layout": {
                "icon-size": 1,
                "text-anchor": "top",
                "text-field": "{name}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-max-width": 8,
                "text-offset": [
                    0,
                    0.5
                ],
                "text-size": 11,
                "visibility": "none"
            },
            "minzoom": 14,
            "paint": {
                "text-color": "#666",
                "text-halo-blur": 1,
                "text-halo-color": "rgba(255,255,255,0.75)",
                "text-halo-width": 1,
                "text-opacity": 0.7
            },
            "source": "openmaptiles",
            "source-layer": "poi",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_light"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Point"
                ],
                [
                    "==",
                    "rank",
                    1
                ]
            ],
            "id": "poi_label_dark",
            "layout": {
                "icon-size": 1,
                "text-anchor": "top",
                "text-field": "{name}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-max-width": 8,
                "text-offset": [
                    0,
                    0.5
                ],
                "text-size": 11,
                "visibility": "none"
            },
            "minzoom": 14,
            "paint": {
                "text-halo-width": 1.25,
                "text-halo-color": "hsla(0, 0%, 10%, 0.75)",
                "text-color": "hsl(0, 0%, 100%)",
                "text-opacity": 0.9
            },
            "source": "openmaptiles",
            "source-layer": "poi",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_dark"
            }
        },
        {
            "filter": [
                "all",
                [
                    "has",
                    "iata"
                ]
            ],
            "id": "airport-label",
            "layout": {
                "icon-size": 1,
                "text-anchor": "top",
                "text-field": "{name}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-max-width": 8,
                "text-offset": [
                    0,
                    0.5
                ],
                "text-size": 11,
                "visibility": "none"
            },
            "minzoom": 10,
            "paint": {
                "text-color": "#666",
                "text-halo-blur": 1,
                "text-halo-color": "rgba(255,255,255,0.75)",
                "text-halo-width": 1,
                "text-opacity": 0.7
            },
            "source": "openmaptiles",
            "source-layer": "aerodrome_label",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_light"
            }
        },
        {
            "filter": [
                "all",
                [
                    "has",
                    "iata"
                ]
            ],
            "id": "airport-label-dark",
            "layout": {
                "icon-size": 1,
                "text-anchor": "top",
                "text-field": "{name}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-max-width": 8,
                "text-offset": [
                    0,
                    0.5
                ],
                "text-size": 11,
                "visibility": "none"
            },
            "minzoom": 10,
            "paint": {
                "text-halo-width": 1.25,
                "text-halo-color": "hsla(0, 0%, 10%, 0.75)",
                "text-color": "hsl(0, 0%, 100%)",
                "text-opacity": 0.9
            },
            "source": "openmaptiles",
            "source-layer": "aerodrome_label",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_dark"
            }
        },
        {
            "filter": [
                "==",
                "$type",
                "LineString"
            ],
            "id": "road_major_label",
            "layout": {
                "symbol-placement": "line",
                "text-field": "{name}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-letter-spacing": 0.1,
                "text-rotation-alignment": "map",
                "text-size": {
                    "base": 1.4,
                    "stops": [
                        [
                            10,
                            8
                        ],
                        [
                            20,
                            14
                        ]
                    ]
                },
                "text-transform": "uppercase",
                "visibility": "none"
            },
            "paint": {
                "text-color": "#000",
                "text-halo-color": "hsl(0, 0%, 100%)",
                "text-halo-width": 2,
                "text-opacity": 0.7
            },
            "source": "openmaptiles",
            "source-layer": "transportation_name",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_light"
            }
        },
        {
            "filter": [
                "==",
                "$type",
                "LineString"
            ],
            "id": "road_major_label_dark",
            "layout": {
                "symbol-placement": "line",
                "text-field": "{name}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-letter-spacing": 0.1,
                "text-rotation-alignment": "map",
                "text-size": {
                    "base": 1.4,
                    "stops": [
                        [
                            10,
                            8
                        ],
                        [
                            20,
                            14
                        ]
                    ]
                },
                "text-transform": "uppercase",
                "visibility": "none"
            },
            "paint": {
                "text-halo-width": 1.25,
                "text-halo-color": "hsla(0, 0%, 10%, 0.75)",
                "text-color": "hsl(0, 0%, 100%)",
                "text-opacity": 0.9
            },
            "source": "openmaptiles",
            "source-layer": "transportation_name",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_dark"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Point"
                ],
                [
                    "!in",
                    "class",
                    "city",
                    "state",
                    "country",
                    "continent"
                ]
            ],
            "id": "place_label_other",
            "layout": {
                "text-anchor": "center",
                "text-field": "{name}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-max-width": 6,
                "text-size": {
                    "stops": [
                        [
                            6,
                            10
                        ],
                        [
                            12,
                            14
                        ]
                    ]
                },
                "visibility": "none"
            },
            "minzoom": 8,
            "paint": {
                "text-color": "hsl(0, 0%, 25%)",
                "text-halo-blur": 0,
                "text-halo-color": "hsl(0, 0%, 100%)",
                "text-halo-width": 2,
                "text-opacity": 0.7
            },
            "source": "openmaptiles",
            "source-layer": "place",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_light"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Point"
                ],
                [
                    "!in",
                    "class",
                    "city",
                    "state",
                    "country",
                    "continent"
                ]
            ],
            "id": "place_label_other_dark",
            "layout": {
                "text-anchor": "center",
                "text-field": "{name}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-max-width": 6,
                "text-size": {
                    "stops": [
                        [
                            6,
                            10
                        ],
                        [
                            12,
                            14
                        ]
                    ]
                },
                "visibility": "none"
            },
            "minzoom": 8,
            "paint": {
                "text-halo-width": 1.25,
                "text-halo-color": "hsla(0, 0%, 10%, 0.75)",
                "text-color": "hsl(0, 0%, 100%)",
                "text-opacity": 0.9
            },
            "source": "openmaptiles",
            "source-layer": "place",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_dark"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Point"
                ],
                [
                    "==",
                    "class",
                    "city"
                ]
            ],
            "id": "place_label_city",
            "layout": {
                "text-field": "{name_en}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-max-width": 10,
                "text-size": {
                    "stops": [
                        [
                            3,
                            12
                        ],
                        [
                            8,
                            16
                        ]
                    ]
                },
                "visibility": "none"
            },
            "maxzoom": 16,
            "paint": {
                "text-color": "hsl(0, 0%, 0%)",
                "text-halo-blur": 0,
                "text-halo-color": "hsla(0, 0%, 100%, 0.75)",
                "text-halo-width": 2,
                "text-opacity": 0.7
            },
            "source": "openmaptiles",
            "source-layer": "place",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_light"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Point"
                ],
                [
                    "==",
                    "class",
                    "city"
                ]
            ],
            "id": "place_label_city_dark",
            "layout": {
                "text-field": "{name_en}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-max-width": 10,
                "text-size": {
                    "stops": [
                        [
                            3,
                            12
                        ],
                        [
                            8,
                            16
                        ]
                    ]
                },
                "visibility": "none"
            },
            "maxzoom": 16,
            "paint": {
                "text-halo-width": 1.25,
                "text-halo-color": "hsla(0, 0%, 10%, 0.75)",
                "text-color": "hsl(0, 0%, 100%)",
                "text-opacity": 0.9
            },
            "source": "openmaptiles",
            "source-layer": "place",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_dark"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Point"
                ],
                [
                    "==",
                    "class",
                    "country"
                ],
                [
                    "!has",
                    "iso_a2"
                ]
            ],
            "id": "country_label-other",
            "layout": {
                "text-field": "{name_en}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-max-width": 10,
                "text-size": {
                    "stops": [
                        [
                            3,
                            12
                        ],
                        [
                            8,
                            22
                        ]
                    ]
                },
                "visibility": "none"
            },
            "maxzoom": 12,
            "paint": {
                "text-color": "hsl(0, 0%, 13%)",
                "text-halo-blur": 0,
                "text-halo-color": "rgba(255,255,255,0.75)",
                "text-halo-width": 2,
                "text-opacity": 0.7
            },
            "source": "openmaptiles",
            "source-layer": "place",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_light"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Point"
                ],
                [
                    "==",
                    "class",
                    "country"
                ],
                [
                    "!has",
                    "iso_a2"
                ]
            ],
            "id": "country_label-other_dark",
            "layout": {
                "text-field": "{name_en}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-max-width": 10,
                "text-size": {
                    "stops": [
                        [
                            3,
                            12
                        ],
                        [
                            8,
                            22
                        ]
                    ]
                },
                "visibility": "none"
            },
            "maxzoom": 12,
            "paint": {
                "text-halo-width": 1.25,
                "text-halo-color": "hsla(0, 0%, 10%, 0.75)",
                "text-color": "hsl(0, 0%, 100%)",
                "text-opacity": 0.9
            },
            "source": "openmaptiles",
            "source-layer": "place",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_dark"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Point"
                ],
                [
                    "==",
                    "class",
                    "country"
                ],
                [
                    "has",
                    "iso_a2"
                ]
            ],
            "id": "country_label",
            "layout": {
                "text-field": "{name_en}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-max-width": 10,
                "text-size": {
                    "base": 1,
                    "stops": [
                        [
                            1,
                            10
                        ],
                        [
                            6,
                            24
                        ]
                    ]
                },
                "visibility": "none"
            },
            "maxzoom": 12,
            "paint": {
                "text-halo-width": 1.25,
                "text-halo-color": {
                    "base": 1,
                    "stops": [
                        [
                            2,
                            "rgba(255,255,255,0.75)"
                        ],
                        [
                            3,
                            "#fff"
                        ]
                    ]
                },
                "text-color": "hsl(0, 0%, 0%)",
                "text-opacity": 0.7
            },
            "source": "openmaptiles",
            "source-layer": "place",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_light"
            }
        },
        {
            "filter": [
                "all",
                [
                    "==",
                    "$type",
                    "Point"
                ],
                [
                    "==",
                    "class",
                    "country"
                ],
                [
                    "has",
                    "iso_a2"
                ]
            ],
            "id": "country_label_dark",
            "layout": {
                "text-field": "{name_en}",
                "text-font": [
                    "Klokantech Noto Sans Regular"
                ],
                "text-max-width": 10,
                "text-size": {
                    "base": 1,
                    "stops": [
                        [
                            1,
                            10
                        ],
                        [
                            6,
                            24
                        ]
                    ]
                },
                "visibility": "none"
            },
            "maxzoom": 12,
            "paint": {
                "text-halo-width": 1.25,
                "text-halo-color": "hsla(0, 0%, 10%, 0.75)",
                "text-color": "hsl(0, 0%, 100%)",
                "text-opacity": 0.9
            },
            "source": "openmaptiles",
            "source-layer": "place",
            "type": "symbol",
            "metadata": {
                "mapbox:group": "labels_dark"
            }
        }
    ],
    "id": "base"
}
