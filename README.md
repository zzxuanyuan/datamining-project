# project-panel

This is our project for CSCE474/874 Intro to Data Mining. Our project is to identify human activities.

# src directory
1. It contains fft.py. It calculates fft and plot data both in frequency domain and time domain. To use fft.py, simply put data file as argument. For example, python fft.py $PROJECT/data/run1.csv.
2. preprocess.py is to extract our raw data to formatted data with features as attributes.
3. We completely separate DC component from other FFT samples because this value(fft[0]) is very large and also very important to evaluate as a new feature.
4. One of the features is called Power, this feature is the power of all frequency coefficients except the DC component. We identify the values of this feature are relatively small (10^-5~10^-6), and therefore we use logarithmic of base 10 to represent this feature.

# data directory
1. It contains collected data from SensorLog.
2. In preprocess.py, it needs to search the filename to identify activities. Please make sure your data file name contain an "activity". For example, run123.csv and myrun.csv are good file names for activity RUN.
3. In genfile.sh, it uses data file set {1,2,3,4} to train the model, and test on the data set {5}. In case we would collect more data in future, please modify this file to generate data and test files.
