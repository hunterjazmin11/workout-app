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

    # --- STEP 1: Base recommendation ---
    if has_injury:
        if primary_goal == "Improve flexibility or mobility":
            if intensity == "Low":
                base = "B"
            else:
                base = "C"
        elif primary_goal == "Build strength":
            if intensity == "High":
                base = "E"
            elif intensity == "Moderate":
                base = "E"
            else:
                base = "C"
        else:
            if intensity == "Low":
                base = "C"
            else:
                base = "A"
    else:
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

    # --- STEP 2: Secondary goal adjustments ---
    if secondary_goal == "Strength":
        if intensity == "High":
            base = "F"
        else:
            base = "D"
    elif secondary_goal == "Weight loss":
        if intensity == "High":
            base = "G"
        else:
            base = "F"
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

    # --- STEP 3: Time per session ---
    if time_per_session == "10-20 minutes":
        if intensity == "High":
            base = "G"
        elif base not in ["F", "G"]:
            base = "F"

    # --- STEP 4: Equipment ---
    if has_no_equipment:
        if base in ["D", "F", "H"]:
            base = "E" if base in ["D", "F"] else "C"

    # --- STEP 5: Experience level ---
    if experience == "Complete beginner":
        if intensity == "High" and base == "G":
            base = "F"
        if jumping_comfort <= 4:
            if base in ["G", "F", "H"]:
                if primary_goal == "Lose weight/burn fat":
                    base = "A"
                elif primary_goal == "Improve flexibility / mobility":
                    base = "B"
                else:
                    base = "C"

    return base

