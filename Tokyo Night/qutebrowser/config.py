config.load_autoconfig(False)

# ========== Appearance ==========
c.fonts.default_family = "Monocraft"
c.fonts.default_size = "12pt"

c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = 'smart'
c.colors.webpage.darkmode.threshold.foreground = 150

c.tabs.position = "left"
c.tabs.width = 200
c.tabs.show = 'always'

# Tokyo Night colors for tabs
c.colors.tabs.bar.bg = '#1a1b26'
c.colors.tabs.even.bg = '#1a1b26'
c.colors.tabs.odd.bg = '#1a1b26'
c.colors.tabs.even.fg = '#c0caf5'
c.colors.tabs.odd.fg = '#c0caf5'
c.colors.tabs.selected.even.bg = '#2a2b3f'
c.colors.tabs.selected.odd.bg = '#2a2b3f'
c.colors.tabs.selected.even.fg = '#c0caf5'
c.colors.tabs.selected.odd.fg = '#c0caf5'
c.colors.tabs.indicator.start = '#7aa2f7'
c.colors.tabs.indicator.stop = '#7aa2f7'
c.colors.tabs.indicator.error = '#f7768e'

# Statusbar
c.colors.statusbar.normal.bg = '#1a1b26'
c.colors.statusbar.normal.fg = '#c0caf5'
c.colors.statusbar.insert.bg = '#7aa2f7'
c.colors.statusbar.insert.fg = '#1a1b26'
c.colors.statusbar.command.bg = '#1a1b26'
c.colors.statusbar.command.fg = '#c0caf5'
c.colors.statusbar.passthrough.bg = '#9ece6a'
c.colors.statusbar.passthrough.fg = '#1a1b26'
c.colors.statusbar.private.bg = '#bb9af7'
c.colors.statusbar.private.fg = '#1a1b26'

# Completion & prompts
c.colors.completion.category.bg = '#1a1b26'
c.colors.completion.category.fg = '#7aa2f7'
c.colors.completion.category.border.top = '#1a1b26'
c.colors.completion.category.border.bottom = '#1a1b26'
# c.colors.completion.item.selected.bg = '#2a2b3f'
# c.colors.completion.item.selected.fg = '#c0caf5'
c.colors.completion.item.selected.border.top = '#2a2b3f'
c.colors.completion.item.selected.border.bottom = '#2a2b3f'
c.colors.completion.item.selected.match.fg = '#bb9af7'
# c.colors.completion.item.fg = '#c0caf5'
# c.colors.completion.item.bg = '#1a1b26'
# c.colors.completion.item.match.fg = '#7aa2f7'
c.colors.completion.scrollbar.bg = '#1a1b26'
c.colors.completion.scrollbar.fg = '#7aa2f7'

c.colors.prompts.bg = '#1a1b26'
c.colors.prompts.fg = '#c0caf5'
c.colors.prompts.selected.bg = '#2a2b3f'
c.colors.prompts.selected.fg = '#c0caf5'
c.colors.prompts.border = '#1a1b26'

c.colors.hints.bg = '#7aa2f7'
c.colors.hints.fg = '#1a1b26'
c.colors.hints.match.fg = '#1a1b26'

# Keyhints
c.colors.keyhint.bg = '#1a1b26'
c.colors.keyhint.fg = '#c0caf5'
c.colors.keyhint.suffix.fg = '#7aa2f7'

# Messages
c.colors.messages.info.bg = '#1a1b26'
c.colors.messages.info.fg = '#c0caf5'
c.colors.messages.warning.bg = '#e0af68'
c.colors.messages.warning.fg = '#1a1b26'
c.colors.messages.error.bg = '#f7768e'
c.colors.messages.error.fg = '#1a1b26'

# Start page & default
c.url.start_pages = ["https://start.duckduckgo.com/"]
c.url.default_page = "https://start.duckduckgo.com/"
c.tabs.last_close = 'startpage'

# ========== Input ==========
c.input.insert_mode.auto_load = False
c.input.insert_mode.auto_enter = True
c.input.insert_mode.auto_leave = True

# ========== Scrolling ==========
c.scrolling.smooth = False
c.scrolling.bar = 'always'

# ========== Keybinds ==========
# Quick site launchers
config.bind('yt', 'open https://www.youtube.com/')
config.bind('ch', 'open https://chat.openai.com/')
config.bind('pe', 'open https://www.perplexity.ai/')
config.bind('m', 'open https://modrinth.com/')
config.bind('n', 'open -t https://start.duckduckgo.com/')  # background tab
config.bind('a', 'open https://archlinux.org/')
config.bind('au', 'open https://aur.archlinux.org/')

# Sidebar toggle
config.bind('s', 'config-cycle tabs.show always never')

# Disable hints
config.unbind('f')
config.unbind('F')
config.unbind('gf')

# Tab clone
config.bind('tc', 'tab-clone')

# Arrow scrolling
config.bind('<Left>', 'scroll left')
config.bind('<Right>', 'scroll right')
config.bind('<Up>', 'scroll up')
config.bind('<Down>', 'scroll down')

# Toggle between left and bottom tabs
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

c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

# Aliases
c.aliases['!yt'] = 'open !yt {}'
c.aliases['!gh'] = 'open !gh {}'
c.aliases['!aw'] = 'open !aw {}'
c.aliases['!apkg'] = 'open !apkg {}'
c.aliases['!ddg'] = 'open -t {}'  # DuckDuckGo alias opens in background

# Smart URL detection for :o
def is_url(text: str) -> str:
    if '.' in text or text.startswith('localhost'):
        if not text.startswith(('http://', 'https://')):
            text = 'https://' + text
        return f'open {text}'  # current tab
    return f'open -t https://duckduckgo.com/?q={text}'  # DuckDuckGo background

config.bind('o', 'prompt --tab "Open URL or search:" "python is_url({})"')

# -----------------
# Additional stuff
# -----------------
c.content.tls.certificate_errors = "load-insecurely"

