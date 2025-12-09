import streamlit as st

# ----------------- Page config + basic styling -----------------

st.set_page_config(page_title="Workout Type Recommendation System", page_icon="💪")

st.markdown(
    """
    <style>
        /* Full background */
        .stApp {
            background-color: #E5E5E5;
        }

        /* Main content card */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 900px;
            margin: auto;
            background-color: #FFFFFF;
            border-radius: 14px;
            box-shadow: 0 0 12px rgba(0,0,0,0.6);
        }

        /* Text color */
        html, body, [class*="css"]  {
            color: #1B263B;
        }

        /* Survey + result cards */
        .recommend-box {
            background-color: #FFFFFF;
            border-radius: 14px;
            padding: 1.2rem;
            border: 1px solid #CBD5E0;
            box-shadow: 0 0 8px rgba(0,0,0,0.5);
            margin-top: 1.5rem;
            margin-bottom: 1.5rem;
        }

        /* Section divider */
        .custom-divider {
            height: 3px;
            background: linear-gradient(to right, #2EC4B6, #CBF3F0);
            border-radius: 10px;
            margin: 3rem 0;
        }

        /* Buttons */
        button {
            background-color: #2EC4B6 !important;
            color: #1B263B !important;
            border-radius: 10px !important;
            font-weight: 600;
        }

        /* Selectbox + inputs */
        .stSelectbox, .stSlider, .stRadio, .stMultiSelect {
            background-color: #FFFFFF !important;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ----------------- Workout type descriptions (A–H) -----------------

WORKOUT_TYPES = {
    "A": "Low-Impact Cardio – walking, cycling, low-impact aerobics, gentle steady-state cardio.",
    "B": "Pilates / Yoga / Mobility – flexibility, core strength, stretching, joint-friendly movement.",
    "C": "Low-Impact + Pilates Safety Blend – gentle cardio plus Pilates/yoga for people with injuries or pain.",
    "D": "Strength Training (Standard) – machines, dumbbells, or barbells with moderate loads.",
    "E": "Gentle / Bodyweight Strength – bodyweight or very light resistance, joint-friendly.",
    "F": "Circuit / HIIT-Style Strength – time-efficient strength circuits with minimal rest.",
    "G": "HIIT (High-Intensity Interval Training) – short intense intervals with rest, cardio or full-body.",
    "H": "Hybrid Functional Training – mixed strength, cardio, and mobility (bootcamp / F45-style).",
}

TYPE_EMOJIS = {
    "A": "🚶‍♂️",
    "B": "🧘‍♀️",
    "C": "🤸‍♀️",
    "D": "🏋️‍♂️",
    "E": "💪",
    "F": "⚡",
    "G": "🔥",
    "H": "🏃‍♀️",
}

WORKOUT_EXAMPLES = {
    "A": [
        "20–30 minutes brisk walking 3–4 days per week.",
        "Beginner bike: 10 minutes easy pace, 10 minutes moderate pace.",
    ],
    "B": [
        "20-minute beginner yoga flow focusing on hips and lower back.",
        "15 minutes of basic Pilates mat work (bridges, dead bugs, clamshells).",
    ],
    "C": [
        "10 minutes easy walking + 10 minutes gentle yoga for joints.",
        "5-minute warm-up walk, 10 minutes light Pilates, 5-minute stretch.",
    ],
    "D": [
        "Full-body strength 2–3x/week: squats, rows, chest press, shoulder press, core.",
        "3 sets of 8–12 reps for 4 basic lifts using machines or dumbbells.",
    ],
    "E": [
        "Bodyweight circuit: squats, glute bridges, wall push-ups, dead bugs (2–3 rounds).",
        "Beginner strength: chair squats, step-ups, bird dogs, standing calf raises.",
    ],
    "F": [
        "20-minute circuit: 40s work / 20s rest – squats, rows, lunges, push-ups, march in place.",
        "3 rounds: 10 goblet squats, 10 rows, 10 hip hinges, 30s fast walk or step-ups.",
    ],
    "G": [
        "8 rounds of 20s fast effort / 40s slow walk (bike, treadmill, or fast walk).",
        "10 x 30s fast pace / 60s easy pace on bike/rower.",
    ],
    "H": [
        "Bootcamp-style: 5 strength moves + 2 cardio moves + 1 mobility move (3 rounds).",
        "Hybrid day: squats + push-ups + rows, then 5–10 min brisk walk, then stretching.",
    ],
}

WORKOUT_RESOURCES = {
    "A": {
        "label": "Low-Impact Cardio",
        "links": [
            ("Aerobic Activity Ideas", "https://www.heart.org/en/healthy-living/fitness/fitness-basics/aha-recs-for-physical-activity-in-adults/"),
            ("At-home Cardio Workout Playlist", "https://www.youtube.com/playlist?list=PLN99XDk2SYr4EqI6foftUGsztysm1HfV1/"),
            ("What is Aerobic Activity", "https://my.clevelandclinic.org/health/articles/7050-aerobic-exercise/"),

        ],
    },
    "B": {
        "label": "Pilates / Yoga / Mobility",
        "links": [
            ("Yoga, a Harvard Study", "https://www.health.harvard.edu/staying-healthy/yoga-benefits-beyond-the-mat/"),
            ("Yoga Poses for Beginners", "https://www.verywellfit.com/essential-yoga-poses-for-beginners-3566747/"),
            ("Beginner Friendly Yoga Videos", "https://www.verywellfit.com/essential-yoga-poses-for-beginners-3566747/"),
            ("History of Pilates", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3666467/"),
            ("Pilates for Beginners", "https://www.healthline.com/health/fitness/pilates-for-beginners#common-mistakes/"),
            ("Pilates Workout Playlist for Beginners", "https://www.youtube.com/playlist?list=PLipSZg1JNsC9DZcCHkgjHwIIP1jMnRrr0/"),

        ],
    },
    "C": {
        "label": "Low-Impact + Pilates Safety Blend",
        "links": [
            ("Exercise with Joint Pain – Arthritis Foundation", "https://www.arthritis.org/health-wellness/exercise/"),
        ],
    },
    "D": {
        "label": "Standard Strength Training",
        "links": [
            ("What is Strength Training", "https://health.clevelandclinic.org/strength-training/"),
            ("Dumbbell Strength Workouts", "https://www.youtube.com/playlist?list=PLvf_LH4Nzg10XXtEkDOIuMln0EtIFmM0D/"),
            ("How to Start Lifting Weights", "https://www.healthline.com/health/how-to-start-lifting-weights#weight-training-exercises/"),

        ],
    },
    "E": {
        "label": "Gentle / Bodyweight Strength",
        "links": [
            ("Bodyweight Exercises for Beginners", "https://www.onepeloton.com/blog/beginner-bodyweight-exercises/"),
        ],
    },
    "F": {
        "label": "Circuit / HIIT-Style Strength",
        "links": [
            ("16 Beginner-Friendly Circuit Training Workouts", "https://wellfitinsider.com/workout-tips/best-circuit-training-workout-for-beginners/"),
            ("How to Create a Circuit Home Workout Infographic", "https://www.heart.org/en/healthy-living/fitness/getting-active/create-a-circuit-home-workout/"),
            ("What is Circuit Training", "https://www.verywellhealth.com/what-is-circuit-training-5224393/"),


        ],
    },
    "G": {
        "label": "HIIT (High-Intensity Interval Training)",
        "links": [
            ("What is HIIT?", "https://health.clevelandclinic.org/think-you-cant-do-high-intensity-interval-training-think-again/"),
            ("HIIT Workouts", "https://www.youtube.com/playlist?list=PL9jpSjr09H4dmRgJcTZQvu5ixoNxgrfX/"),
            ("HIIT Workout Plan: Beginner, Intermediate, and Advanced Exercises to Try", "https://hydrow.com/blog/hiit-workout-plan-beginner-intermediate-and-advanced-exercises-to-try/"),        ],
    },
    "H": {
        "label": "Hybrid Functional Training",
        "links": [
            ("Hybrid Training for Beginners", "https://www.inov8.com/us/blog/post/hybrid-training-for-beginners/"),
            ("What is Hybrid Training?", "https://www.gymshark.com/blog/article/what-is-hybrid-training-complete-guide?srsltid=AfmBOoq8pz_JkOef0FzIP4wwJ2qg0hsUrplH4bH-5t-SgJChvAPUk9zy/"),

        ],
    },
}

# ----------------- Rule-based logic -----------------

def recommend_workout(
    activity,
    primary_goal,
    secondary_goal,
    intensity,
    injuries,
    jumping_comfort,
    time_per_session,
    equipment,
    experience,
):
    has_injury = injuries == "Yes"
    has_no_equipment = ("None / bodyweight only" in equipment) or ("None" in equipment)

    # step 1: injury branch vs main goal branch
    if has_injury:
        # injury branch: stay in A, B, C, E as much as possible
        if primary_goal == "Build strength":
            if intensity == "Moderate":
                base = "D"
            else:
                base = "E"
        elif primary_goal == "Improve flexibility or mobility":
            if intensity == "Low":
                base = "B"
            else:
                base = "C"
        elif primary_goal in ["Lose weight/burn fat", "Increase endurance / cardio wellness"]:
            if intensity == "Low":
                base = "A"
            else:
                base = "C"
        else:
            base = "C"
    else:
        # main goal branch
        if primary_goal == "Build strength":
            if intensity == "High":
                base = "F"
            elif intensity == "Moderate":
                base = "D"
            else:
                base = "E"
        elif primary_goal == "Lose weight/burn fat":
            if intensity == "High":
                base = "G"
            elif intensity == "Moderate":
                base = "F"
            else:
                base = "A"
        elif primary_goal == "Improve flexibility or mobility":
            if intensity == "High":
                base = "H"
            else:
                base = "B"
        elif primary_goal == "Increase endurance / cardio wellness":
            if intensity == "High":
                base = "G"
            else:
                base = "A"
        else:
            base = "A"

    # step 2: secondary goal tweaks
    if secondary_goal != "No secondary goal":
        if secondary_goal == "Strength":
            if has_injury:
                base = "E"
            else:
                if intensity == "High":
                    base = "F"
                elif intensity == "Moderate":
                    base = "D"
                else:
                    base = "E"

        elif secondary_goal == "Weight loss":
            if has_injury:
                if intensity == "Low":
                    base = "A"
                else:
                    base = "C"
            else:
                if intensity == "High":
                    if base in ["D", "E", "F", "H"]:
                        base = "H"
                    else:
                        base = "G"
                elif intensity == "Moderate":
                    base = "F"
                else:
                    base = "A"

        elif secondary_goal == "Flexibility / mobility":
            if has_injury or intensity == "Low":
                base = "C"
            else:
                base = "B"

        elif secondary_goal == "Endurance":
            if intensity == "High":
                base = "G"
            else:
                base = "A"

    # step 3: time per session
    if time_per_session == "10-20 minutes":
        if intensity == "High":
            if base not in ["F", "G"]:
                base = "G"
        else:
            if base not in ["F", "G"]:
                base = "F"

    # step 4: equipment
    if has_no_equipment and base in ["D", "F", "H"]:
        if base in ["D", "F"]:
            base = "E"
        else:
            base = "C"

    # step 5: beginner safety and impact comfort
    if experience == "Complete beginner":
        if base == "G":
            if primary_goal == "Improve flexibility or mobility" or secondary_goal == "Flexibility / mobility":
                base = "B"
            else:
                base = "A"

    if jumping_comfort <= 4 and base in ["G", "F", "H"]:
        if primary_goal == "Lose weight/burn fat" or secondary_goal == "Weight loss":
            base = "A"
        elif primary_goal == "Improve flexibility or mobility" or secondary_goal == "Flexibility / mobility":
            base = "B" if not has_injury else "C"
        else:
            base = "C"

    return base

# ----------------- Detail page for each workout type -----------------

def show_workout_detail(code):
    label = WORKOUT_RESOURCES.get(code, {}).get("label", "")
    emoji = TYPE_EMOJIS.get(code, "")
    st.subheader(f"{emoji} Details for Workout Type {code} – {label}")
    st.write(WORKOUT_TYPES[code])

    st.markdown("**Example beginner-friendly workouts:**")
    examples = WORKOUT_EXAMPLES.get(code, [])
    if examples:
        for ex in examples:
            st.markdown(f"- {ex}")
    else:
        st.write("Examples coming soon.")

    resources = WORKOUT_RESOURCES.get(code, {}).get("links", [])
    if resources:
        st.markdown("**Helpful websites to learn more:**")
        for label, url in resources:
            st.markdown(f"- [{label}]({url})")

# ----------------- Survey UI -----------------

def survey_inputs():
    st.header("Beginner Workout Type Recommendation Survey")

    st.subheader("Basic Information")
    col1, col2 = st.columns(2)

    with col1:
        age_group = st.selectbox(
            "Age Group",
            ["Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"],
        )

        gender = st.selectbox(
            "Gender Identity",
            ["Woman", "Man", "Nonbinary", "Prefer not to say", "Other"],
        )

        activity = st.selectbox(
            "What is your current activity level?",
            [
                "Mostly inactive (rarely exercise)",
                "Lightly active (walk, light movement)",
                "Moderately active (exercise 1-2 times weekly)",
                "Active (exercise 3+ times weekly)",
            ],
        )

        medical_concerns = st.selectbox(
            "Do you have any medical concerns that may affect exercise?",
            ["Yes", "No", "Prefer not to say"],
        )

        if medical_concerns == "Yes":
            _ = st.text_input(
                "If you answered 'yes' above, please explain (optional)", ""
            )

        primary_goal = st.selectbox(
            "What is your primary fitness goal?",
            [
                "Build strength",
                "Lose weight/burn fat",
                "Improve flexibility or mobility",
                "Increase endurance / cardio wellness",
            ],
        )

        secondary_goal = st.selectbox(
            "Do you have a secondary goal?",
            [
                "No secondary goal",
                "Strength",
                "Weight loss",
                "Flexibility / mobility",
                "Endurance",
            ],
        )

        intensity = st.selectbox(
            "What workout intensity do you prefer or feel comfortable with?",
            ["Low", "Moderate", "High"],
        )

    with col2:
        environment = st.selectbox(
            "Which workout environment do you prefer?",
            ["Home", "Gym", "Outdoor", "No preference", "Other"],
        )

        pace = st.selectbox(
            "What pace do you prefer?",
            [
                "Slow and controlled",
                "Steady and moderate",
                "Fast and intense",
                "A mix of multiple styles",
            ],
        )

        experience = st.selectbox(
            "How would you describe your experience with exercise?",
            ["Complete beginner", "Some experience", "Experienced"],
        )

        used_programs = st.selectbox(
            "Have you used structured workout programs before?",
            ["Yes", "No"],
        )

        confidence = st.slider(
            "How confident do you feel starting a new routine?",
            min_value=1,
            max_value=10,
            value=5,
        )

        injuries = st.radio(
            "Do you have any current injuries or physical limits? (Joint pain, sprains, etc.)",
            ["Yes", "No"],
        )

        if injuries == "Yes":
            _injury_locations = st.multiselect(
                "If you answered 'yes', where? (optional)",
                [
                    "Knees",
                    "Lower back",
                    "Hips",
                    "Shoulders",
                    "Wrists",
                    "Cardio/breathing limitations",
                    "Other",
                ],
            )

    st.subheader("Impact, Equipment, and Schedule")
    col3, col4 = st.columns(2)

    with col3:
        jumping_comfort = st.slider(
            "How comfortable are you with jumping or high-impact movements?",
            min_value=1,
            max_value=10,
            value=5,
        )

        equipment = st.multiselect(
            "What equipment do you have access to?",
            [
                "None / bodyweight only",
                "Mat or open floor space",
                "Dumbbells",
                "Resistance bands",
                "Barbell",
                "Machines",
            ],
            default=["None / bodyweight only"],
        )

        days_per_week = st.selectbox(
            "How many days per week can you exercise?",
            ["1-2", "3-4", "5+", "None"],
        )

    with col4:
        time_per_session = st.selectbox(
            "How much time per session?",
            [
                "10-20 minutes",
                "20-35 minutes",
                "35-60 minutes",
                "60+ minutes",
                "None",
            ],
        )

        hardest_part = st.selectbox(
            "What makes sticking to a routine hardest for you?",
            [
                "Time",
                "Not knowing what to do",
                "Low motivation",
                "Work/school commitments",
                "Physical discomfort",
                "Lack of routine",
                "Other",
            ],
        )

        motivation = st.selectbox(
            "How motivated do you feel to start working out right now?",
            ["Not motivated", "Somewhat motivated", "Very motivated"],
        )

        hiit_feelings = st.selectbox(
            "How do you feel about intense styles like HIIT or CrossFit?",
            [
                "I enjoy intensity",
                "I'm open to trying",
                "I prefer moderate",
                "I prefer low-impact only",
            ],
        )

        structure_pref = st.selectbox(
            "How much structure do you like in your workouts?",
            ["Highly structured", "Some structure", "Flexible", "Doesn't matter"],
        )

    return (
        activity,
        primary_goal,
        secondary_goal,
        intensity,
        injuries,
        jumping_comfort,
        time_per_session,
        equipment,
        experience,
    )

# ----------------- Main app -----------------

def main():
    st.title("Workout Type Recommendation System 💪")
    st.write(
        """
This is my **Senior Capstone Project**.

It uses a survey and a **rule-based model** to recommend a beginner-friendly
**workout type (A–H)** based on your goals, comfort level, injuries, equipment, and time.
"""
    )

    user_inputs = survey_inputs()

    if st.button("Get My Recommended Workout Type"):
        code = recommend_workout(*user_inputs)

        label = WORKOUT_RESOURCES.get(code, {}).get("label", "")
        emoji = TYPE_EMOJIS.get(code, "")

        st.markdown("<div class='recommend-box'>", unsafe_allow_html=True)
        st.markdown(
        f"<h2 style='color:#2EC4B6;'>{emoji} Recommended Workout Type: {code} – {label}</h2>",
        unsafe_allow_html=True
    )

        st.write(WORKOUT_TYPES[code])
        st.markdown("</div>", unsafe_allow_html=True)

        st.info(
            "This recommendation is generated using a **rule-based model** "
            "based on your goals, intensity preference, injuries, time, and equipment."
        )

        show_workout_detail(code)

    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
    st.subheader("Browse All Workout Types")


    browse_code = st.selectbox(
        "Pick a workout type to learn more:",
        ["A", "B", "C", "D", "E", "F", "G", "H"],
        format_func=lambda c: f"{c} – {WORKOUT_RESOURCES[c]['label']}",
    )

    show_workout_detail(browse_code)


if __name__ == "__main__":
    main()
