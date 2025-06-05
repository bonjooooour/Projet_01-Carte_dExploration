# Evolving World Exploration Map


### Description

This project aims to display on a world map all the places and areas visited during my photographic walks or sporting activities (running, cycling, walking). The explored geographical areas are represented by graduated color clouds, indicating the intensity of visits to each area (similar to a "heatmap"). 
The data comes from two sources: Apple Photos’ location metadata is used to map photographic explorations, while Strava provides GPS tracks for sporting activities. 
Users can fully customize the map using data from their own activities and it evolves as new data is added.


### Result (with my own data)


**Overview of the World:**

![Overview of the World:](data/05_readme_images_and_videos/Final_exploration_map_overview_screenshot_overview.png)


**Zoomed view on Paris, France:**

![Zoomed view on Paris, France:](data/05_readme_images_and_videos/Final_exploration_map_overview_screenshot_paris.png)


**Complete video demonstration:**

<p align="center">
  <a href="data/05_readme_images_and_videos/Final_exploration_map_overview_video.mp4">
    <img src="data/05_readme_images_and_videos/icon_video.png" alt="Watch video" width="50"/>
  </a>
</p>

### Features

- Collects position data from:
  1. Personal sporting activities recorded on the Strava app, exportable via a downloadable archive file from the website.
  2. Position metadata from personal photos stored in the Apple Photos library (macOS).
- Conversion and normalization of data into CSV files.
- Aggregation of all data into a single normalized CSV file.
- Reduction of the amount of geographical data to optimize display.
- Generation of an interactive map to visualize, through colored clouds, the areas of the world visited by the user.


### Tools Used

- **Python**: The primary programming language used for this project.
- **Folium**: A Python library used to create interactive maps. It allows the visualization of geographical data on an interactive Leaflet map, ideal for displaying heatmaps and custom map visualizations.
- **osxphotos**: A Python library to interact with Apple Photos on macOS, allowing the extraction of photo metadata, including geographical coordinates.
- **Pandas**: An ideal library for manipulating and analyzing large volumes of data and formatting into CSV files.
- **gpx_converter**: A tool used to convert GPX files into other formats, such as CSV.
- **fitparse**: A library for analyzing, extracting, and converting data from FIT format files, a common format for activity data from devices like GPS watches and sensors.
- **gzip**: A file format used for compressing and decompressing files, particularly useful for managing large datasets and archives efficiently.
- **scipy.spatial**: A SciPy module that provides spatial algorithms and data structures, used here to implement the nearest neighbors algorithm to reduce the amount of geographical data.


### Installation

To install and run this project, follow these steps:

1. Clone the repository to your local machine.
2. Make sure you have Python installed (preferably Python 3.8 or later).
3. Install the necessary dependencies with `pip install -r requirements.txt`.


### Requirements

- Use of macOS is necessary for extracting position data from photos. This version of the project can only extract this metadata from the Apple Photos application.


### Usage

0. Start by creating the folders specified in the REQUIRED_DIRECTORIES.txt file, located inside the data/ directory.
1. On the [Strava](https://www.strava.com) website, from your personal space, request an export of your personal data. It will be sent to you by email.
2. Import your Strava activity archive received by email into the `data/01_strava_RAW_files` folder.
3. Run the main script with `python script_00_main.py`.
4. The personalized exploration map will be generated and stored in the `data/04_final_FOLIUM_MAP` folder.
5. To update the map with new data:
   - If from photos: Run the main script again.
   - If from Strava: Import the new archive file, then run the main script again.


### Project Structure

- `script_00_main.py`: Main script that automates the entire process.
- `script_01_apple_photos_data_scrap_to_csv.py`: Collects geographical metadata from photos stored in the Apple Photos library and stores it in a CSV file.
- `script_02_strava_activities_data_to_csv.py`: Converts Strava activity geographical data into CSV.
- `script_03_multiple_to_one_csv.py`: Aggregates all data into a single normalized CSV file.
- `script_04_data_reduction_algorithm.py`: Reduces the amount of geographical data using a nearest neighbors algorithm.
- `script_05_folium_map_generator.py`: Generates the interactive and personalized world map.


### Contribution

Contributions are welcome! To contribute, please follow these steps:

1. Fork the project.
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.


### License

Distributed under the MIT License. See `LICENSE` for more information.


### Contact

For any questions or comments, please contact me at **m.gerenius@outlook.com**.
