# Project Structure

```
data-driven-reloading/
├── .git/
├── data/
│   ├── bad_data_zoo.csv
│   ├── example_velocities.csv
│   ├── messy_velocity_data.csv
│   ├── real_world/
│   │   ├── flyer_identification.csv
│   │   └── small_sample_illusion.csv
│   ├── simulated/
│   │   ├── group_size_simulation.csv
│   │   ├── ocw_test_simulation.csv
│   │   ├── velocity_10fps_sd_1000shots.csv
│   │   ├── velocity_15fps_sd_1000shots.csv
│   │   ├── velocity_20fps_sd_1000shots.csv
│   │   ├── velocity_5fps_sd_1000shots.csv
│   │   └── velocity_ladder_test_raw.csv
│   └── templates/
│       ├── group_measurement_template.csv
│       ├── load_comparison_template.csv
│       └── velocity_log_template.csv
├── docs/
│   ├── mobile_app_plan.md
│   ├── myth_origins.md
│   └── Rules.md
├── notebooks/
│   ├── md/
│   │   ├── 00_Welcome_and_Why_This_Matters.md
│   │   ├── 00_Welcome_and_Why_This_Matters.nbconvert.md
│   │   ├── 01_The_Biggest_Lie_in_Reloading_Testing.md
│   │   ├── 01_The_Biggest_Lie_in_Reloading_Testing.nbconvert.md
│   │   ├── 02_What_We_Actually_Mean_by_Consistency.md
│   │   ├── 02_What_We_Actually_Mean_by_Consistency.nbconvert.md
│   │   ├── 03_How_Many_Shots_Do_You_Really_Need.md
│   │   ├── 04_Testing_One_Thing_at_a_Time.md
│   │   ├── 05_Velocity_Data_-_What_to_Measure_and_How_to_Think_About_It.md
│   │   ├── 05_Velocity_Data_-_What_to_Measure_and_How_to_Think_About_It.nbconvert.md
│   │   ├── 06_Group_Size_and_Accuracy_-_Beyond_the_Best_Group.md
│   │   ├── 06_Group_Size_and_Accuracy_-_Beyond_the_Best_Group.nbconvert.md
│   │   ├── 07_Real_Examples_-_Dissecting_Common_Myths.md
│   │   ├── 08_Your_Experiments_Template.md
│   │   ├── 08_Your_Experiments_Template.nbconvert.md
│   │   ├── 09_Reasonable_Expectations_-_What_Real_Precision_Looks_Like.md
│   │   ├── 09_Reasonable_Expectations_-_What_Real_Precision_Looks_Like.nbconvert.md
│   │   ├── 10_When_Is_A_Result_Real.md
│   │   ├── 10_When_IS_a_Result_Real.md
│   │   ├── 10_When_IS_a_Result_Real.nbconvert.md
│   │   ├── 10_When_Is_A_Result_Real.md
│   │   ├── 11_Peer_Review_Your_Own_Data.md
│   │   ├── 11_Peer_Review_Your_Own_Data.nbconvert.md
│   │   ├── 12_What_About_The_Pros.md
│   │   └── 12_What_About_The_Pros.nbconvert.md
│   └── static/
│       ├── plot_1.png
│       ├── plot_2.png
│       └── plot_3.png
├── .gitignore
├── README.md
└── requirements.txt
```

Note: The `.git` directory (git repository) and `scripts` folder (with run_notebooks.sh) are present but not fully expanded in this view. The `notebooks/executed/` folder (containing executed notebook versions) is also part of the structure but not shown here.