Poc - Redis vs Relacional.
===================

#### Múltiplas requisições - Diversas consultas simultânias no Mysql.
Prova de conceito entre o uso do banco chave-valor Redis se saíra melhor em questão de performance comparado com um relacional quando muitas requisições de consultas ao relacional.
Usaremos o redis como sistema de cache.


#### Instalação
Se preferir você pode acessar o repositório com diversos Poc entre redis e mysql sem precisar criar um projeto django para instalar essa app. [LINK](https://github.com/douglasbastos/redis_practice_with_django)

#### Configurando em sua máquina.

Necessários:
Django >= 1.8
django-redis-cache >= 1.6

    Configure/altere no settings seu projeto o cache.

    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': '127.0.0.1:6379',
            'TIMEOUT': 60*10,
            'OPTIONS': {
                'DB': 1,
            },
        },
    }