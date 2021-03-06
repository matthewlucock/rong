import tkinter
from rong import custom_widgets, colors, fonts, game_variables, game_modes, \
    event_names, utilities
from rong.screen_manager import screen_manager


versus_ai_screen = tkinter.Frame()

_title = tkinter.Label(
    master=versus_ai_screen,
    text="Versus AI",
    font=fonts.side_screen_title_font
)
_title.pack(pady=(30, 0))

_settings_container = tkinter.Frame(
    master=versus_ai_screen,
    **custom_widgets.miscellaneous_widget_parameters.SETTINGS_CONTAINER
)
_settings_container.pack(expand=True)

_difficulty_selector = custom_widgets.IntegerSelector(
    master=_settings_container,
    variable=game_variables.versus_ai_difficulty,
    minimum_value=1,
    maximum_value=10,
    text="Difficulty"
)
_difficulty_selector.pack(pady=(0, 20))

_power_ups_checkbox = custom_widgets.StyledCheckbox(
    master=_settings_container,
    variable=game_variables.power_ups_enabled,
    text="Power-ups"
)

_free_movement_checkbox = custom_widgets.StyledCheckbox(
    master=_settings_container,
    variable=game_variables.free_movement_enabled,
    text="Free movement"
)

_checkboxes = [_power_ups_checkbox, _free_movement_checkbox]

utilities.pack_widgets_as_vertical_list(
    widgets=_checkboxes,
    anchor=tkinter.W,
    margin=10
)

_buttons_container = tkinter.Frame(master=versus_ai_screen)
_buttons_container.pack(pady=(0, 50))

_play_button = custom_widgets.PlayButton(
    master=_buttons_container,
    game_mode=game_modes.VERSUS_AI
)
_play_button.pack(side=tkinter.LEFT, padx=(0, 20))

_back_button = custom_widgets.BackButton(master=_buttons_container)
_back_button.pack()

_widgets_to_set_background_of = [
    versus_ai_screen,
    _title,
    _buttons_container
]


_widgets_to_have_screen_background = [
    versus_ai_screen,
    _title,
    _buttons_container
]

_widgets_to_have_settings_container_background = [
    _settings_container
]

def _screen_background_color_trace_callback(*args):
    for _widget in _widgets_to_have_screen_background:
        _widget.config(
            background=colors.screen_background.get()
        )


def _settings_container_background_color_trace_callback(*args):
    background = colors.settings_container_background.get()

    for _widget in _widgets_to_have_settings_container_background:
        _widget.config(background=background)

    for _checkbox in _checkboxes:
        _checkbox.set_background(background)

    _difficulty_selector.set_background(background)

def _title_color_trace_callback(*args):
    _title.config(foreground=colors.title.get())


_screen_background_color_trace_callback()
_title_color_trace_callback()
_settings_container_background_color_trace_callback()
colors.screen_background.trace("w", _screen_background_color_trace_callback)
colors.title.trace("w", _title_color_trace_callback)
colors.settings_container_background.trace(
    "w",
    _settings_container_background_color_trace_callback
)
