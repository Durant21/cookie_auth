import pyramid_handlers
from cookie_auth.controllers.base_controller import BaseController
from cookie_auth.services.albums_service import AlbumsService


class AlbumsController(BaseController):
    @pyramid_handlers.action(renderer='templates/albums/index.pt')
    def index(self):
        # data / service access
        all_albums = AlbumsService.get_albums()

        # return the model
        return {'albums': all_albums}
