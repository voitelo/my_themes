config.load_autoconfig(False)

# ========================================
# General Appearance
# ========================================
c.fonts.default_family = "Monocraft"
c.fonts.default_size = "12pt"

c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'smart'
c.colors.webpage.darkmode.threshold.foreground = 150
c.colors.webpage.bg = "#2d1a22"

c.tabs.position = "left"
c.tabs.width = 200
c.tabs.show = "always"
c.tabs.last_close = "startpage"

c.url.start_pages = ["https://start.duckduckgo.com/"]
c.url.default_page = "https://start.duckduckgo.com/"

# ========================================
# Input
# ========================================
c.input.insert_mode.auto_load = False
c.input.insert_mode.auto_enter = True
c.input.insert_mode.auto_leave = True

# ========================================
# Scrolling
# ========================================
c.scrolling.smooth = False
c.scrolling.bar = "always"

# ========================================
# Keybinds
# ========================================
config.bind('yt', 'open https://www.youtube.com/')
config.bind('ch', 'open https://chat.openai.com/')
config.bind('pe', 'open https://www.perplexity.ai/')
config.bind('m', 'open https://modrinth.com/')
config.bind('n', 'open -t https://start.duckduckgo.com/')
config.bind('a', 'open https://archlinux.org/')
config.bind('au', 'open https://aur.archlinux.org/')

config.bind('s', 'config-cycle tabs.show always never')

config.unbind('f')
config.unbind('F')
config.unbind('gf')

config.bind('tc', 'tab-clone')

config.bind('<Left>', 'scroll left')
config.bind('<Right>', 'scroll right')
config.bind('<Up>', 'scroll up')
config.bind('<Down>', 'scroll down')

config.bind('tt', 'config-cycle tabs.position left bottom')

# ========================================
# Search engines
# ========================================
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    '!aw': 'https://wiki.archlinux.org/?search={}',
    '!pkg': 'https://archlinux.org/packages/?sort=&q={}&maintainer=&flagged=',
    '!gh': 'https://github.com/search?o=desc&q={}&s=stars',
    '!yt': 'https://www.youtube.com/results?search_query={}',
}
c.completion.open_categories = [
    'searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem'
]

# ========================================
# Aliases
# ========================================
c.aliases['!yt'] = 'open !yt {}'
c.aliases['!gh'] = 'open !gh {}'
c.aliases['!aw'] = 'open !aw {}'
c.aliases['!apkg'] = 'open !apkg {}'
c.aliases['!ddg'] = 'open -t {}'

# ========================================
# Smart URL detection for :o
# ========================================
def is_url(text: str) -> str:
    if '.' in text or text.startswith('localhost'):
        if not text.startswith(('http://', 'https://')):
            text = 'https://' + text
        return f'open {text}'
    return f'open -t https://duckduckgo.com/?q={text}'

config.bind('o', 'prompt --tab "Open URL or search:" "python is_url({})"')

# ========================================
# Security / TLS
# ========================================
c.content.tls.certificate_errors = "load-insecurely"

# ========================================
# Cherry Grove Theme 🌸
# ========================================
cherry_grove = {
    "bg0": "#2d1a22",
    "bg1": "#3a2c36",
    "bg2": "#5a4754",
    "fg":  "#f4e1dc",
    "fg_dim": "#b7d9a7",
    "red": "#f28fa1",
    "green": "#b7d9a7",
    "yellow": "#f2c2a0",
    "blue": "#a3c4f0",
    "magenta": "#e6b3d1",
    "cyan": "#9bd3c4",
    "gray": "#5a4754",
}

# Tabs
c.colors.tabs.bar.bg = cherry_grove["bg0"]
c.colors.tabs.even.bg = cherry_grove["bg1"]
c.colors.tabs.odd.bg = cherry_grove["bg1"]
c.colors.tabs.selected.even.bg = cherry_grove["bg2"]
c.colors.tabs.selected.odd.bg = cherry_grove["bg2"]
c.colors.tabs.even.fg = cherry_grove["fg"]
c.colors.tabs.odd.fg = cherry_grove["fg"]
c.colors.tabs.selected.even.fg = cherry_grove["fg"]
c.colors.tabs.selected.odd.fg = cherry_grove["fg"]

# Statusbar
c.colors.statusbar.normal.bg = cherry_grove["bg0"]
c.colors.statusbar.normal.fg = cherry_grove["fg"]
c.colors.statusbar.insert.bg = cherry_grove["green"]
c.colors.statusbar.insert.fg = cherry_grove["bg0"]
c.colors.statusbar.command.bg = cherry_grove["bg1"]
c.colors.statusbar.command.fg = cherry_grove["fg"]
c.colors.statusbar.url.success.http.fg = cherry_grove["blue"]
c.colors.statusbar.url.success.https.fg = cherry_grove["green"]
c.colors.statusbar.url.error.fg = cherry_grove["red"]

# Completion
c.colors.completion.fg = cherry_grove["fg"]
c.colors.completion.odd.bg = cherry_grove["bg1"]
c.colors.completion.even.bg = cherry_grove["bg0"]
c.colors.completion.category.bg = cherry_grove["bg2"]
c.colors.completion.category.fg = cherry_grove["yellow"]
c.colors.completion.item.selected.bg = cherry_grove["bg2"]
c.colors.completion.item.selected.fg = cherry_grove["fg"]
c.colors.completion.match.fg = cherry_grove["green"]

# Prompts
c.colors.prompts.bg = cherry_grove["bg1"]
c.colors.prompts.fg = cherry_grove["fg"]
c.colors.prompts.border = f"1px solid {cherry_grove['bg2']}"

# Downloads
c.colors.downloads.bar.bg = cherry_grove["bg0"]
c.colors.downloads.start.bg = cherry_grove["blue"]
c.colors.downloads.stop.bg = cherry_grove["green"]
c.colors.downloads.error.bg = cherry_grove["red"]

# Hints
c.colors.hints.bg = cherry_grove["yellow"]
c.colors.hints.fg = cherry_grove["bg0"]
c.colors.hints.match.fg = cherry_grove["red"]

# Messages
c.colors.messages.error.bg = cherry_grove["red"]
c.colors.messages.error.fg = cherry_grove["bg0"]
c.colors.messages.info.bg = cherry_grove["bg1"]
c.colors.messages.info.fg = cherry_grove["fg"]
c.colors.messages.warning.bg = cherry_grove["yellow"]
c.colors.messages.warning.fg = cherry_grove["bg0"]

# Context menu
c.colors.contextmenu.menu.bg = cherry_grove["bg0"]
c.colors.contextmenu.menu.fg = cherry_grove["fg"]
c.colors.contextmenu.selected.bg = cherry_grove["bg2"]
c.colors.contextmenu.selected.fg = cherry_grove["fg"]

# Progress / downloads
c.colors.downloads.system.bg = "none"

