# Service Desk Ticket Analysis and Optimization

This project uses Python to analyze and optimize service desk ticket resolution times. The process involves data cleaning, visualization, building predictive models, and generating optimization recommendations.

## Project Structure
- `data/service_desk_data.csv`: Raw data file.
- `data/service_desk_cleaned.csv`: Cleaned data.
- `src/data_cleaning.py`: Script to clean the data.
- `src/data_visualization.py`: Script to visualize the data.
- `src/model_training.py`: Script to train the model and evaluate its performance.
- `src/optimization.py`: Script to generate optimization recommendations.

## How to Run the Project
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Generate data:
   ```bash
   python src/generate_data.py
   ```
3. Clean data:
   ```bash
   python src/data_cleaning.py
   ```
4. Visualize data:
   ```bash
   python src/data_visualization.py
   ```
5. Train the model:
   ```bash
   python src/model_training.py
   ```
6. Get optimization recommendations:
   ```bash
   python src/optimization.py
   ```

## Data Visualization

Here is an example of a data visualization showing ticket resolution time distribution:

![Ticket Resolution Time Distribution](images/Screenshot%202025-01-08%20141502.png)
![Ticket Resolution Time Distribution](images/Screenshot%202025-01-08%20141519.png)


## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Faker (for generating mock data)

## License
This project is licensed under the MIT License.

