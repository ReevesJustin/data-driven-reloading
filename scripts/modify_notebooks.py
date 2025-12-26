import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path
import os

repo = 'ReevesJustin/data-driven-reloading'
notebooks_dir = Path('notebooks')

# Key takeaways for each notebook
takeaways_dict = {
    '00_Welcome_and_Why_This_Matters.ipynb': [
        'Chasing perfect reloading results often leads to frustration due to natural variation',
        'Small sample sizes can produce misleading results by pure luck',
        'This resource provides tools to distinguish real improvements from random noise',
        'Understanding statistics helps avoid wasting time and money on false leads',
        'Interactive notebooks demonstrate how statistical concepts apply to reloading'
    ],
    '01_The_Biggest_Lie_in_Reloading_Testing.ipynb': [
        'Small sample sizes in reloading tests lead to unreliable results',
        'Statistical significance requires adequate sample sizes',
        'Common testing practices often fail to detect real differences',
        'Simulation shows how luck can create false positives',
        'Proper testing methodology prevents chasing illusions'
    ],
    '02_What_We_Actually_Mean_by_Consistency.ipynb': [
        'Consistency in reloading involves multiple dimensions beyond just velocity',
        'Standard deviation alone doesn\'t tell the full story',
        'Group size and accuracy are crucial components of consistency',
        'Real-world shooting conditions affect perceived consistency',
        'Understanding variation helps set realistic expectations'
    ],
    '03_How_Many_Shots_Do_You_Really_Need.ipynb': [
        'Sample size calculations determine minimum shots needed for reliable results',
        'Statistical power analysis helps design effective tests',
        'Too few shots lead to inconclusive or misleading outcomes',
        'Different variables require different sample sizes',
        'Proper sample planning saves time and resources'
    ],
    '04_Testing_One_Thing_at_a_Time.ipynb': [
        'Multivariate testing can mask individual variable effects',
        'Isolating variables ensures clear attribution of results',
        'Sequential testing approach reveals true relationships',
        'Confounding variables complicate interpretation',
        'Systematic testing methodology leads to reliable conclusions'
    ],
    '05_Velocity_Data_-_What_to_Measure_and_How_to_Think_About_It.ipynb': [
        'Multiple velocity metrics provide comprehensive performance picture',
        'Extreme spread and standard deviation have different meanings',
        'Velocity stability affects precision more than absolute values',
        'Temperature sensitivity impacts real-world performance',
        'Proper data collection methods ensure meaningful results'
    ],
    '06_Group_Size_and_Accuracy_-_Beyond_the_Best_Group.ipynb': [
        'Single group measurements are unreliable indicators of accuracy',
        'Statistical analysis of group distributions reveals true capability',
        'Outlier groups can skew perceptions of performance',
        'Confidence intervals provide realistic accuracy expectations',
        'Multiple group analysis prevents over-optimistic conclusions'
    ],
    '07_Real_Examples_-_Dissecting_Common_Myths.ipynb': [
        'Common reloading myths often stem from poor statistical practices',
        'Real data analysis debunks many popular claims',
        'Case studies show how proper analysis changes conclusions',
        'Forum advice frequently lacks statistical rigor',
        'Evidence-based approach replaces anecdotal wisdom'
    ],
    '08_Your_Experiments_Template.ipynb': [
        'Structured experimental design ensures reliable results',
        'Templates provide systematic approach to testing',
        'Proper data collection and analysis methods',
        'Replicable methodology for consistent outcomes',
        'Framework for testing any reloading variable'
    ],
    '09_Reasonable_Expectations_-_What_Real_Precision_Looks_Like.ipynb': [
        'Real-world precision limits exist for all shooting systems',
        'Component variation sets fundamental boundaries',
        'Statistical analysis defines achievable performance levels',
        'Understanding limits prevents unrealistic goals',
        'Accepting natural variation leads to better satisfaction'
    ],
    '10_When_Is_A_Result_Real.ipynb': [
        'Statistical significance testing determines if results are real',
        'P-values and confidence levels quantify result reliability',
        'Type I and Type II errors affect conclusion validity',
        'Power analysis ensures adequate test sensitivity',
        'Proper statistical methods validate or refute claims'
    ],
    '10_When_IS_a_Result_Real.ipynb': [  # assuming duplicate
        'Statistical significance testing determines if results are real',
        'P-values and confidence levels quantify result reliability',
        'Type I and Type II errors affect conclusion validity',
        'Power analysis ensures adequate test sensitivity',
        'Proper statistical methods validate or refute claims'
    ],
    '11_Peer_Review_Your_Own_Data.ipynb': [
        'Self-review process catches common analytical errors',
        'Checklists ensure thorough data examination',
        'Bias recognition improves result interpretation',
        'Critical thinking about data prevents false conclusions',
        'Systematic review methodology enhances reliability'
    ],
    '12_What_About_The_Pros.ipynb': [
        'Professional reloading practices incorporate statistical methods',
        'Industry standards balance precision and practicality',
        'Expert techniques build on fundamental principles',
        'Professional results achieved through systematic approaches',
        'Learning from experts requires understanding their methods'
    ]
}

# Get all ipynb files, sorted
files = sorted(notebooks_dir.glob('*.ipynb'))

for file in files:
    print(f"Processing {file.name}")
    nb = nbformat.read(str(file), as_version=4)
    
    # Add badges at top
    badge_source = f"""[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/{repo}/blob/main/notebooks/{file.name})

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/{repo}/main?filepath=notebooks/{file.name})"""
    badge_cell = nbformat.v4.new_markdown_cell(source=badge_source)
    nb.cells.insert(0, badge_cell)
    
    # Estimate time to complete based on number of code cells
    code_cells = [c for c in nb.cells if c.cell_type == 'code']
    time_est = '10-15 minutes' if len(code_cells) < 20 else '20-30 minutes'
    time_cell = nbformat.v4.new_markdown_cell(source=f"Time to complete: {time_est}")
    nb.cells.insert(1, time_cell)
    
    # Execute the notebook to embed outputs
    try:
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': str(notebooks_dir)}})
        print(f"Executed {file.name}")
    except Exception as e:
        print(f"Execution failed for {file.name}: {e}")
    
    # Add Key Takeaways
    takes = takeaways_dict.get(file.name, ['Summary of main points from the notebook'])
    takeaways = "> **Key Takeaways**\n" + '\n'.join(f"> - {t}" for t in takes)
    takeaways_cell = nbformat.v4.new_markdown_cell(source=takeaways)
    nb.cells.append(takeaways_cell)
    
    # Add next/previous links
    idx = files.index(file)
    prev_link = f"[Previous: {files[idx-1].name}]({files[idx-1].name})" if idx > 0 else "Previous: None"
    next_link = f"[Next: {files[idx+1].name}]({files[idx+1].name})" if idx < len(files)-1 else "Next: None"
    links_source = f"{prev_link} | {next_link}"
    links_cell = nbformat.v4.new_markdown_cell(source=links_source)
    nb.cells.append(links_cell)
    
    # Save back
    nbformat.write(nb, str(file))
    print(f"Saved {file.name}")