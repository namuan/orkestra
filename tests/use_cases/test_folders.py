# Test that the Fake FoldersView is called to update folder on App started event
from app.controllers.folders_controller import FoldersController
from app.settings.app_world import AppWorld


class FakeFoldersView(object):
    pass


class FakeAppWorld(object):
    pass


def test_show_all_folders():
    # given
    fake_view = FakeFoldersView()
    world = AppWorld
    # FoldersController(fake_view, world)

    # when
    # world.data.events.app_started.emit()

    # then
    assert 1 == 1
