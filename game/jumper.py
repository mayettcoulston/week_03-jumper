from game.terminal_service import TerminalService

# 1) Add the class declaration. Use the following class comment.
class Jumper:

    """The person jumping with a parachute. 
    
    The responsibility of a Jumper is to keep track of stay a float in the air.
    """

# 2) Create the class constructor. Use the following method comment.
def _init_(self):

    self.terminalservice = TerminalService
    self._jumper = [
        """Constructs a new Jumper.
        """
        "   __",
        "//___\\",
        "\\   //",
        "  \\//",
        "    0",
        "  //\\",
        " //  \\",
        "",
        "^^^^^^^^^"
    ]
       
# 3) Create the draw_jumper(self) method. Use the following method comment.
def draw_jumper(self):
        """Gets the jumper situation."""
        for line in self._jumper:
            self.terminalservice.write_text(line)

        
def cut_line(self):
    self._jumper.pop(0)