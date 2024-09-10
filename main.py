from pathlib import Path

import flet_easy as fs
from core.config import ConfigApp
import flet as ft

app = fs.FletEasy(route_init="/home", path_views=Path(__file__).parent / "views")

# We load the application configuration.
ConfigApp(app)

# We run the application
ft.app(
    target=app.run(fastapi=True),
    view=ft.AppView.WEB_BROWSER,
    use_color_emoji=True,
    route_url_strategy="hash",
)
