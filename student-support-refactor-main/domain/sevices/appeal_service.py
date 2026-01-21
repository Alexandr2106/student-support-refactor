from infrastructure.notifications.factories import AbstractMessengerFactory

class AppealService:
    def __init__(self, data_source, messenger_factory: AbstractMessengerFactory):
        self.data_source = data_source
        self.messenger_factory = messenger_factory

    def update_appeal_status(self, appeal_id: str, new_status: str):
        appeal = self.data_source.get_appeal(appeal_id)
        appeal.status = new_status
        self.data_source.save_appeal(appeal)

        # Отправка уведомления
        client = self.messenger_factory.create_client()
        auth = self.messenger_factory.create_auth()
        serializer = self.messenger_factory.create_serializer()
        error_handler = self.messenger_factory.create_error_handler()

        try:
            token = auth.get_token()
            if not token:
                raise Exception("Auth failed")
            message = serializer.serialize(
                appeal_id=appeal.id,
                status=appeal.status,
                student_name=appeal.student_name
            )
            client.send(message)
        except Exception as e:
            error_handler.handle(e)
