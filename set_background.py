from sys import platform

import os


class SetBackground:
    def __init__(self, img_path) -> None:
        img_path: str = str(os.path.join(img_path) if os.path.isabs(img_path) else os.path.abspath(img_path))

        p = platform
        if p.startswith('win32'):  # or p.startswith('cygwin'):
            self.Windows(img_path)
        elif p.startswith('darwin'):
            self.Mac(img_path)
        elif p.startswith('linux'):
            self.Linux(img_path)
        else:
            print('Unsupported Operating System')

    class Windows:
        # https://github.com/judge2020/ghstatic.judge.sh/blob/master/ducky/wallpaper.ps1
        # use win api (PyWin32)
        # https://stackoverflow.com/questions/1977694/how-can-i-change-my-desktop-background-with-python
        # https://docs.python.org/3/library/winreg.html#winreg.OpenKey

        bg_styles: dict = {
            'center': [0, 0],
            'tile': [0, 1],
            'fill': [10, 0],
            'adjust': [6, 0],
            'fit': [2, 0],
            'stretch': [22, 0],
        }

        def __init__(self, img_path: str) -> None:
            """
            from command_runner.elevate import elevate
            elevate(self.set_bg(img_path))  # elevation fails???

            from elevate import elevate
            elevate(show_console=False, graphical=True)
            self.set_bg(img_path)
            """

            self.set_bg(img_path)

        def set_bg(self, img_path: str) -> None:
            import ctypes
            import winreg

            # SET IMAGES
            spi_set_desk_wallpaper: int = 0x14  # =20
            update_ini_file: int = 0x01
            send_win_ini_change: int = 0x02

            ctypes.windll.user32.SystemparametersInfoW(spi_set_desk_wallpaper, 0, img_path, update_ini_file | send_win_ini_change)

            # REGISTRY ACTIONS
            bg_style = self.bg_styles.get(self.choose_bg_style())

            # needs elevated permissions...
            reg_path: str = r"Control Panel\Desktop"
            reg_desktop = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)

            winreg.SetValueEx(reg_desktop, "WallpaperStyle", 0, winreg.REG_SZ, bg_style[0])
            winreg.SetValueEx(reg_desktop, "TileWallpaper", 0, winreg.REG_SZ, bg_style[1])

            # print(winreg.QueryValueEx(reg_desktop, "WallpaperStyle"))
            # print(winreg.QueryValueEx(reg_desktop, "TileWallpaper"))

            winreg.CloseKey(reg_desktop)

        def choose_bg_style(self) -> str:
            while True:
                style: str = input(f"Choose Background Style {self.bg_styles.keys()}: ").lower()

                if len(style) == 0:
                    return 'center'
                elif style in self.bg_styles.keys():
                    return style
                print(f"Your style '{style}' is not valid.\n")

    class Mac:
        def __init__(self, img_path: str) -> None:
            pass

    class Linux:
        def __init__(self, img_path: str) -> None:
            # https://stackoverflow.com/questions/2035657/what-is-my-current-desktop-environment/21213358

            desktop_env: str = os.environ.get('DESKTOP_SESSION').lower()

            if desktop_env.startswith('kde') or desktop_env.startswith('kubuntu'):
                self.kde_plasma()
            elif desktop_env.startswith('gnome'):
                pass
            elif desktop_env.startswith('lxde') or desktop_env.startswith('lubuntu'):
                pass
            else:
                print('Unsupported or no desktop environment found.')

        def kde_plasma(self) -> None:
            pass

        def gnome(self) -> None:
            pass

        def lxde(self) -> None:
            pass