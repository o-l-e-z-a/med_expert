# Med_Expert
## API для небольшого мед центра :pill:, реализует след функционал:
- Вывод списка новостей, а также детальный просмотр конкретной новости <br/> 
- Вывод списка лицензий, а также детальный просмотр конкретной лицензии <br/>
- Вывод списка категорий <br/>
- Вывод услуг, принадлежащих к конкретной категории <br/>
- Вывод компаний, принадлежащих к конретному типу компании <br/>
- Реализация поиска по услугам <br/>

## Использованные технологии:
- Django, DRF <br/>
- PostgreSQL <br/>
- Docker <br/>

## Запуск проекта:
- git clone  <br/>
- cd med_expert <br/>
- создать .env файл со след константами: DEBUG, SECRET_KEY,DJANGO_ALLOWED_HOSTS,DB_ENGINE,DB_DATABASE,DB_USER,DB_PASSWORD,DB_HOST,DB_PORT
- docker-compose build <br/>
- docker-compose up <br/>
