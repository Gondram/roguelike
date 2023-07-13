#!/usr/bin/env python3
import traceback

import tcod

import color
import exceptions
import input_handlers
import setup_game


def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine then save it."""
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")


def main() -> None:
    screen_width = 80
    screen_height = 50
    # ADOM maps are 80x25 for personal reference

    tileset = tcod.tileset.load_tilesheet(
        "inconsolata437.png", 16, 16, tcod.tileset.CHARMAP_CP437
        # I made a CP437 inconsolata tileset at http://mifki.com/df/fontgen/
        # import: {"fw":"normal","fn":"Inconsolata","fs":16,"dx":1,"dy":-3,"cw":11,"ch":16,"cust":{"1":{"dx":-4,"dy":-1,"ds":0},"2":{"dx":-4,"dy":-1,"ds":0},"3":{"dx":0,"dy":1,"ds":0},"4":{"dx":0,"dy":0,"ds":0},"5":{"dx":-1,"dy":0,"ds":0},"6":{"dx":0,"dy":0,"ds":0},"8":{"dx":-1,"dy":0,"ds":0},"11":{"dx":0,"dy":0,"ds":-4},"12":{"dx":0,"dy":-1,"ds":-4},"13":{"dx":1,"dy":1,"ds":-2},"14":{"dx":-1,"dy":0,"ds":-2},"15":{"dx":-2,"dy":0,"ds":-3},"19":{"dx":0,"dy":0,"ds":-1},"21":{"dx":0,"dy":0,"ds":0},"22":{"dx":0,"dy":-1,"ds":0},"23":{"dx":0,"dy":-3,"ds":-1},"30":{"dx":-3,"dy":2,"ds":-1},"31":{"dx":-3,"dy":-2,"ds":-1},"35":{"dx":0,"dy":0,"ds":2},"95":{"dx":0,"dy":0,"ds":0},"112":{"dx":0,"dy":0,"ds":0},"123":{"dx":0,"dy":-1,"ds":0},"124":{"dx":0,"dy":-1,"ds":0},"125":{"dx":0,"dy":-1,"ds":0},"141":{"dx":0,"dy":0,"ds":0},"142":{"dx":0,"dy":1,"ds":0},"143":{"dx":0,"dy":1,"ds":0},"144":{"dx":0,"dy":1,"ds":0},"146":{"dx":0,"dy":0,"ds":0},"165":{"dx":0,"dy":1,"ds":0},"166":{"dx":0,"dy":0,"ds":0},"168":{"dx":0,"dy":-1,"ds":0},"174":{"dx":0,"dy":-1,"ds":0},"175":{"dx":0,"dy":-1,"ds":0},"176":{"dx":-1,"dy":0,"ds":0},"177":{"dx":-1,"dy":0,"ds":0},"178":{"dx":-1,"dy":0,"ds":-1},"179":{"dx":-1,"dy":0,"ds":0},"180":{"dx":-1,"dy":0,"ds":0},"181":{"dx":-1,"dy":0,"ds":0},"182":{"dx":-1,"dy":0,"ds":0},"183":{"dx":-1,"dy":0,"ds":0},"184":{"dx":-1,"dy":0,"ds":0},"185":{"dx":-1,"dy":0,"ds":0},"186":{"dx":-1,"dy":0,"ds":0},"187":{"dx":-1,"dy":0,"ds":0},"188":{"dx":-1,"dy":0,"ds":0},"189":{"dx":-1,"dy":0,"ds":0},"190":{"dx":-1,"dy":0,"ds":0},"191":{"dx":-1,"dy":0,"ds":0},"192":{"dx":-1,"dy":0,"ds":0},"193":{"dx":-1,"dy":0,"ds":0},"194":{"dx":-1,"dy":0,"ds":0},"195":{"dx":-1,"dy":0,"ds":0},"196":{"dx":-1,"dy":0,"ds":0},"197":{"dx":-1,"dy":0,"ds":0},"198":{"dx":-1,"dy":0,"ds":0},"199":{"dx":-1,"dy":0,"ds":0},"200":{"dx":-1,"dy":0,"ds":0},"201":{"dx":-1,"dy":0,"ds":0},"202":{"dx":-1,"dy":0,"ds":0},"203":{"dx":-1,"dy":0,"ds":0},"204":{"dx":-1,"dy":0,"ds":0},"205":{"dx":-1,"dy":0,"ds":0},"206":{"dx":-1,"dy":0,"ds":0},"207":{"dx":-1,"dy":0,"ds":0},"208":{"dx":-1,"dy":0,"ds":0},"209":{"dx":-1,"dy":0,"ds":0},"210":{"dx":-1,"dy":0,"ds":0},"211":{"dx":-1,"dy":0,"ds":0},"212":{"dx":-1,"dy":0,"ds":0},"213":{"dx":-1,"dy":0,"ds":0},"214":{"dx":-1,"dy":0,"ds":0},"215":{"dx":-1,"dy":0,"ds":0},"216":{"dx":-1,"dy":0,"ds":0},"217":{"dx":-1,"dy":0,"ds":0},"218":{"dx":-1,"dy":0,"ds":0},"219":{"dx":-1,"dy":0,"ds":0},"220":{"dx":0,"dy":0,"ds":0},"221":{"dx":-1,"dy":0,"ds":0},"222":{"dx":-1,"dy":0,"ds":0},"223":{"dx":0,"dy":-1,"ds":0},"226":{"dx":0,"dy":0,"ds":0},"228":{"dx":0,"dy":0,"ds":-1},"232":{"dx":-1,"dy":0,"ds":0},"233":{"dx":-1,"dy":0,"ds":-1},"234":{"dx":-1,"dy":0,"ds":-2},"235":{"dx":0,"dy":0,"ds":0},"238":{"dx":1,"dy":0,"ds":0},"239":{"dx":-1,"dy":0,"ds":0},"240":{"dx":0,"dy":0,"ds":0},"243":{"dx":0,"dy":0,"ds":0},"245":{"dx":0,"dy":0,"ds":0},"247":{"dx":0,"dy":0,"ds":0},"251":{"dx":0,"dy":0,"ds":0},"254":{"dx":-1,"dy":-1,"ds":0}}}
    )

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:  # Handle exceptions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), color.error
                        )
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit.
            save_game(handler, "savegame.sav")
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise


if __name__ == "__main__":
    main()