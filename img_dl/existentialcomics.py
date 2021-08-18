from img_dl import DownloadImages
from bs4 import BeautifulSoup

import requests


class ExistentialComics(DownloadImages):
    base_url = "https://existentialcomics.com/"

    def save_image(self, soup: BeautifulSoup) -> None:
        img_s = soup.find_all('img', class_='comicImg')

        for img in img_s:
            super(ExistentialComics, self).save_image('https:' + img['src'])

    def get_latest_image(self) -> int:
        try:
            soup = BeautifulSoup(requests.get(self.base_url).text, 'html.parser')
            self.save_image(soup)

            prev_link = soup.find_all('meta', property='og:url')[0]['content'].split('/')
            return int(prev_link[-1] if prev_link[-1] != '' else prev_link[-2])

        except requests.RequestException:
            print(f"Error requesting '{self.base_url}'.")
        except Exception as e:
            print('An error occurred.')
            print(f"Details:\n{e}")

        return 0

    def get_image(self, position: int) -> None:
        url = f"{self.base_url}comic/{position}"

        try:
            soup = BeautifulSoup(requests.get(url).text, 'html.parser')
            self.save_image(soup)
        except requests.RequestException:
            print(f"Error requesting '{url}'.")
        except Exception as e:
            print("An error occurred.")
            print(f"Details:\n{e}")

    def get_from_count(self) -> None:
        if self.count > 0:
            pos_now = self.get_latest_image() - 1  # prev

            i = 0
            while i < self.count - 1 and pos_now > 0:
                pos = pos_now - i
                if pos > 0:
                    self.get_image(pos_now - i)
                else:
                    break
                i += 1