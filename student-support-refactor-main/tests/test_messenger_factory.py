from infrastructure.notifications.factories import ProviderAFactory, ProviderBFactory

def test_provider_a_creates_consistent_components():
    factory = ProviderAFactory()
    assert "ProviderA" in type(factory.create_client()).__name__
    assert "ProviderA" in type(factory.create_serializer()).__name__

def test_provider_b_creates_consistent_components():
    factory = ProviderBFactory()
    assert "ProviderB" in type(factory.create_client()).__name__

def test_notification_flow_with_provider_a(mocker):
    factory = ProviderAFactory()
    service = AppealService(MockDataSource(), factory)
    mock_send = mocker.patch.object(factory.create_client(), 'send', return_value=True)
    service.update_appeal_status("123", "Принято")
    mock_send.assert_called_once()
    assert "123" in mock_send.call_args[0][0]

def test_auth_failure_triggers_error_handler(mocker):
    factory = ProviderAFactory()
    service = AppealService(MockDataSource(), factory)
    mocker.patch.object(factory.create_auth(), 'get_token', return_value=None)
    mock_handle = mocker.patch.object(factory.create_error_handler(), 'handle')
    service.update_appeal_status("123", "Принято")
    mock_handle.assert_called_once()
