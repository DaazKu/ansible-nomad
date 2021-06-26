def test_service(host):
    """Validate nomad service."""
    nomad = host.service('nomad')

    assert nomad.is_running
    assert nomad.is_enabled
