import math
######################################################################
def draw_separator(text: str, num_emoji: int = 0, extra: float = 0.0) -> str:

    text_value = extra + (1.95 * num_emoji)

    for c in text:
        if c == "'":
            text_value += 0.25
        elif c in ("i", "j", ".", " "):
            text_value += 0.30
        elif c in ("I", "!", ";", "|", ","):
            text_value += 0.35
        elif c in ("f", "l", "`", "[", "]"):
            text_value += 0.40
        elif c in ("(", ")", "t"):
            text_value += 0.45
        elif c in ("r", "t", "1" "{", "}", '"', "\\", "/"):
            text_value += 0.50
        elif c in ("s", "z", "*", "-"):
            text_value += 0.60
        elif c in ("x", "^"):
            text_value += 0.65
        elif c in ("a", "c", "e", "g", "k", "v", "y", "J", "7", "_", "=", "+", "~", "<", ">", "?"):
            text_value += 0.70
        elif c in ("n", "o", "u", "2", "5", "6", "8", "9"):
            text_value += 0.75
        elif c in ("b", "d", "h", "p", "q", "E", "F", "L", "S", "T", "Z", "3", "4", "$"):
            text_value += 0.80
        elif c in ("P", "V", "X", "Y", "0"):
            text_value += 0.85
        elif c in ("A", "B", "C", "D", "K", "R", "#", "&"):
            text_value += 0.90
        elif c in ("G", "H", "U"):
            text_value += 0.95
        elif c in ("w", "N", "O", "Q", "%"):
            text_value += 1.0
        elif c in ("m", "W"):
            text_value += 1.15
        elif c == "M":
            text_value += 1.2
        elif c == "@":
            text_value += 1.3

    return "═" * math.ceil(text_value)
  
######################################################################
### EXAMPLE ###
######################################################################
# import make_embed
#
# sample_text = "My super cool text string thing!"
# emoji = "👍"
#
# embed = make_embed(
#     title="Get Ready to Be Amazed",
#     description=(
#         f"{sample_text}\n"
#         f"{draw_separator(sample_text)}\n\n"
#        
#         f"{emoji} {sample_text} {emoji}\n"
#         f"{draw_separator(sample_text, num_emoji=2)}"
#     )
# )
#
#
#  __________________________________________________
# |                                                  |
# |             Get Ready to Be Amazed               |
# |                                                  |
# |                                                  |
# |        My super cool text string thing!          |
# |        ════════════════════════════════          |
# |                                                  |
# |                                                  |
# |     👍 My super cool text string thing! 👍      |
# |     ═══════════════════════════════════════      |
# |                                                  |
# |                                                  |
#  __________________________________________________
