## Проект по тестированию сервиса Trello  
----
> Trello - инструмент, который позволяет вашей команде управлять проектами, рабочими процессами и заданиям любых типов.  
> [Сайт Trello](https://trello.com/home)

![](assets/trello_main_page.PNG)
----
### Список проверок, реализованных в автотестах: 


### Проект реализован с использованием:  

<p  align="left">
<code><img width="5%" title="python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
<code><img width="5%" title="selene" src="https://github.com/MDN78/MDN78/blob/main/assets/selene.png"></code>
<code><img width="5%" title="selenium" src="https://github.com/MDN78/MDN78/blob/main/assets/selenium.png"></code>
<code><img width="5%" title="requests" src="https://github.com/MDN78/MDN78/blob/main/assets/requests.png"></code>
<code><img width="5%" title="pytest" src="https://github.com/MDN78/MDN78/blob/main/assets/pytest.png"></code>
<code><img width="5%" title="allure" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_report.png"></code>
<code><img width="5%" title="alluretestops" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_testops.png"></code>
<code><img width="5%" title="pycharm" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg"></code>  

### Локальный запуск
1. Получить API key & Token via Trello service
2. Создать файл `test_data.json` и наполнить тестовыми данными в формате:
```json
{
    "key": "3d8eb615e7abdd4dbe36bcche656f9",
    "token": "ATTA047246b1dc3478903f1f804ecdfd15c31b8caa37bf2fc515ae56432b1096ef234A4FDFCE0",
    "email": "test@test.com",
    "password": "123456789",
    "username": "Semen",
    "org_id": "63558b830d636136d0181047"
}
```

