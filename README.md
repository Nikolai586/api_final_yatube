# api_final
api final
Работа с постами:
  GET  http://localhost:8000/api/v1/posts/        #просмотреть все посты
       http://localhost:8000/api/v1/posts/{id}/   #Получить публикацию по id
  POST  http://localhost:8000/api/v1/posts/       #создание поста
  PUT   http://localhost:8000/api/v1/posts/{id}/  #Обновить публикацию по id
  PATCH http://localhost:8000/api/v1/posts/{id}/  #Частично обновить публикацию по id
  DELETE http://localhost:8000/api/v1/posts/{id}/ #Удалить публикацию по id
 
Работа с COMMENTS:
   GET  http://localhost:8000/api/v1/posts/{post_id}/comments/                #Получить список всех комментариев публикации
        http://localhost:8000/api/v1/posts/{post_id}/comments/{comment_id}/   #Получить комментарий для публикации по id
   POST http://localhost:8000/api/v1/posts/{post_id}/comments/                #Создать новый комментарий для публикации
   PUT  http://localhost:8000/api/v1/posts/{post_id}/comments/{comment_id}/   #Обновить комментарий для публикации по id
   PATCH http://localhost:8000/api/v1/posts/{post_id}/comments/{comment_id}/  #Частично обновить комментарий для публикации по id
   DELETE http://localhost:8000/api/v1/posts/{post_id}/comments/{comment_id}/ #Удалить комментарий для публикации по id
