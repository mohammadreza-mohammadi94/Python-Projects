import streamlit as st
import time
from monty_hall import simulate_game

# Set page configuration
st.set_page_config(
    layout="wide",
    page_title="Monty Hall Problem Simulator",
    page_icon="🚗"
)

# Sidebar for controls
with st.sidebar:
    st.header("⚙️ Simulation Controls")
    num_games = st.number_input(
        label="Number of simulations to run:",
        min_value=100,
        max_value=10000,
        value=1000,
        step=100,
        help="Select the number of times you want to run the simulation."
    )
    start_button = st.button("Start Simulation", type="primary")

# Main page layout
st.title("🚗 Monty Hall Problem Simulator")
st.markdown("""
This application simulates the famous **Monty Hall Problem**. 
- You pick one of three doors. Behind one is a car, and behind the other two are goats.
- The host, who knows what's behind the doors, opens one of the other doors to reveal a goat.
- You are then given the choice to **switch** your chosen door or **stay** with your original choice.
***
Run the simulation to see which strategy has a higher chance of winning the car!
""")

if start_button:
    # Create placeholders for live updates
    progress_bar = st.progress(0, text="Simulation in progress...")
    
    metric_col1, metric_col2 = st.columns(2)
    stay_metric_placeholder = metric_col1.empty()
    switch_metric_placeholder = metric_col2.empty()

    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        st.subheader("Win % (Staying)")
        stay_chart_placeholder = st.empty()
    with chart_col2:
        st.subheader("Win % (Switching)")
        switch_chart_placeholder = st.empty()

    # Initialize variables for simulation
    wins_no_switch = 0
    wins_switch = 0
    stay_history = []
    switch_history = []

    for i in range(num_games):
        # Correctly call the imported function
        num_wins_without_switching, num_wins_with_switching = simulate_game(1)

        wins_no_switch += num_wins_without_switching
        wins_switch += num_wins_with_switching

        # Calculate current win percentages
        current_stay_pct = (wins_no_switch / (i + 1))
        current_switch_pct = (wins_switch / (i + 1))
        
        stay_history.append(current_stay_pct)
        switch_history.append(current_switch_pct)

        # Update progress bar
        progress_bar.progress((i + 1) / num_games, text=f"Simulation in progress... ({i+1}/{num_games})")
        
        # Update metrics
        stay_metric_placeholder.metric(
            label="Win Percentage (Stay)",
            value=f"{current_stay_pct:.2%}",
        )
        switch_metric_placeholder.metric(
            label="Win Percentage (Switch)",
            value=f"{current_switch_pct:.2%}",
            delta=f"{(current_switch_pct - current_stay_pct):.2%}",
            delta_color="normal"
        )

        # Update charts with full history for a smoother look
        stay_chart_placeholder.line_chart(stay_history, use_container_width=True)
        switch_chart_placeholder.line_chart(switch_history, use_container_width=True)
        
        time.sleep(0.001) # Keep the delay for visual effect

    progress_bar.progress(1.0, text="Simulation Complete!")
else:
    st.info("Click the 'Start Simulation' button in the sidebar to begin.")