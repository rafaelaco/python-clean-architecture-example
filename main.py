from adapters.controller import Controller
from infrastructure.graphical_user_interface import GraphicalUserInterface
import dependency_injection as di


def main():
    controller: Controller = di.get_controller()
    gui: GraphicalUserInterface = di.get_graphic_user_interface()

    gui.handle_input_request(controller)


if __name__ == "__main__":
    main()
