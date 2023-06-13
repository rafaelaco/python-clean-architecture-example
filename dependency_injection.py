from adapters.controller import Controller
from adapters.controller_impl import ControllerImpl
from infrastructure.graphical_user_interface import GraphicalUserInterface
from infrastructure.web_api_impl import WebApiImpl
from infrastructure.file_repository_impl import FileRepositoryImpl

def get_controller() -> Controller:
    return ControllerImpl(FileRepositoryImpl())

def get_graphic_user_interface() -> GraphicalUserInterface:
    return WebApiImpl()