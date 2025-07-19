# 🌸 Lavender Lifestyle Store - Real-Time Revenue Prediction Dashboard

A sophisticated Streamlit application that provides real-time revenue predictions for a cosmetics retail store using machine learning models and live data simulation.

## 🚀 Features

- **Real-Time Revenue Predictions**: ML-powered revenue forecasting using trained models
- **Live Data Simulation**: Generates realistic transaction data with customizable parameters
- **Interactive Dashboard**: Beautiful Streamlit interface with dynamic visualizations
- **Multi-Category Analytics**: Tracks performance across Skincare, Makeup, Haircare, and Bodycare
- **Membership Insights**: Analyzes revenue patterns across Premium, Gold, and Starter tiers
- **Platform Comparison**: Monitors performance across Website, Quickcom, Offline, and ecom channels
- **Real-Time Charts**: Live updating line charts and aggregate bar charts
- **Customizable Speed**: Adjustable simulation speed for testing and demonstration

## 📋 Requirements

```
pandas>=1.3.0
numpy>=1.21.0
streamlit>=1.0.0
joblib>=1.0.0
scikit-learn>=1.0.0
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/lavender-lifestyle-store
   cd lavender-lifestyle-store
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure your trained model is available**
   - Place your trained model file as `cosstorerev_model.pkl` in the project directory
   - The model should be a scikit-learn compatible model with `.feature_names_in_` attribute

## 🎯 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the Dashboard

1. **Start the Simulation**: Click "Start Simulation" to begin real-time data generation
2. **Adjust Speed**: Use the slider to control simulation speed (1-5 seconds per batch)
3. **View Information**: Click "Show Information" for details about the prediction system
4. **Monitor Metrics**: Observe real-time line charts and aggregate bar charts

## 📊 Data Features

The application simulates and processes the following features:

| Feature | Description | Values |
|---------|-------------|---------|
| `Time_of_purchase` | Transaction timestamp | Last 30 days |
| `Product_category` | Product type | Skincare, Makeup, Haircare, Bodycare |
| `Product_price` | Item price in currency | ₹500 - ₹5000 |
| `Quantity` | Number of items | 1-5 units |
| `Membership` | Customer tier | Premium, Gold, Starter |
| `Platform_used` | Purchase channel | Website, Quickcom, Offline, ecom |

## 🤖 Machine Learning Model

The application expects a pre-trained scikit-learn model with the following characteristics:

- **Input**: Preprocessed features with one-hot encoding for categorical variables
- **Output**: Revenue predictions in numerical format
- **Format**: Joblib pickle file (`cosstorerev_model.pkl`)
- **Requirements**: Must have `feature_names_in_` attribute for feature alignment

## 📈 Dashboard Components

### Real-Time Visualization
- **Live Data Table**: Shows latest 10 transactions with predictions
- **Time Series Chart**: Real-time line chart of predicted revenue over time
- **Aggregate Metrics**: Bar chart showing average revenue by product category

### Interactive Controls
- **Simulation Speed Slider**: Control data generation frequency
- **Information Panel**: Contextual help about the prediction system
- **Start/Stop Controls**: Manage simulation state

## 🔧 Configuration

### Model Configuration
```python
model_path = "cosstorerev_model.pkl"  # Update path as needed
```

### Data Simulation Parameters
```python
n_samples = 100  # Number of samples per batch
simulation_batches = 10  # Number of simulation rounds
date_range = 30  # Days of historical data
```

## 🐛 Troubleshooting

### Common Issues

1. **Model File Not Found**
   ```
   Error: Model file not found! Please provide a valid path.
   ```
   - Ensure `cosstorerev_model.pkl` exists in the project directory
   - Update `model_path` variable if using a different location

2. **Feature Mismatch**
   - The model expects specific feature names from training
   - Preprocessing automatically handles missing features by adding zero columns

3. **Memory Issues**
   - Large datasets may cause performance issues
   - Adjust `n_samples` parameter to reduce batch sizes

## 📝 Code Structure

```
lavender-lifestyle-store/
├── app.py                 # Main Streamlit application
├── cosstorerev_model.pkl  # Trained ML model
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the interactive dashboard
- Uses [scikit-learn](https://scikit-learn.org/) for machine learning capabilities
- Data visualization powered by [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/)

## 📞 Support

For questions or issues, please:
- Open an issue on GitHub
- Contact the development team
- Check the troubleshooting section above

---

**⭐ Star this repository if you find it useful!**