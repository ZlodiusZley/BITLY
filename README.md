# Обрезка ссылок с помощью Битли

Проект для сокращения ссылок. И покажет сколько было переходов по ним

## Как установить
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Рекоминдуется использовать
```
virtual/venv
```
Перед запуском программы не забудьте склонировать объект или скачать его в архив. В папке архивом не забудьте создать env файл где вы укажите ваш собственный токен Битли [Создать токен](https://app.bitly.com/BnaadMNo1ag/create/создать)
```
apikey_bitly=ваш токен с bitly
```

## Как запустить файл
Для сокращения ссылки необходимо запустить файл где в качестве аргумента будет ваша ссылка:
```
python main.py https:/dvmn.org/modules/
```
Для подсчета перехода по ссылке Битли необходимо запустить файл, где в качестве аргумента будет ваш Битлинк:
```
python main.py https:/bit.ly/3N9ThBf
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org.](https://dvmn.org/modules/web-api/lesson/migration-from-website/#9)
