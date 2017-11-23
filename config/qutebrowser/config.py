# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Background color of the tab bar.
# Type: QtColor
c.colors.tabs.bar.bg = '#555555'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#504945'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#a89984'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#504945'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#a89984'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#a89984'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#282828'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#a89984'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = 'black'

# The proxy to use. In addition to the listed values, you can use a
# `socks://...` or `http://...` URL.
# Type: Proxy
# Valid values:
#   - system: Use the system wide proxy.
#   - none: Don't use any proxy
c.content.proxy = 'socks://127.0.0.1:33247/'

# The page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = ['https://www.baidu.com/']

# Bindings for normal mode
config.bind('<ctrl+i>', 'open-editor')
config.bind('<ctrl+o>', 'back')
config.bind('\\;', 'spawn --userscript ydcv')
config.bind('t', 'set-cmd-text -s :open -t')

# Bindings for insert mode
config.bind('<ctrl+k>', 'fake-key <Shift-End> ;; fake-key <Delete>', mode='insert')
config.bind('<ctrl+u>', 'fake-key <Shift+Home> ;; fake-key <Delete>', mode='insert')
config.bind('<ctrl+w>', 'fake-key <Ctrl-backspace>', mode='insert')
config.bind('jk', 'leave-mode', mode='insert')