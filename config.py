EXERCISE_CONFIGS = {

    "pushup": {

        "indices": {
            "left_shoulder": 5, "right_shoulder": 6,
            "left_elbow": 7, "right_elbow": 8,
            "left_wrist": 9, "right_wrist": 10
        },

        "angle_definition": {
            "left": ["left_shoulder", "left_elbow", "left_wrist"],
            "right": ["right_shoulder", "right_elbow", "right_wrist"]
        },

        "angle_thresholds": {
            "extended": 140,
            "flexed": 80,
            "min_range": 60
        },

        # coaching
        "form_targets": {
            "ideal_extended": 165,
            "ideal_flexed": 65,
            "ideal_range": 105
        },

        "speed_thresholds": {
            "fast": 0.8,
            "slow": 3.0
        },

        "logging": {"log_dir": "workout_logs"},

        "feedback": {
            "use_llm": True,
            "provider": "gemini",

        }
    },

    "bicep_curl": {

        "indices": {
            "left_shoulder": 5, "right_shoulder": 6,
            "left_elbow": 7, "right_elbow": 8,
            "left_wrist": 9, "right_wrist": 10
        },

        "angle_definition": {
            "left": ["left_shoulder", "left_elbow", "left_wrist"],
            "right": ["right_shoulder", "right_elbow", "right_wrist"]
        },

        "angle_thresholds": {
            "extended": 160,
            "flexed": 45,
            "min_range": 70
        },

        # coaching
        "form_targets": {
            "ideal_extended": 175,
            "ideal_flexed": 65,
            "ideal_range": 110
        },

        "speed_thresholds": {
            "fast": 0.6,
            "slow": 2.5
        },

        "logging": {"log_dir": "workout_logs"},

        "feedback": {
            "use_llm": True,
            "provider": "openai",

        }
    },

    "squat": {

        "indices": {
            "left_hip": 11, "right_hip": 12,
            "left_knee": 13, "right_knee": 14,
            "left_ankle": 15, "right_ankle": 16
        },

        "angle_definition": {
            "left": ["left_hip", "left_knee", "left_ankle"],
            "right": ["right_hip", "right_knee", "right_ankle"]
        },

        "angle_thresholds": {
            "extended": 160,
            "flexed": 80,
            "min_range": 70
        },

        # coaching
        "form_targets": {
            "ideal_extended": 170,
            "ideal_flexed": 65,
            "ideal_range": 110
        },
        "speed_thresholds": {
            "fast": 0.8,
            "slow": 4.0
        },

        "logging": {"log_dir": "workout_logs"},

        "feedback": {
            "use_llm": True,
            "provider": "openai",

        }
    },

    "lunge": {

        "indices": {
            "left_hip": 11, "right_hip": 12,
            "left_knee": 13, "right_knee": 14,
            "left_ankle": 15, "right_ankle": 16
        },

        "angle_definition": {
            "left": ["left_hip", "left_knee", "left_ankle"],
            "right": ["right_hip", "right_knee", "right_ankle"]
        },

        "angle_thresholds": {
            "extended": 170,
            "flexed": 80,
            "min_range": 60
        },

        # coaching
        "form_targets": {
            "ideal_extended": 175,
            "ideal_flexed": 65,
            "ideal_range": 110
        },

        "speed_thresholds": {
            "fast": 0.7,
            "slow": 3.5
        },

        "logging": {"log_dir": "workout_logs"},

        "feedback": {
            "use_llm": True,
            "provider": "openai",

        }
    },

    "shoulder_press": {

        "indices": {
            "left_elbow": 7, "right_elbow": 8,
            "left_shoulder": 5, "right_shoulder": 6,
            "left_hip": 11, "right_hip": 12
        },

        "angle_definition": {
            "left": ["left_elbow", "left_shoulder", "left_hip"],
            "right": ["right_elbow", "right_shoulder", "right_hip"]
        },

        "angle_thresholds": {
            "extended": 170,
            "flexed": 80,
            "min_range": 70
        },

        # coaching
        "form_targets": {
            "ideal_extended": 175,
            "ideal_flexed": 65,
            "ideal_range": 110
        },

        "speed_thresholds": {
            "fast": 0.6,
            "slow": 3.0
        },

        "logging": {"log_dir": "workout_logs"},

        "feedback": {
            "use_llm": True,
            "provider": "openai",

        }
    },

    "deadlift": {

        "indices": {
            "left_shoulder": 5, "right_shoulder": 6,
            "left_hip": 11, "right_hip": 12,
            "left_knee": 13, "right_knee": 14
        },

        "angle_definition": {
            "left": ["left_shoulder", "left_hip", "left_knee"],
            "right": ["right_shoulder", "right_hip", "right_knee"]
        },

        "angle_thresholds": {
            "extended": 180,
            "flexed": 100,
            "min_range": 60
        },

        # coaching
        "form_targets": {
            "ideal_extended": 175,
            "ideal_flexed": 65,
            "ideal_range": 110
        },

        "speed_thresholds": {
            "fast": 1.0,
            "slow": 4.0
        },

        "logging": {"log_dir": "workout_logs"},

        "feedback": {
            "use_llm": True,
            "provider": "openai",

        }
    },


"leg_extension": {

    "indices": {
        "left_hip": 11,
        "right_hip": 12,
        "left_knee": 13,
        "right_knee": 14,
        "left_ankle": 15,
        "right_ankle": 16
    },

    "angle_definition": {
        "left": ["left_hip", "left_knee", "left_ankle"],
        "right": ["right_hip", "right_knee", "right_ankle"]
    },

    "angle_thresholds": {
        "extended": 175,
        "flexed": 90,
        "min_range": 70
    },

    # coaching
    "form_targets": {
        "ideal_extended": 175,
        "ideal_flexed": 65,
        "ideal_range": 110
    },

    "speed_thresholds": {
        "fast": 0.6,
        "slow": 3.0
    },

    "logging": {"log_dir": "workout_logs"},

    "feedback": {
        "use_llm": True,
        "provider": "openai",

    }
},

"leg_curl": {

    "indices": {
        "left_hip": 11,
        "right_hip": 12,
        "left_knee": 13,
        "right_knee": 14,
        "left_ankle": 15,
        "right_ankle": 16
    },

    "angle_definition": {
        "left": ["left_hip", "left_knee", "left_ankle"],
        "right": ["right_hip", "right_knee", "right_ankle"]
    },

    "angle_thresholds": {
        "extended": 170,
        "flexed": 60,
        "min_range": 80
    },

    # coaching
    "form_targets": {
        "ideal_extended": 175,
        "ideal_flexed": 65,
        "ideal_range": 110
    },

    "speed_thresholds": {
        "fast": 0.7,
        "slow": 3.5
    },

    "logging": {"log_dir": "workout_logs"},

    "feedback": {
        "use_llm": True,
        "provider": "openai",

    }
},


"calf_raise": {

    "indices": {
        "left_hip": 11,
        "right_hip": 12,
        "left_knee": 13,
        "right_knee": 14,
        "left_ankle": 15,
        "right_ankle": 16
    },

    "angle_definition": {
        "left": ["left_hip", "left_knee", "left_ankle"],
        "right": ["right_hip", "right_knee", "right_ankle"]
    },

    "angle_thresholds": {
        "extended": 175,
        "flexed": 150,
        "min_range": 20
    },

    # coaching
    "form_targets": {
        "ideal_extended": 175,
        "ideal_flexed": 65,
        "ideal_range": 110
    },

    "speed_thresholds": {
        "fast": 0.5,
        "slow": 2.0
    },

    "logging": {"log_dir": "workout_logs"},

    "feedback": {
        "use_llm": True,
        "provider": "openai",

    }
},

"situp": {

    "indices": {
        "left_shoulder": 5,
        "right_shoulder": 6,
        "left_hip": 11,
        "right_hip": 12,
        "left_knee": 13,
        "right_knee": 14
    },

    "angle_definition": {
        "left": ["left_shoulder", "left_hip", "left_knee"],
        "right": ["right_shoulder", "right_hip", "right_knee"]
    },

    "angle_thresholds": {
        "extended": 160,
        "flexed": 80,
        "min_range": 60
    },

    # coaching
    "form_targets": {
        "ideal_extended": 175,
        "ideal_flexed": 65,
        "ideal_range": 110
    },

    "speed_thresholds": {
        "fast": 0.8,
        "slow": 3.5
    },

    "logging": {"log_dir": "workout_logs"},

    "feedback": {
        "use_llm": True,
        "provider": "openai",

    }
},
"crunch": {

    "indices": {
        "left_shoulder": 5,
        "right_shoulder": 6,
        "left_hip": 11,
        "right_hip": 12,
        "left_knee": 13,
        "right_knee": 14
    },

    "angle_definition": {
        "left": ["left_shoulder", "left_hip", "left_knee"],
        "right": ["right_shoulder", "right_hip", "right_knee"]
    },

    "angle_thresholds": {
        "extended": 150,
        "flexed": 95,
        "min_range": 40
    },

    # coaching
    "form_targets": {
        "ideal_extended": 175,
        "ideal_flexed": 65,
        "ideal_range": 110
    },

    "speed_thresholds": {
        "fast": 0.5,
        "slow": 2.5
    },

    "logging": {"log_dir": "workout_logs"},

    "feedback": {
        "use_llm": True,
        "provider": "openai",

    }
},

"tricep_extension": {

    "indices": {
        "left_shoulder": 5, "right_shoulder": 6,
        "left_elbow": 7, "right_elbow": 8,
        "left_wrist": 9, "right_wrist": 10
    },

    "angle_definition": {
        "left": ["left_shoulder", "left_elbow", "left_wrist"],
        "right": ["right_shoulder", "right_elbow", "right_wrist"]
    },

    "angle_thresholds": {
        "extended": 170,
        "flexed": 60,
        "min_range": 80
    },

    # coaching
    "form_targets": {
        "ideal_extended": 175,
        "ideal_flexed": 65,
        "ideal_range": 110
    },


    "speed_thresholds": {
        "fast": 0.6,
        "slow": 2.5
    },

    "logging": {"log_dir": "workout_logs"},

    "feedback": {
        "use_llm": True,
        "provider": "openai",

    }
},

"lateral_raise": {

    "indices": {
        "left_elbow": 7, "right_elbow": 8,
        "left_shoulder": 5, "right_shoulder": 6,
        "left_hip": 11, "right_hip": 12
    },

    "angle_definition": {
        "left": ["left_elbow", "left_shoulder", "left_hip"],
        "right": ["right_elbow", "right_shoulder", "right_hip"]
    },

    "angle_thresholds": {
        "extended": 95,
        "flexed": 20,
        "min_range": 60
    },

    # coaching
    "form_targets": {
        "ideal_extended": 175,
        "ideal_flexed": 65,
        "ideal_range": 110
    },

    "speed_thresholds": {
        "fast": 0.5,
        "slow": 2.5
    },

    "logging": {"log_dir": "workout_logs"},

    "feedback": {
        "use_llm": True,
        "provider": "openai",

    }
},

"front_raise": {

    "indices": {
        "left_elbow": 7, "right_elbow": 8,
        "left_shoulder": 5, "right_shoulder": 6,
        "left_hip": 11, "right_hip": 12
    },

    "angle_definition": {
        "left": ["left_elbow", "left_shoulder", "left_hip"],
        "right": ["right_elbow", "right_shoulder", "right_hip"]
    },

    "angle_thresholds": {
        "extended": 100,
        "flexed": 20,
        "min_range": 70
    },

    # coaching
    "form_targets": {
        "ideal_extended": 175,
        "ideal_flexed": 65,
        "ideal_range": 110
    },

    "speed_thresholds": {
        "fast": 0.5,
        "slow": 2.5
    },

    "logging": {"log_dir": "workout_logs"},

    "feedback": {
        "use_llm": True,
        "provider": "openai",

    }
},

"bent_over_row": {

    "indices": {
        "left_shoulder": 5, "right_shoulder": 6,
        "left_elbow": 7, "right_elbow": 8,
        "left_wrist": 9, "right_wrist": 10
    },

    "angle_definition": {
        "left": ["left_shoulder", "left_elbow", "left_wrist"],
        "right": ["right_shoulder", "right_elbow", "right_wrist"]
    },

    "angle_thresholds": {
        "extended": 160,
        "flexed": 70,
        "min_range": 70
    },

    # coaching
    "form_targets": {
        "ideal_extended": 175,
        "ideal_flexed": 65,
        "ideal_range": 110
    },

    "speed_thresholds": {
        "fast": 0.7,
        "slow": 3.0
    },

    "logging": {"log_dir": "workout_logs"},

    "feedback": {
        "use_llm": True,
        "provider": "openai",

    }
},

"pull_up": {

    "indices": {
        "left_shoulder": 5, "right_shoulder": 6,
        "left_elbow": 7, "right_elbow": 8,
        "left_wrist": 9, "right_wrist": 10
    },

    "angle_definition": {
        "left": ["left_shoulder", "left_elbow", "left_wrist"],
        "right": ["right_shoulder", "right_elbow", "right_wrist"]
    },

    "angle_thresholds": {
        "extended": 170,
        "flexed": 55,
        "min_range": 80
    },

    # coaching
    "form_targets": {
        "ideal_extended": 175,
        "ideal_flexed": 65,
        "ideal_range": 110
    },

    "speed_thresholds": {
        "fast": 0.7,
        "slow": 3.5
    },

    "logging": {"log_dir": "workout_logs"},

    "feedback": {
        "use_llm": True,
        "provider": "openai",

    }
},

}