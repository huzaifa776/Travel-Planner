import gradio as gr
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

load_dotenv()

def generate_itineary(city: str, interests: str) -> str:
    city = city.strip()
    interests = interests.strip()

    if not city or not interests:
        return "Please fill City and Interest to move forward"

    planner = TravelPlanner()
    planner.set_city(city)
    planner.set_interests(interests)
    return planner.create_itineary()


with gr.Blocks(title="AI Travel Planner") as app:
    gr.Markdown("# AI Travel Itineary Planner")
    gr.Markdown("Plan your day trip itineary by entering your city and interests")

    with gr.Row():
        city_input = gr.Textbox(label="Enter the city name for your trip")
        interests_input = gr.Textbox(label="Enter your interests (comma-seperated )")

    submit_button = gr.Button("Generate itineary")
    output = gr.Markdown(label="Your Itineary")

    submit_button.click(
        fn=generate_itineary,
        inputs=[city_input, interests_input],
        outputs=output,
    )


if __name__ == "__main__":
    app.launch()



