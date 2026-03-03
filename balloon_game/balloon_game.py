import reflex as rx
import random
import asyncio

class State(rx.State):
    # Game Data
    char: str = "A"
    color: str = "#FF595E"
    score: int = 0
    input_value: str = ""
    is_popping: bool = False

    def reset_game(self):
        """Resets the game and refocuses the hidden input."""
        self.score = 0
        self.char = "A"
        self.input_value = ""
        return rx.set_focus("balloon-input")

    async def handle_input(self, val: str):
        """Processes keyboard input and handles sound/animations."""
        if not val:
            return
        
        typed_char = val[-1].upper()
        self.input_value = "" 

        # Clean Slate for Audio
        yield rx.call_script("""
            document.querySelectorAll('audio').forEach(audio => {
                audio.pause();
                audio.currentTime = 0;
            });
        """)

        if typed_char == self.char:
            self.score += 1
            self.is_popping = True
            
            yield rx.call_script("document.getElementById('success-snd').play();")
            
            await asyncio.sleep(0.15)
            self.char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            self.color = random.choice(["#FF595E", "#FFCA3A", "#8AC926", "#1982C4", "#6A4C93", "#FF924C"])
            self.is_popping = False
        else:
            yield rx.call_script("document.getElementById('fail-snd').play();")

def index() -> rx.Component:
    return rx.center(
        # Audio Elements
        rx.el.audio(src="/clapping.mp3", id="success-snd", controls=False, preload="auto"),
        rx.el.audio(src="/oops.mp3", id="fail-snd", controls=False, preload="auto"),

        # 1. THE HIDDEN INPUT (Moved to a lower layer)
        rx.input(
            id="balloon-input",
            value=State.input_value,
            on_change=State.handle_input,
            opacity="0",
            position="absolute",
            width="100%",
            height="100%",
            auto_focus=True,
            z_index="0", # Bottom layer
        ),
        
        # 2. THE UI LAYOUT (Moved to a higher layer)
        rx.vstack(
            rx.heading(f"Score: {State.score}", size="9", color="white"),
            
            rx.vstack(
                rx.center(
                    rx.text(State.char, font_size="5em", color="white", font_weight="bold"),
                    width="200px", height="250px",
                    background=f"radial-gradient(circle at 30% 30%, {State.color}, #00000044)",
                    border_radius="50% 50% 50% 50% / 40% 40% 60% 60%",
                    box_shadow="0 20px 40px rgba(0,0,0,0.3)",
                    transform=rx.cond(State.is_popping, "scale(1.4)", "scale(1)"),
                    opacity=rx.cond(State.is_popping, 0, 1),
                    transition="all 0.15s ease-out",
                ),
                rx.box(width="3px", height="80px", background_color="white", opacity="0.6"),
                align="center",
                spacing="0",
            ),
            
            rx.text("Type the letter to pop!", color="white", font_size="1.5em", margin_top="20px"),
            
            rx.button(
                "Restart Game", 
                on_click=State.reset_game,
                color_scheme="gray",
                variant="outline",
                margin_top="30px",
                style={"color": "white", "border-color": "white", "cursor": "pointer"},
                _hover={"background": "rgba(255,255,255,0.2)"},
            ),
            
            align="center",
            spacing="5",
            z_index="10", # Top layer - makes it clickable!
        ),
        width="100%",
        height="100vh",
        background="linear-gradient(to top, #87CEEB, #00BFFF)",
    )

# App instance
app = rx.App()
app.add_page(index, title="Balloon Pop Game")