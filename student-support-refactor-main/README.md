Ссылка на репозиторий - [https://github.com/Alexandr2106/student-support-refactor.git](https://github.com/Alexandr2106/student-support-refactor.git)
## Конфигурация

Файл `config.yaml` определяет тип источника данных:

```yaml
dataSourceType: db 

notificationProvider: provider_a

```bash
pip install pytest pyyaml
pytest tests/ -v
