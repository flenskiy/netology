import os
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = os.path.basename(file_path)
        href = self.__get_upload_link(file_name=file_name)
        with open(file_path, 'rb') as file:
            try:
                response = requests.put(url=href, files={'file': file})
                if response.ok:
                    return response.status_code
                else:
                    raise Exception(response.status_code)
            except Exception as error:
                print(f'Error: {error}')

    def __get_upload_link(self, file_name: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_name, 'overwrite': False}
        headers = {'Authorization': f'OAuth {self.token}'}
        try:
            response = requests.get(url=url, params=params, headers=headers)
            if response.ok:
                return response.json()['href']
            else:
                raise Exception(response.status_code)
        except Exception as error:
            print(f'Error: {error}')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
