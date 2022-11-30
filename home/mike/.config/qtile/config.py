# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

mod = "mod4"
terminal = guess_terminal("kitty")

keys = [
    
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Reload the config"),
    Key([mod, "control"], "r", lazy.reload_layout(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Rofi
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show window"), desc="show apliations"),
    # Abrir navegador 
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch firefox"),
    # Abrir Discord y Spotify
    Key([mod], "d", lazy.spawn("discord &"), desc="Launch Discord"),
    Key([mod], "s", lazy.spawn("spotify &"), desc="Launch spotify"),
    # Capturas de pantalla 
    Key([mod], "x", lazy.spawn("scrot -q 100 /home/mike/screenshot/captura.jpg"), desc="Captura de pantalla"),
    Key([mod, "shift"], "x", lazy.spawn("scrot -s -q 100 /home/mike/screenshot/captura.jpg"), desc="Captura recortable"),
    # Buscador de archivos
    Key([mod], "a", lazy.spawn("thunar"), desc="Buscador de archivos"),
]        

groups = [Group(i) for i in ["  ", "  ", "  ", "  ", " 漣 ", "  ", "  ", "  ", "  "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layout_Max = {
    'border_focus': '#8da1a0',
    'border_normal': '#000000',
    'border_width': 0,
    'margin': 0
}

layout_MonadTall = {
    'border_focus': '#8da1a0',
    'border_normal': '#000000',
    'border_width': 2,
    'margin': 3
}

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(**layout_Max),
    # Try morefq layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_MonadTall),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                
                widget.GroupBox(
                    font='Hack Nerd Font',
                    fontsize=18,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=2,
                    active=["#3c5a67", "#d7dcd7"],
                    inactive=["#1a282e", "#9a9e9a"],
                    block_highlight_text_color=["#365864", "#e4fef7"],
                    highlight_method="line",
                    highlight_color=["#0a0a0a", "#00141b"],
                    disable_drag=True
                ),

                widget.Prompt(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#0000ff"),
                    },
                ),
                
                widget.Spacer(),
                
                widget.Sep(
                    linewidth=3,
                    foreground=["#032633", "#c2e5e1"],
                    padding=5,
                    background=None
                ),
                
                widget.Systray(
                    padding=5,
                ),
                
                widget.Sep(
                    linewidth=3,
                    foreground=["#315963", "#c2e5e1"],
                    padding=10,
                    background=None
                ),

                widget.TextBox(
                    text="",
                    fontsize=16,
                    foreground=["#365864", "#d9f2ec"],
                ),

                widget.Net(
                    foreground=["#365864", "#d9f2ec"],
                    interface='enp6s0',
                    format="{total}",
                ),

                widget.Sep(
                    linewidth=3,
                    foreground=["#032633", "#c2e5e1"],
                    padding=10,
                    background=None
                ),

                widget.TextBox(
                    text=" ",
                    foreground=["#365864", "#d9f2ec"],
                    fontsize=18,
                    padding=5,
                ),

                widget.CheckUpdates(
                    colour_have_updates=["#365864", "#d9f2ec"],
                    colour_no_updates=["#365864", "#d9f2ec"],
                    display_format='{updates}',
                    distro='Arch_checkupdates',
                    no_update_string="0",
                    update_interval=1800,
                    fontsize="14",
                ),
                
                widget.Sep(
                    linewidth=3,
                    foreground=["#032633", "#c2e5e1"],
                    padding=10,
                    background=None
                ),

                widget.TextBox(
                    text=" ",
                    foreground=["#365864", "#d9f2ec"],
                    fontsize=18,
                    padding=5,
                ),

                widget.CurrentLayout(
                    foreground=["#365864", "#d9f2ec"],
                    scale=0.60
                ),

                widget.Sep(
                    linewidth=3,
                    foreground=["#032633", "#c2e5e1"],
                    padding=10,
                    background=None
                ),
                
                widget.TextBox(
                    text=" ",
                    fontsize=19,
                    foreground=["#365864", "#d9f2ec"],
                ),
                
                
                widget.Clock(foreground=["#365864", "#d9f2ec"], format='%H:%M - %d/%m/%Y ',
                    fontsize="14",
                ),    
            ],
            30,
            opacity=0.80,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=["#000000", "#000000"],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
